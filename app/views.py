#coding:utf-8

from django.views.generic import View
from django.http import HttpResponse
#
# class Index(View):
#     def get(self,request,name,age):
#         return HttpResponse('Hello i am {0}, age is {1}'.format(name,age))


# 第一种参数
# def index(request):
#    name =request.GET.get('name','')
#    age = request.GET.get('age',0)
#
#    return HttpResponse('Hello i am {0},age is {1}'.format(name,age))


# 第二种
# def index(request,name,age):
#     return HttpResponse('Hello i am {0},age is {1}'.format(name,age))


# 20200804
class LessionTwo(View):

    def get(self,request):

        message = request.GET

        return HttpResponse('ok')
