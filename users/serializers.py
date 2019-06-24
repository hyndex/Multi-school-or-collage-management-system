from rest_framework import serializers
from users.models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            #'dob',
            'status',
        ]
        #write_only_fields = ('password',)
        #read_only_fields = ('id',)

    # def create(self, validated_data):
    #     user = User.objects.create(
    #         username=validated_data['phone'],
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name']
    #     )

    #     user.set_password(validated_data['password'])
    #     user.save()

    
    ######## saving a data ################
    # p = ProfileSerializer(data = {'phone':'9876543210','email':'dikibhuyan@gmail.com'})
    # p.is_valid()
    # p.save()

    ########## Fetching data ###############
    # u = Profile.objects.all()
    #or user = User.objects.get(id = 1)
    # print(u[i])

    ########## Updateing data ###############
    # let there is another field in Profile i.e 'created_by' which is a forign key of Users
    # p = Profile.objects.all()
    # u = Users.objects.get(id = 1)
    #####################################################################
    # updating or serializing one at a time
    # p1 = ProfileSerializer(p[0] ,'created_by' = u.id, partial = True)
    # p1.save()
    # print(str(p1.data))
    #####################################################################
    # updating or serializing all at a time
    # p = ProfileSerializer(p , many = True,'created_by' = u.id, partial = True)
    # p.save()
    #####################################################################


        