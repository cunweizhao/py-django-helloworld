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
# import requests
# from django.views.generic import View
# from django.http import JsonResponse
#
#
#
#
# class Music(View):
#
#       DOUBAN_MUSIC_API = 'https://api.douban.com/v2/music/search?q={0}'
#       def get(self,request):
#             music_name = request.GET.get('musicname','')
#             if not music_name:
#                 return JsonResponse({'errcode':-1,'errmsg':'音乐名称不能为空'})
#             url = self.DOUBAN_MUSIC_API.format(music_name)
#             response = requests.get(url)
#             data = response.json()
#             return JsonResponse({'errcode':0,'errmsg':'成功','data':data})
#
# # 获取电影
# class Movie(View):
#       DOUBAN_MOVIE_API ='https://api.douban.com/v2/movie/search?q={0}'
#       def get(self,request):
#             movie_name = request.GET.get('moviename','')
#             if not movie_name:
#                   return JsonResponse({'errcode': -1, 'errmsg': '电影名称不能为空'})
#             url =self.DOUBAN_MOVIE_API.format(movie_name)
#
#             try:
#                   response = request.get(url)
#             except Exception as e:
#                   return JsonResponse({'errcode': -1,'errmsg':str(e)})
#             if response.status_code !=200:
#                   return JsonResponse({'errcode':-1,'errmsg':'请求豆瓣异常'})
#             data = response.json()
#
#             return JsonResponse({'errcode':0,'errmsg':'成功','data':data})
# # 获取图书
# class Book(View):
#       DOUBAN_BOOK_API = 'http://api.douban.com/v2/book/search?q={0}'
#
#       def get(self,request):
#             book_name = request.GET.get('bookname','')
#             if not book_name:
#                   return JsonResponse({'errcode' : -1,'errmsg':'图书名称不能为空'})
#             url = self.DOUBAN_BOOK_API.format(book_name)
#
#             response =requests.get(url)
#             data = response.json()
#             return JsonResponse({'errcode':0,'errmsg':'成功','data':data})



#=====================================================================================

from django.shortcuts import render
from django.views.generic import View

class Index(View):
      TEMPLATE = 'index.html'

      def get(self,request,name):

            data = {}
            data['name'] = name
            data['array'] = range(10)

            return render(request,self.TEMPLATE,data)
