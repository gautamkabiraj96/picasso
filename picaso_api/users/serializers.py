from django.contrib.auth import get_user_model
from rest_framework import serializers

# Get the custom User model using Django's dynamic model retrieval
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model to be serialized
        model = User
        # Fields of the model to be included in the serialization/deserialization
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        # Set the password field to write-only for security reasons
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user instance using the validated data while handling the password correctly
        user = User.objects.create_user(**validated_data)
        return user
