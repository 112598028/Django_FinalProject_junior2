"""pms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from login import views as lviews
from flower import views as fviews
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from news import views as nviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fviews.flower),
    path('accounts/', include('allauth.urls')),
    # path('login/', lviews.login),
    # path('register/', lviews.register, name="register"),
    # path('logout/', lviews.logout),
    # path('flower/', fviews.flower),
    path('create/', fviews.create, name='create'), 
    path('flower/<slug:slug>/', fviews.detail, name='detail'),    
    path('tags/<slug:slug>/', fviews.tags, name='tags'),
    path('flower/edit/<int:pk>/', fviews.edit, name='edit'),
    path('flower/delete/<int:pk>/', fviews.delete, name='delete'),
    path('news/', nviews.news, name='news'),
    path('news/<str:pageindex>/', nviews.news, name='news'),
    path('detail/<int:detailid>/', nviews.detail, name='detail'),
    path('newsadd/', nviews.newsadd),
    path('newsedit/<int:newsid>/', nviews.newsedit),
    path('newsedit/<int:newsid>/<str:edittype>/', nviews.newsedit),
    path('newsdelete/<int:newsid>/', nviews.newsdelete),
    path('newsdelete/<int:newsid>/<str:deletetype>/', nviews.newsdelete),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
