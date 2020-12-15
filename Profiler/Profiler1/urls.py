from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('ttt/', views.tesst, name='tesst'),
    path('register/', views.home_view, name='home_view'),
    path('<str:student_di>/tes/', views.tes, name='tes'),
    path('<str:staff_di>/tes2/', views.tes2, name='tes2'),
    path('<str:student_di>/register-courses/', views.to_regCourses, name='register-courses'),
    path('<str:student_di>/registered-courses/', views.regCourses, name='registered-courses'),
    path('<str:person>/<str:level>/register/', views.regcourseview, name='register'),
]
