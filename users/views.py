from users.models import *
from users.serializers import *
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class OwnerView(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class OwnerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    lookup_field='id'

class ChainView(generics.ListCreateAPIView):
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer
    
class ChainDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer
    lookup_field='id'

class SchoolView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    
class SchoolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field='id'

class RolePersissionView(generics.ListCreateAPIView):
    queryset = RolePersission.objects.all()
    serializer_class = RolePersissionSerializer
    
class RolePersissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RolePersission.objects.all()
    serializer_class = RolePersissionSerializer
    lookup_field='id'

class ProfileRoleView(generics.ListCreateAPIView):
    queryset = ProfileRole.objects.all()
    serializer_class = ProfileRoleSerializer
    
class ProfileRoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfileRole.objects.all()
    serializer_class = ProfileRoleSerializer
    lookup_field='id'

class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field='id'

