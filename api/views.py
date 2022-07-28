from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 



# Create your views here
#class Test(APIView):
#    def get(self,request):
#        pass
#        return Response(data = 'Hello World',status= status.HTTP_200_OK)


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

    