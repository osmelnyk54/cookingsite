from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^recepts.html', views.post_list_recept_day, name='post_list_recept_day'),
    url(r'^holiday.html', views.post_list_holiday, name='post_list_holiday'),
    url(r'^health.html', views.post_list_health, name='post_list_health'),
    url(r'^modelss.html', views.post_list_modelss, name='post_list_modelss'),
    url(r'^equipment.html', views.post_list_equipment, name='post_list_equipment'),
    url(r'^thematic.html', views.post_list_thematic, name='post_list_thematic'),
]
