from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student_detail'),
    path('student/register', views.StudentCreateView.as_view(), name='student_register'),
    path('student/<int:pk>/delete', views.StudentDelete.as_view(), name='student_delete'),
]