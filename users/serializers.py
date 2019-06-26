from rest_framework import serializers
from users.models import *
from django.contrib.auth.models import User

class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        #fields='__all__'
        fields = [
            'type',
            'institute_id',
            'created_by',
        ]

class ChainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chain
        #fields='__all__'
        fields = [
            'id',
            'name',
            'address',
            'phone',
            'email',
            'reg_date',
            'currency',
            'Bank',
            'ifsc',
            'commision',
            'logo',
            'created_by',
        ]

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        #fields='__all__'
        fields = [
            'id',
            'name',
            'address',
            'session_start_month',
            'session_end_month',
            'phone',
            'email',
            'reg_date',
            'currency',
            'Bank',
            'ifsc',
            'commision',
            'logo',
            'front_end',
            'chain',
            'created_by',
        ]

class RolePersissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RolePersission
        #fields='__all__'
        fields = [
            'id',
            'owner',
            'role',
            'module',
            'create',
            'read',
            'update',
            'delete',
            'type',
            'created_by',
        ]

class ProfileRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProfileRole
        #fields='__all__'
        fields = [
            'id',
            'user',
            'role',
            'owner',
            'created_by',
        ]



        


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

