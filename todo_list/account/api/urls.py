from django.urls import path, include
from loguru import logger
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('bot', views.ProfileCheckViewSet)
router.register('task', views.TaskViewSet)


user_router = routers.DefaultRouter()
user_router.register('user', views.UserViewSet)

app_name = 'bot'

urlpatterns = [

    path('', include(router.urls)),
    path('bot/', include(user_router.urls)),
    path('task/<int:telegram_id>/get_tasks/', views.TaskViewSet.as_view({'get': 'get_tasks'})),

]

