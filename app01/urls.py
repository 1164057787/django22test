from django.urls import path
from app01.views import login,LoginClass

urlpatterns = [
    path('login/', login),
    path("login1/",LoginClass.as_view())
]


