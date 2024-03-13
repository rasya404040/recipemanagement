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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter
from recipes import views
from django.db.models import Q
from rest_framework.authtoken import views as rviews #import aliasing

router=SimpleRouter()
router.register('user',views.CreateUser)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # path('search/',include('search.urls')),
    path('recipes/',views.Recipelist.as_view()),
    path('reviews/',views.Reviewlist.as_view()),
    path('details/<int:pk>',views.Recipedetail.as_view()),
    path('reviews/<int:pk>',views.Reviewdetail.as_view()),
    path('search/',views.search.as_view()),
    path('logout', views.user_logout.as_view()),
    path('api-token-auth/',rviews.obtain_auth_token),#login view
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)