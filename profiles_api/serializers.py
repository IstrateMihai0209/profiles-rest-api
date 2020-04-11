from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    #Serialize a name field for testing our APIView
    name = serializers.CharField(max_length=28)

########################################################################################################
########################################################################################################

class UserProfileSerializer(serializers.ModelSerializer):
    #Serializes a user profile object

    class Meta:
        #What field do I want to add to a model and specify which model
        model = models.UserProfile
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True, #Make the password only for POST, not for GET
                'style': {'input_style': 'password'} #Make the password show only dots
            }
        }

    def create(self, validated_data):
        #Create and return user
        # We are overriding the default Django create function to make the
        # password a hash and not just plain text
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        #Handle updating user account
        if 'password' in validated_data:
            password = validated_data.pop('password')#pop means assign the value and remove from dictionary
            instance.set_password(password) #saves the password as a hash

        return super().update(instance, validated_data)
