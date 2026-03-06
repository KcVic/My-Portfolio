from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectsView.as_view(), name='projects'),
    path('download/<int:pk>/', views.download_pdf, name='download_pdf'),
]