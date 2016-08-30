from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^destacado/(?P<deportista_id>\d+)/$', views.destacado_detail, name='destacado_detail'),
    url(r'^deportista/(?P<deporte_id>\d+)/$', views.deportista, name='deportista'),
    url(r'^login/', views.UserFormView.as_view(), name='login'),
    url(r'^logout/', views.logout_view, name='logout'),

]