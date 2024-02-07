from django.urls import path
from .views import signup,login,test_token,UserLogout

urlpatterns = [ 
        path('signup', signup),
        path('login', login),
        path('test_token', test_token),
        path('logout', UserLogout.as_view())
]
