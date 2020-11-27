from django.urls import path
from . import views

app_name = 'houses'
urlpatterns = [
    path("list/", views.ListHousesView.as_view()),
    path('<int:pk>/', views.SeeHouseView.as_view())
]
