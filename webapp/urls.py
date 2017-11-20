from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^cat$', views.catnote, name='catnote'),
	url(r'^tuna$', views.tunanote, name='tunanote'),
    url(r'^hey/', views.index, name='index'),



]