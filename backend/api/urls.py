from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
    path('users', views.UserView.as_view()),
    path('users/<int:id>', views.UserView.as_view()),
    path('houses', views.HouseView.as_view()),
    path('houses/<int:id>', views.HouseView.as_view()),
    path('community', views.CommunityView.as_view()),
    path('community/<int:id>', views.CommunityView.as_view()),
    path('community/comment', views.CommentView.as_view()),
    path('community/comment/<int:id>', views.CommentView.as_view()),
]
