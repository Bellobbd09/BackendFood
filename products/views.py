from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import food
from rest_framework import serializers


# Create your views here.
# def function():
#     print("Hello World!")

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = '__all__'

@api_view(['GET'])
def fetchallfood(request):
    allfood = food.objects.all()
    # print(allfood)
    # return Response("Hello World")
    serializer = FoodSerializer(allfood, many=True)
    # return Response(allfood)
    return Response(serializer.data)



@api_view(['POST'])
def createfood(request):
    # return Response("you want to create food")
    return Response("The title is " + request.data['title'])

