from django.urls import path

from users.views import loginView
from users.views import logoutView
from users.views import verifyView
from users.views import registerView

urlpatterns = [
     path('my-account/', loginView, name='my-account'),
     path('my-account/register',registerView, name='register'),
     path('my-account/logout', logoutView, name='logout'),
     path('confirm-verify-code/', verifyView, name='confirm')
]
