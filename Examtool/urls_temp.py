from django.conf.urls import patterns, url

from Examtool import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)