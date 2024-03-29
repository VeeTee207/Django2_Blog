from django.urls import path
from .views import *

urlpatterns = [
    path('', post_list, name = 'post_list_url'),
    # path('post/<str:slug>', post_deatail , name = 'post_detail_url'),
    path('post/<str:slug>', PostDetail.as_view(), name = 'post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    # path('tag/<str:slug>', tag_detail, name = 'tag_detail_url'),
    path('tag/<str:slug>', TagDetail.as_view(), name = 'tag_detail_url'),
]


