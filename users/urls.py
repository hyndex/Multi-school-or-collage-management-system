from django.contrib import admin
from django.urls import path
from django.urls import include, path
from users.views import *
from rest_framework import routers


router = routers.DefaultRouter()

# router.register('owner', OwnerViewSet)
# router.register('profile', ProfileViewSet)
# router.register('chain', ChainViewSet)
# router.register('school', SchoolViewSet)
# router.register('role', RolePersissionViewSet)
# router.register('access', ProfileRoleViewSet)

urlpatterns = [

    path('',include(router.urls)),
    path('api/owner/',OwnerView.as_view()),
    path('api/owner/<int:id>/',OwnerDetailView.as_view()),
    path('api/chain/',ChainView.as_view()),
    path('api/chain/<int:id>/',ChainDetailView.as_view()),
    path('api/school/',SchoolView.as_view()),
    path('api/school/<int:id>/',SchoolDetailView.as_view()),
    path('api/role_permission/',RolePersissionView.as_view()),
    path('api/role_permission/<int:id>/',RolePersissionDetailView.as_view()),
    path('api/profile_role/',ProfileRoleView.as_view()),
    path('api/profile_role/<int:id>/',ProfileRoleDetailView.as_view()),
    path('api/profile/',ProfileView.as_view()),
    path('api/profile/<int:id>/',ProfileDetailView.as_view()),
]
