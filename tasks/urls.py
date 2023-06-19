from django.contrib import admin
from django.urls import path
from tasks.views import task_list, create_task, update_task, delete_task,register,user_login,user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('t/', task_list, name='task_list'),
    path('task/create/', create_task, name='create_task'),
    path('task/update/<int:pk>/', update_task, name='update_task'),
    path('task/delete/<int:pk>/', delete_task, name='delete_task'),
    path('register/', register, name='register'),
    path('',user_login, name='login'),
    path('logout/',user_logout, name='logout'),

    
]
