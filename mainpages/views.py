from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404
#from django.template import loader

from .models import User, Order


def index(request):
    latest_user_list = User.objects.order_by("-createdAt")[:3]
    print(latest_user_list[0].mobile)
    #template = loader.get_template('mainpages/index.html')
    context = {
        "latest_user_list": latest_user_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'mainpages/index.html', context)  #  return a HttpResponse object


def showuser(request, mobile):
    """
    try:
        user = User.objects.get(mobile=mobile)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    """
    user = get_object_or_404(User, mobile=mobile)
    return render(request, 'mainpages/show_user.html', {"user": user})


def info(request, user_id):
    response = "You're looking at the info of user %s."
    return HttpResponse(response % user_id)


def useramount(request, mobile):
    user = get_object_or_404(User, mobile=mobile)
    try:
        selected_order = user.order_set.get(out_trade_no=request.POST['order'])
    except(KeyError, Order.DoesNotExist):

    return HttpResponse("You're viewing the orders on user %s." % mobile)
