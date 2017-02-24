from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import User


def index(request):
    latest_user_list = User.objects.order_by("-createdAt")[:3]
    print(latest_user_list[0].mobile)
    template = loader.get_template('mainpages/index.html')
    context = {
        latest_user_list: latest_user_list,
    }
    return HttpResponse(template.render(context, request))


def show_user(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)


def info(request, user_id):
    response = "You're looking at the info of user %s."
    return HttpResponse(response % user_id)


def user_amount(request, user_id):
    return HttpResponse("You're viewing the orders on user %s." % user_id)
