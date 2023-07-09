from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.contrib.auth import views

from userextend.forms import AuthenticationNewForm, PasswordChangeNewForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('service.urls')),
    path('', include('agent.urls')),
    path('', include('userextend.urls')),
    path("login/", views.LoginView.as_view(form_class=AuthenticationNewForm)),
    path('logout/', LogoutView.as_view(next_page='homepage'), name='logout'),
    path("password_change/", views.PasswordChangeView.as_view(form_class=PasswordChangeNewForm),
         name="password-change-form"),
    path('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
