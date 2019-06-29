from rest_framework import serializers
from users.models import *
from django.contrib.auth.models import User

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields='__all__'
  

class ChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chain
        fields='__all__'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields='__all__'


class RolePersissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePersission
        fields='__all__'


class ProfileRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileRole
        fields='__all__'
             


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'phone',
            'address',
            'status',
        ]
        #write_only_fields = ('password',)
        #read_only_fields = ('id',)

