from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
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

########################################################################################################
########################################################################################################

class Viewset(viewsets.ViewSet):
    #Test API Viewset

    def list(self, request):
        #Return a message and throw in a list
        the_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'This is written in the viewset', 'the_viewset': the_viewset})

    def create(self, request):
        #Create a new message
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}' #just like writing 'Hello ' + name
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        #Handle getting an object by its ID
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        #Handle updating an object
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        #Handle updating part of an object
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        #Handle removing an object
        return Response({'http_method': 'DELETE'})




