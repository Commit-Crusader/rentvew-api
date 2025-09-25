from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


# Serializer for user registration
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name',
            'role', 'phone_number', 'password', 'password2'
        )

    def validate(self, attrs):
        """Ensure password and password2 match"""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                "password": "Password fields didn't match."
            })
        return attrs

    def create(self, validated_data):
        """Create user instance with hashed password"""
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user


# Serializer for user profile (read/update)
class UserProfileSerializer(serializers.ModelSerializer):
    properties_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name',
            'role', 'phone_number', 'date_joined', 'properties_count'
        )
        read_only_fields = ('id', 'username', 'date_joined', 'properties_count')

    def get_properties_count(self, obj):
        """Return count of properties owned by this user"""
        return obj.properties.filter(is_active=True).count()


# Minimal user serializer for nested representations
class UserMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'role')
        read_only_fields = fields
