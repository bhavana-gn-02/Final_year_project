"""
URL configuration for Auto_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from Auto_system import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminhome/',include("auto_admin.urls")),
    
    path('',views.captcha,name='captcha'),
    path('home/',views.home,name='home'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('driverlogin/',views.driverlogin,name='driverlogin'),
    path('driveregister/',views.driveregister,name='driveregister'),
    path('logotp/',views.logotp,name='logotp'),
    path('forget/',views.forget,name='forget'),
    path('logout/',views.logout,name='logout'),
    path('dlogout/',views.dlogout,name='dlogout'),
    path('changecpin/',views.changecpin,name='changecpin'),
    path('dchangecpin/',views.dchangecpin,name='dchangecpin'),

    path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')

    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)