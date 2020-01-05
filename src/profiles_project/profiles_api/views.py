from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response

# Create your views here.
class SampleAPIView(APIView):
    """-This is just an example- """

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
