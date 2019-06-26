from django.contrib import admin
from django.urls import path
from django.urls import include, path
from users.views import *
from rest_framework import routers


router = routers.DefaultRouter()

router.register('owner', OwnerViewSet)
router.register('profile', ProfileViewSet)
router.register('chain', ChainViewSet)
router.register('school', SchoolViewSet)
router.register('role', RolePersissionViewSet)
router.register('access', ProfileRoleViewSet)

urlpatterns = [

    path('',include(router.urls)),
    path('api/owner/',owner_view),
    path('api/owner/<int:id>/',owner_view_details),

]
