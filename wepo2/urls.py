from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from Examtool import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^home/', views.home, name="home"),
    #url(r'^index/', views.index, name='index'),
    url(r'^$','django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout$','django.contrib.auth.views.logout', name='logout'),
    url(r'^create/', views.create, name="create"),
    url(r'^createQuestion/', views.createQuestion, name="createQuestion"),
    url(r'^admin/', include(admin.site.urls)),
)
