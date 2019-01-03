from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from tc_translations.main.views import dashboard

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', dashboard, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='base.jinja'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='base.jinja'), name='logout'),
]
