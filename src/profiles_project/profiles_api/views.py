from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from  rest_framework import viewsets


from rest_framework.views import Response
from rest_framework import status

from . import serializers
from . import models

# Create your views here.
#There are multiple views
#1. APIView

#2. ViewSet
#   Use model operations for functions
#    - List, Create, Retrieve, Update, Partial update, Destroy/Delete
#   Take care lot of typically logic for us
#       - Perfect for standard database operations
#       - Fastest way to build database interface
# When to use these
#   - Perform Simple CRUD operations
#   - Want to build simple and quick API
#   - We need little or no customizations on logic

class SampleAPIView(APIView):
    """-This is just an example- """

    #Tell the django what serialize you want to use for this api
    serializer_class = serializers.SampleSerializer

    def get(self,request,format=None):
        """This is a get call and return a list of Strings"""
        features_of_API_View=[
            'Use HTTP method as function - get, put, post, delete, patch',
            'It is similar to traditional django API view',
            'Give you most control of your logic',
            'It mapped manually to URLs'
            'Best fit when you have complex logic',
            'When you call 3rd party apis',
            'When you required to access multiple database tables',
            'When you need to handle local files'
        ]

        #Response always return a dictonary object, which is then converted to JSON
        return Response({'message':'Sample API call','data':features_of_API_View})

    def post(self,request):
        serializer = serializers.SampleSerializer(data=request.data)

        if serializer.is_valid():
            name= serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        '''Update the data'''
        message = 'Method {0} is called'.format('PUT')
        return Response({'message': message})

    def patch(self,request,pk=None):
        '''Update the partial data'''
        message = 'Method {0} is called'.format('PATCH')
        return Response({'message': message})


    def delete(self,request,pk=None):
        '''Delete the object'''
        message = 'Method {0} is called'.format('DELETE')
        return Response({'message': message})


# TO USE SampleViewSet we need following import in our urls file
#from rest_framework.routers import DefaultRouter
class SampleViewSet(viewsets.ViewSet):
    """Example of view set"""
    serializer_class = serializers.SampleSerializer

    def list(self,request):
        """This will return a list of objects"""
        message =[
            'Use actions (list, create, retrieve, delete, update, partial_update)',
            'Automatically maps to URLs using Rousters ',
            'Provide more functionality with less code'
        ]

        return Response({'message':message})

    def create(self, request):
        """Create method of a viewSet used as a post method"""
        serializer = serializers.SampleSerializer(data=request.data)

        if serializer.is_valid():
            name= serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """This is GET method"""
        message = 'Method {0} is called'.format('GET')
        return Response({'message': message})

    def update(self, request, pk=None):
        """This is PUT method"""
        message = 'Method {0} is called'.format('PUT')
        return Response({'message': message})
    #
    def partial_update(self, request, pk=None):
         """This is PATCH method"""
         message = 'Method {0} is called'.format('PATCH')
         return Response({'message': message})

    def delete(self,request, pk=None):
         """This is DELETE method"""
         message = 'Method {0} is called'.format('DELETE')
         return Response({'message': message})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle create, reading and update UserProfiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

