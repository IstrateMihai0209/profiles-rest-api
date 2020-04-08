from rest_framework.views import APIView
from rest_framework.response import Response

class ApiView(APIView):
    #Test API View

    def get(self, request, format=None): #it is good practice to type in format=None
        #Returns a list of APIView features
        the_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello World!', 'the_apiview': the_apiview})