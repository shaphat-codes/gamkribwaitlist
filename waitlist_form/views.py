from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from . models import *
# Create your views here.


@api_view(['POST'])
def Waitlist(request):
        if request.method == "POST":

            serializer = WaitlistSerializer(data=request.data)
            
        if serializer.is_valid():
                
            serializer.save()

        return Response(serializer.data)