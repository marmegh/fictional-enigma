from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^/new', views.new),
    url(r'^/create', views.create),
    url(r'^/({0-9})/edit', views.edit),
    url(r'^/({0-9})/delete', views.destroy),
    url(r'^/({0-9})', views.show),
    url(r'^', views.index),
]