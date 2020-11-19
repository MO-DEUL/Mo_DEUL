from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.UserView.as_view()),
    path('<int:id>', views.UserView.as_view()),
    path('login', views.LoginView.as_view(), name='login'),
    path('login/kakao', views.kakao_login, name="kakao-login"),
    path('login/kakao/callback', views.kakao_callback, name="kakao-callback"),
]
