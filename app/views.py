#coding:utf-8

# from django.views.generic import View
# from django.http import HttpResponse
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
# class LessionTwo(View):
#
#     def get(self,request):
#
#         message = request.GET.get('message','这里没有内容')
#         return HttpResponse(message)


# 获取音乐
import requests
from django.views.generic import View
from django.http import JsonResponse

class Music(View):

      DOUBAN_MUSIC_API = 'https://api.douban.com/v2/music/search?q={0}'
      def get(self,request):
            music_name = request.GET.get('musicname','')
            if not music_name:
                return JsonResponse({'errcode':-1,'errmsg':'音乐名称不能为空'})
            url = self.DOUBAN_MUSIC_API.format(music_name)
            response = requests.get(url)
            data = response.json()
            return JsonResponse({'errcode':0,'errmsg':'成功','data':data})