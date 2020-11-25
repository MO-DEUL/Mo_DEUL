from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('<int:id>/', views.UserView.as_view()),
]
