from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    
    url(r'^about/$', views.about, name="about"),
    url(r'^art/$', views.art, name="art"),
    url(r'^contacts/$', views.contact, name="contacts"),
]
