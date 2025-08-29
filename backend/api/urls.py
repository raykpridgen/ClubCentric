from django.urls import path
from .views import ClubCreate, ClubDetail

urlpatterns = [
    path('tasks/', ClubCreate.as_view(), name='task-list'),
    path('tasks/<int:pk>/', ClubDetail.as_view(), name='task-detail'),
]