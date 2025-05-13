from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('map/', views.ProjectMapView.as_view(), name='project_map'),
    path('geojson/', views.project_geojson, name='project_geojson'),
]
