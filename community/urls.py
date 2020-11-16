from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.CommunityView.as_view()),
    path('<int:id>', views.CommunityView.as_view()),
    path('comment', views.CommentView.as_view()),
    path('comment/<int:id>', views.CommentView.as_view())
]