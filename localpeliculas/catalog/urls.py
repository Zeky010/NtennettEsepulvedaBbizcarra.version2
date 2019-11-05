from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('peliculas/', views.peliculaListView.as_view(),name='peliculas'),
    path('pelicula/<int:pk>', views.peliculaDetailView.as_view(),name='pelicula-detail'),
    path('autor/<int:pk>', views.autorDetailView.as_view(),name='autor-detail'),
]
