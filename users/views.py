from django.shortcuts import render
from users.models import *
from rest_framework import viewsets
from users.serializers import *
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


#Create your views here.
@csrf_exempt
def owner_view(request):
    if request.method == 'GET':
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        #1.convert post requst data to json using json perser
        data = JSONParser().parse(request)
        #2.making and instance of Serializer
        data = OwnerSerializer(data=data)
        #3.checking the data is valid or not and if valid then saving it
        if data.is_valid():
            data.save() # data.data contains the newly saved touple
            return JsonResponse(data.data, status=201)
        #4.if data is not valid then taking whats the error
        else:
            return JsonResponse(data.error, status=400)

@csrf_exempt
def owner_view_details(request,id):
    #1.fetching data to check if the data exist or not
    try:
        instance = Owner.objects.get(id=id)
    except Owner.DoesNotExist as e:
        return JsonResponse({'message':'404 Not found'}, status=404)

    if request.method == 'GET':
        serializer = OwnerSerializer(instance)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT': #for updaing all are same as create but need to provide (where,what) => (instance,data=data)
        #1.convert post requst data to json using json perser
        data = JSONParser().parse(request)
        #2.making and instance of Serializer
        data = OwnerSerializer(instance,data=data)
        #3.checking the data is valid or not and if valid then saving it
        if data.is_valid():
            data.save() # data.data contains the newly saved touple
            return JsonResponse(data.data, status=200)
        #4.if data is not valid then taking whats the error
        else:
            return JsonResponse(data.error, status=400)

    elif request.method == 'DELETE': #for deleting we just have to delete
        instance.delete()
        return JsonResponse({'message':'Successfully deleted'}, status=204)

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset =  Profile.objects.all()
    serializer_class = ProfileSerializer

class ChainViewSet(viewsets.ModelViewSet):
    queryset =  Chain.objects.all()
    serializer_class = ChainSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset =  School.objects.all()
    serializer_class = SchoolSerializer

class RolePersissionViewSet(viewsets.ModelViewSet):
    queryset =  RolePersission.objects.all()
    serializer_class = RolePersissionSerializer

class ProfileRoleViewSet(viewsets.ModelViewSet):
    queryset =  ProfileRole.objects.all()
    serializer_class = ProfileRoleSerializer