#coding:utf-8


# from django.conf.urls import url
from django.urls import path
# from .views import index
from .views import Index



# 这用应用的视图与url绑定在一起了
# urlpatterns = [
#     url('',index)
# ]

# urlpatterns = [
#     path('<str:name>/<int:age>',index)
# ]

urlpatterns = [
    path('<str:name>/<int:age>',Index.as_view(), name='index')
]