from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password


# Serializer for reading user info
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'role', 'phone_number', 'bio', 'profile_picture']

# Serializer for creating/registering users
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
            write_only=True, 
            required=True, 
            validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)  # confirm password

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return attrs

    def create(self, validated_data):
        # Remove password2 before creating user
        validated_data.pop('password2')

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role=validated_data.get('role', CustomUser.Role.TOURIST),
            password=validated_data['password']
        )
        return user
