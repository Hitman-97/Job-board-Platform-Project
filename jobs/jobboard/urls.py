from django.contrib import admin
from django.urls import path
from jobs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.job_list, name='job_list'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('post_job/', views.post_job, name='post_job'),
    path('apply_job/<int:pk>/', views.apply_job, name='apply_job'),
    path('profile/', views.profile, name='profile'),
]
