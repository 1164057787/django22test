"""django22test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path

from django.views.decorators.cache import cache_page

from app01 import views
from rest_framework.routers import DefaultRouter
from appsers.views import StuView,StusView,StusView2


from cachetest.views import test_cache, test_cache2


router = DefaultRouter()
router.register('books',views.BookViewSet)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('page/', include("app01.urls")),
    re_path('stu/(?P<pk>\d+)',StuView.as_view()),
    path('stus/',StusView.as_view()),
    path('stus2/',StusView2.as_view()),

    path('cache/',test_cache),
    # path('cache/',cache_page(15)(test_cache)), #也可这样使用缓存
    path('cache2/',test_cache2)
]


urlpatterns += router.urls