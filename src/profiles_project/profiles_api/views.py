from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status

from . import serializers
# Create your views here.
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