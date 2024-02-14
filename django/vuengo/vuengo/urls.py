from django.contrib import admin
from django.urls import path, include
from task.views import TaskViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
]
