from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from . import views
from django.contrib.auth import views as auth
from ticketit import views as t_views
from django.conf.urls.static import static
 
urlpatterns = [
    path('login/',views.Login, name="login"),
    path('logout/',auth.LogoutView.as_view(next_page = 'home'), name="logout"),
    path('register/', views.register, name ='register'),
    path('password-reset/',
         auth.PasswordResetView.as_view(
             template_name='user/password_reset.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth.PasswordResetDoneView.as_view(
             template_name='user/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth.PasswordResetConfirmView.as_view(
             template_name='user/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth.PasswordResetCompleteView.as_view(
             template_name='user/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('update/profile/', views.update_profile, name='update_profile'),
    path('update/password/', views.update_password, name='update_password'),
]