from django.conf.urls import url, include

from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^deportes/', views.lista_deportes, name='lista_deportes'),
    url(r'^destacado/(?P<deportista_id>\d+)/$', views.destacado_detail, name='destacado_detail'),
    url(r'^deportista/(?P<deporte_id>\d+)/$', views.deportista, name='deportista'),
    url(r'^evento/(?P<deportista_id>\d+)/$', views.evento, name='evento'),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^crear_usuario$', views.post_usuario, name='post_usuario'),
    url(r'^login/', views.login_view, name="login"),
]