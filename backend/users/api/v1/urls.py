from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.UserView.as_view()),
    path('me/', views.MeView.as_view()),
    path('<int:pk>/', views.userDetailView.as_view()),
]
