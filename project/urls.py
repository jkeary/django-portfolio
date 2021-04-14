from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:project_type>', views.listview, name='listview'),
    path('<int:project_id>/', views.projectview, name='projectview'),
]
