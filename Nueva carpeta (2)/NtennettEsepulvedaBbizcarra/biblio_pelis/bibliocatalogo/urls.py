from django.urls import path
from django.views.generic import ListView
from . import views


urlpatterns = [
   path('user/<int:pk>', views.DetalleVistaUsuario.as_view(), name='user-detail'),
]

urlpatterns += [
    path('user/create/', views.creacion_usuario.as_view(), name='CreateView'),
    path('user/<int:pk>/update/', views.Actualizacion_usuario.as_view(), name="UpdateView"),
    path('user/<int:pk>/delete', views.Eliminacion_usuario.as_view(), name='DeleteView')
    
]