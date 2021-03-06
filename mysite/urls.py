"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from mainapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RegisterPageView.as_view(), name='register-page'),
    path('login-page', LoginPageView.as_view(), name='login-page'),
    path('index/', Index.as_view(), name='index'),
    path("register", RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', Logout.as_view(), name='logout'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
