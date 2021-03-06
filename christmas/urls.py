from django.conf.urls import url
from django.shortcuts import render

from .views import *

urlpatterns = [
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^$', GroupCreateView.as_view(), name='create_group'),
    url(r'^(?P<group_id>[0-9A-Za-z]+)/$', GroupUpdateView.as_view(), name='view_group'),
    url(r'^(?P<group_id>[0-9A-Za-z]+)/invite/$', InviteView.as_view(), name='invite'),
    url(r'^(?P<group_id>[0-9A-Za-z]+)/create/$', ListCreateView.as_view(), name='create_list'),
    url(r'^(?P<group_id>[0-9A-Za-z]+)/(?P<list_id>[0-9]+)/$', ListUpdateView.as_view(), name='view_list'),
    url(r'^(?P<group_id>[0-9A-Za-z]+)/(?P<list_id>[0-9]+)/delete/$', ListDeleteView.as_view(), name='delete_list'),
    url(r'^(?P<group_id>[0-9A-Za-z]+)/(?P<list_id>[0-9]+)/create/$', ItemCreateView.as_view(), name='create_item'),
    url(r'^(?P<group_id>[0-9A-Za-z]+)/(?P<list_id>[0-9]+)/(?P<item_id>[0-9]+)/$', ItemUpdateView.as_view(), name='view_item'),
    url(r'^(?P<group_id>[0-9A-Za-z]+)/(?P<list_id>[0-9]+)/(?P<item_id>[0-9]+)/delete/$', ItemDeleteView.as_view(), name='delete_item'),
]