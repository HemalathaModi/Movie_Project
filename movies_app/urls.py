from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name = 'delete'),
    path('list/', views.list, name='list'),
    path('favorites/', views.favorites, name='favorites'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)