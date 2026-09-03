from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/create/", views.post_create, name="post_create"),
    path("post/<int:id>/", views.post_detail, name="post_detail"),
    path("post/<int:id>/edit/", views.post_edit, name="post_edit"),
    path("post/<int:id>/delete/", views.post_delete, name="post_delete"),
    # Authentication
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]