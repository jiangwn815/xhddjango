from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from .models import User, Order, Task
from django.urls import reverse
import json, time
import requests
import os
import re
from bs4 import BeautifulSoup
from datetime import datetime
import calendar


def index(request):
    latest_user_list = User.objects.order_by("-createdAt")
    print(latest_user_list[0].mobile)
    kk = {}
    for e in latest_user_list:
        kk[e.mobile] = e.createdAt
        print(kk)

    # template = loader.get_template('mainpages/index.html')
    context = {
        "latest_user_list": latest_user_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'mainpages/index.html', context)  # return a HttpResponse object


def register(request):
    return render(request, 'mainpages/register.html')


def crawler(request):
    return render(request, 'mainpages/crawler.html')


def downloadpic(picurl, picname, piclimit=100):
    headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like "
                             "Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
               "Referer": "https://m.meitulu.com/item/6932.html",
               "Connection": "keep-alive",
               "Pragma": "no-cache",
               "Host": "mtl.ttsqgs.com",
               "Accept-Encoding": "gzip, deflate, br",
               "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
               "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
               "Cache-Control": "no-cache"
               }

    try:
        picdata = requests.get(picurl, headers=headers, timeout=20)
        print("{0} len:{1:.2f} KB".format(picurl, len(picdata.content) / 1024))
    except requests.exceptions.ConnectionError:
        print(picname + " 无法下载")
        return
    if len(picdata.content) / 1024 < piclimit:
        return

    filename = picname
    while os.path.exists('./mainpages/download/' + filename):
        filename = filename.split(r'.')[0] + "-1." + filename.split(r'.')[1]
    with open('./mainpages/download/' + filename, 'wb') as picfile:
        picfile.write(picdata.content)


def crawlerpic(request):
    ul = {}
    target_url = "https://m.meitulu.com/item/6932.html"
    home_r = requests.get(target_url)
    home_soup = BeautifulSoup(home_r.text, 'lxml')
    url_list = home_soup.find('div', id='pages').find_all('a')[1:-1]

    for url in url_list:
        url = target_url.split(r'/item')[0]+url['href']
        print(url)
        continue
        r = requests.get(url)
        print("Headers", r.request.headers)
        img_soup = BeautifulSoup(r.text, 'lxml')
        img_lists = img_soup.find_all('img')
        # lists = soup.find_all('img', class_="content_img")

        for li in img_lists:
            picname = "".join(li['src'].split(r'/')[-2:])
            picurl = li['src']
            downloadpic(picurl, picname)

    return JsonResponse(ul)

def sms(request):
    user_list = User.objects
    order_list = Order.objects
    return render(request, 'mainpages/sms.html', {"ul": user_list, "ol": order_list})


def smslist(request):
    user_list = User.objects
    order_list = Order.objects
    return render(request, 'mainpages/sms_list.html', {"ul": user_list,"ol": order_list})

def smsedit(request):
    user_list = User.objects
    order_list = Order.objects
    return render(request, 'mainpages/sms_edit.html', {"ul": user_list,"ol": order_list})

def showuser(request, mobile):
    """
    try:
        user = User.objects.get(mobile=mobile)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    """
    user = get_object_or_404(User, mobile=mobile)
    return render(request, 'mainpages/show_user.html', {"user": user})


def users(request):
    userslist = User.objects.order_by("-createdAt")
    print(type(userslist))
    ul = {}
    for e in userslist:
        ul[e.mobile] = e.createdAt
    return JsonResponse(ul)


def createuser(request):
    User.objects.create(passwd=request.POST["password"],mobile=request.POST["contactNumber"], nickname=request.POST["userName"])
    # return render(request, 'mainpages/index.html',{'latest_user_list': latest_user_list})
    return HttpResponseRedirect(reverse('mainpages:index'))


def info(request, mobile):
    user = get_object_or_404(User, mobile=mobile)
    return render(request, 'mainpages/info.html', {'user': user})


def useramount(request, mobile):
    user = get_object_or_404(User, mobile=mobile)
    try:
        selected_order = user.order_set.get(out_trade_no=request.POST['order'])
    except(KeyError, Order.DoesNotExist):
        return render(request, 'mainpages/show_user.html', {
            'user': user,
            'error_message': "Order does not exist"
        })
    else:
        selected_order.total_fee = request.POST['amount']
        selected_order.save()
    return HttpResponseRedirect(reverse('mainpages:info', args=(user.mobile,)))


def tasks(request):
    task = Task.objects.order_by("-createdAt")
    ul = {}
    no = 1
    for e in task:
        ul[no] = {"id": str(e.id),
                  "createdAt": json.dumps(calendar.timegm(e.createdAt.timetuple())*1000),
                  "taskName": e.taskName,
                  "taskStatus": e.taskStatus}
        no = no + 1
    return JsonResponse(ul)


def createtask(request):

    sendtime = datetime.fromtimestamp(float(request.POST["sendTime"]))

    Task.objects.create(taskName=request.POST["task-name"],
                        taskContent=request.POST["task-content"],
                        startAt=sendtime,
                        taskStatus=request.POST["taskStatus"],
                        senderNumber=request.POST["sender-number"],
                        receiverNumber=request.POST["receiver-number"]
                        )
    return HttpResponseRedirect(reverse('mainpages:smslist'))


def viewtask(request):
    print(request.GET['id'])
    task = get_object_or_404(Task, id=request.GET['id'])
    print(task.taskName)
    print(task.createdAt)
    return JsonResponse({
        "id": task.id,
        "taskName": task.taskName,
        "taskContent": task.taskContent,
        "taskStatus": task.taskStatus,
        "startAt": json.dumps(calendar.timegm(task.startAt.timetuple())*1000),
        "createdAt": json.dumps(calendar.timegm(task.createdAt.timetuple())*1000),
        "senderNumber": task.senderNumber,
        "receiverNumber": task.receiverNumber
    })

@csrf_exempt
def deletetask(request):
    task = get_object_or_404(Task, id=request.POST['id'])
    task.delete()
    return JsonResponse({"code": "0"})