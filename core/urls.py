from django.urls import path
from core.views import *


app_name = 'core'

urlpatterns = [
    #path('', HomeView.as_view(), name='home'),
    path('', LoginView.as_view(), name='home'),
    path('user-register/', UserRegistrationView.as_view(), name='user-register'),
    path('user-login/', LoginView.as_view(), name='user-login'),
    path('user-logout/', UserLogout, name='user-logout'),
]
