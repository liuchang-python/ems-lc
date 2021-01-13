from django.urls import path

from api import views

urlpatterns = [
    path('user/',views.UserAPIView.as_view()),
    path('employee/',views.EmployeeAPIView.as_view()),
    path('employee/<str:pk>',views.EmployeeAPIView.as_view()),

]