from django.urls import path
from accounts.views import UserRegistrationView, UserLoginView


urlpatterns = [
    path('signup/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    ]