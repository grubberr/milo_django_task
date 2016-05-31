
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new_user, name='new'),
    url(r'^edit/(?P<user_id>[0-9]+)/$', views.edit_user, name='edit'),
    url(r'^delete/(?P<user_id>[0-9]+)/$', views.delete_user, name='delete'),
    url(r'^download/$', views.download, name='download'),
]
