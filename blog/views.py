from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    """
    主页渲染的实现
    :param request:
    :return: 返回首页渲染需要的数据库的数据
    """

    return render(request, 'home/home.html')