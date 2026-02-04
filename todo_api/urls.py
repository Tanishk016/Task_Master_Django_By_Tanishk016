from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.web_index, name='web_index'),
    
    # NEW: Paths for deleting and updating
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('toggle/<int:pk>/', views.toggle_task, name='toggle_task'),
    
    # NEW: The Edit Path
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),


    
    # NEW: The Sign Up Path
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

]