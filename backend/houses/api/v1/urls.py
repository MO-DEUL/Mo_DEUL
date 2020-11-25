from django.urls import path
from . import views

app_name = 'houses'
urlpatterns = [
    path('<int:id>/', views.HouseView.as_view())
]
