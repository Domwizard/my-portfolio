from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path("", views.home, name="home"),
    path("project/<int:pk>/", views.project_detail, name="project_detail"), # НОВАЯ СТРОКА
]
