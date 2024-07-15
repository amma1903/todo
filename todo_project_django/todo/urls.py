from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TodoItemViewSet, UserCreateAPIView

router = DefaultRouter()
router.register(r'todos', TodoItemViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserCreateAPIView.as_view({'post': 'create'}), name='user-create'),
]
