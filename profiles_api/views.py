from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

class ApiView(APIView):
    #Test API View
    serializer_class = serializers.HelloSerializer  # import the HelloSerializers class

    def get(self, request, format=None): #it is good practice to type in format=None
        #Returns a list of APIView features
        the_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello World!', 'the_apiview': the_apiview})

    def post(self, request):
        #Create a Hello message with our serializer name
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello' + ' ' + name
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #if the input
            #is invalid, then the serializer will send the 400 error with details

    #We put the pk=None because usually this functions are used on a specific object
    def put(self, request, pk=None):
        #Handle updating an object
        return Response({'method:' 'PUT'})

    def patch(self, request, pk=None):
        #Handle a partial update of an object
        return Response({'method:' 'PATCH'})

    def delete(self, request, pk=None):
        #Delete an object
        return Response({'method:' 'DELETE'})