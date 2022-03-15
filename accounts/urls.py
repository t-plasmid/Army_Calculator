from datetime import datetime
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',
        auth_views.LoginView.as_view
        (
            template_name="accounts/login.html",
            extra_context=
                      {
                          'title': 'Log in',
                          'sidebar': 'Account',
                          'year' : datetime.now().year,
                      }
        ),
        name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('contact/', views.ContactView.as_view(), name="contact"),
]
