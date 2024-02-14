from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


@api_view(['GET'])
def home(request):
    content= fiszka.objects.all()
    serializer= FiszkiSerializer(content, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
def fiszki(request):
    return Response("ZWRACAMxd")

