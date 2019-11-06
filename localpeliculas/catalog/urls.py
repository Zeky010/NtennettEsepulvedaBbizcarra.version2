from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('peliculas/', views.peliculaListView.as_view(),name='peliculas'),
    path('pelicula/<int:pk>/', views.peliculaDetailView.as_view(),name='pelicula-detail'),
    path('autor/<int:pk>/', views.autorDetailView.as_view(),name='autor-detail'),
]


urlpatterns += [
    path('pelicula/create/', views.peliculaCreateView.as_view(), name='pelicula-create'),
    path('pelicula/<int:pk>/update/', views.peliculaUpdate.as_view(), name='pelicula-update'),
    path('pelicula/<int:pk>/delete/', views.peliculaDelete.as_view(), name='pelicula-delete'),
    path('autor/create/', views.autorCreate.as_view(), name='autor_create'),
    path('autor/<int:pk>/update/', views.autorUpdate.as_view(), name='autor_update'),
    path('autor/<int:pk>/delete/', views.autorDelete.as_view(), name='autor_delete'),
    path('autores/',views.autorListView.as_view(),name='autores'),
]