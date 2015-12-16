from django.conf.urls import patterns, include, url 
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^drafts/$',	views.post_draft_list,	name='post_draft_list'),
	url(r'^post/(?P<pk>[0-9]+)/publish/$',	views.post_publish,	name='post_publish'),
	url(r'^post/(?P<pk>[0-9]+)/remove/$',	views.post_remove,	name='post_remove'),
	url(r'^accounts/login/$',	'django.contrib.auth.views.login'),
	url(r'^post/(?P<pk>[0-9]+)/comment/$',	views.add_comment_to_post,	name='add_comment_to_post'),
	url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
	url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]