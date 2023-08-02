# Importing Required Libraries
from database.models import User, EnquiryEmail
from rest_framework import serializers
from django.core import exceptions
from django.contrib.auth import get_user_model, authenticate, password_validation
from django.core.validators import validate_email
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

# Overriding a default User List Serializer


class ListuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id', 'email', 'first_name', 'last_name', 'user_profile', 'is_staff', 'created_at',

        ]
        read_only_fields = ['id',]


# Overriding a default User Create Serializer
class CreateuserSerializer(serializers.ModelSerializer):
    '''Serializer for creating a new user'''
    password = serializers.CharField(
        write_only=True, min_length=8, required=True)
    confirm_password = serializers.CharField(
        write_only=True, min_length=8, required=True)
    tokens = serializers.SerializerMethodField()

    def validate(self, attrs):
        try:
            if User.objects.filter(email=attrs['email']).exists():
                raise serializers.ValidationError('This Email is Already Used')

            if attrs['password'] != attrs['confirm_password']:
                raise serializers.ValidationError('This Password Not Match')

            else:
                password_validation.validate_password(attrs['password'])
                validate_email(attrs['email'])

        except exceptions.ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return attrs

    def get_tokens(self, user):
        tokens = RefreshToken.for_user(user)
        refresh = str(tokens)
        access = str(tokens.access_token)
        data = {
            "refresh": refresh,
            "access": access
        }
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        return User.objects.create_user(**validated_data)

    class Meta:
        model = get_user_model()
        fields = [
            'id', 'email', 'first_name', 'last_name', 'contact_no', 'password', 'confirm_password', 'user_profile', 'subject', 'is_approve', 'is_staff', 'created_at', 'tokens',

        ]
        read_only_fields = ['id',]
        extra_kwargs = {

            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'user_profile': {'required': True},
        }


class AdminUpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [

            'id', 'first_name', 'last_name', 'user_profile', 'is_approve', 'is_staff', 'created_at',
        ]
        read_only_fields = ['id',]


class AdminUserApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [

            'id', 'email', 'first_name', 'last_name', 'contact_no', 'subject', 'user_profile', 'is_approve','is_active', 'created_at',
        ]
        read_only_fields = ['id',]


class AdminApproveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [

            'is_approve', 
        ]
        read_only_fields = ['id',]


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [

            'id', 'first_name', 'last_name', 'contact_no'
        ]
        read_only_fields = ['id', 'user_type']


# Creating a Authentication by token Serializer
class AuthtokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={
            'input_type': 'password'

        }
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            email=email,
            password=password,


        )
        if not user:
            msg = 'unable to determine'
            raise serializers.ValidationError(msg, code='authentication')
        attrs['user'] = user
        return attrs


################################### Passsword Reset And Forget Serializers #############################################


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


# Change Password
class ChangePasswordSerializer(serializers.Serializer):
    model = User
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


####################### Created a Api for fetching Created by and Updated by ########################################
class GetUserfullnameSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    class Meta:
        model = User
        fields = ['full_name']


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnquiryEmail
        fields = '__all__'
