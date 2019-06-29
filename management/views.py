from django.shortcuts import render
from users.models import *
from rest_framework import viewsets
from management.serializers import *
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

#Create your views here.
@csrf_exempt
def news_view(request):
    if request.method == 'GET':
        instance = News.objects.all()
        serializer = NewsSerializer(instance, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data = NewsSerializer(data=data)
        if data.is_valid():
            data.save() 
            return JsonResponse(data.data, status=201)
        else:
            return JsonResponse(data.error, status=400)

@csrf_exempt
def news_view_details(request,id):
    try:
        instance = News.objects.get(id=id)
    except News.DoesNotExist as e:
        return JsonResponse({'message':'404 Not found'}, status=404)

    if request.method == 'GET':
        serializer = NewsSerializer(instance)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT': 
        data = JSONParser().parse(request)
        data = NewsSerializer(instance,data=data)
        if data.is_valid():
            data.save() 
            return JsonResponse(data.data, status=200)
        else:
            return JsonResponse(data.error, status=400)

    elif request.method == 'DELETE': 
        instance.delete()
        return JsonResponse({'message':'Successfully deleted'}, status=204)

    ####################################################################################################