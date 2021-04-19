from django.urls import path
from . import views

app_name = 'houses'
urlpatterns = [
    path("list/", views.HousesView.as_view()),
    path("search/", views.search_house),
    path('<int:pk>/', views.HouseView.as_view())
]
