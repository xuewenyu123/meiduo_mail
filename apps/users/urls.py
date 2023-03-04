from django.urls import path

from apps.users.views import UsernameCountView, RegisterView


urlpatterns = [
    path('usernames/<username:username>/count/', UsernameCountView.as_view()),
    path('users/', RegisterView.as_view())
]