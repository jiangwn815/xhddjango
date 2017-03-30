from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
# from django.template import loader

from .models import User, Order
from django.urls import reverse


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

def sms(request):
    user_list = User.objects
    order_list = Order.objects
    return render(request, 'mainpages/sms.html', {"ul": user_list,"ol": order_list})

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
