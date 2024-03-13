"""
URL configuration for recipeapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from recipes import views
from rest_framework.routers import SimpleRouter
app_name = "recipes"



urlpatterns = [
    # path('recipes/', include(router.urls)),
    path('recipes/',views.Recipelist.as_view()),
    path('reviews/',views.Reviewlist.as_view()),
    path('details/<int:pk>',views.Recipedetail.as_view()),



]