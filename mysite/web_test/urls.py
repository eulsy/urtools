from django.conf.urls import url

from . import views

urlpatterns = [
    
	url(r'^del_code$', views.del_code),
    url(r'^base_info$', views.base_info),
    url(r'', views.index),
]