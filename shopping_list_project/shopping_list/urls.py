from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login_user"),
    path('logout/', views.logout_user, name="logout_user"),
    path('signup/', views.signup_user, name="signup_user"),
    path('shoppinglist/', views.shoppinglist, name="shoppinglist"),
    path('shoppinglistitems/<int:list_id>', views.shoppinglistitems, name="shoppinglistitems"),
    path('addlist/', views.addlist, name="add_list")
]
