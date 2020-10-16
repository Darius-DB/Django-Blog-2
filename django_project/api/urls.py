from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
    path('v1/resources/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
]