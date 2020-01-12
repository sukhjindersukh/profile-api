from rest_framework import serializers

from . import models
class SampleSerializer(serializers.Serializer):
    """Serializes our name field for testing our API view"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """This is a seriazer for Profile model"""
    class Meta:
        model= models.UserProfile
        fields =('id','email','name','password')

        #We dont want user to see the password It should be only Write only
        extra_kwargs ={'password':{
            'write_only':True
        }}

    def create(self, validated_data):
        """Create and return a new user"""

        # We are create a new user object from the data that is coming in post request
        # We are using constructor of UserProfile(parameters) class

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name'],

        )
        # We are using set_password because we want to encrypt it
        user.set_password(validated_data['password'])
        # Save the data into database
        user.save()

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeedItem
        fields =('id','user_profile','status_text','created_on')

        # We dont want user to see the password It should be only Write only
        extra_kwargs = {'user_profile': {
            'read_only': True
        }}

