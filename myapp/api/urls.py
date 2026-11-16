from django.urls import path
from . import views

urlpatterns=[
    path('', views.StudentListCreateAPIView.as_view()),
    path('detail/<int:id>/', views.StudentRetrieveUpdateDestroyAPIView.as_view()),
]