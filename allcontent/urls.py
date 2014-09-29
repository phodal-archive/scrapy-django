from django.conf.urls import patterns, url

from allcontent import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
)
