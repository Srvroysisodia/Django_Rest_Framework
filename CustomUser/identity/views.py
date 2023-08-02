# Importing Required Libraries
from django.core.mail import send_mail
from rest_framework import status
from database.models import User, EmailOTP
from identity import serializers
# from identity.serializers import *
from rest_framework import generics, viewsets, authentication
from database import models
from django.contrib.auth import get_user_model
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from identity.pagination import CustomLimitOffsetPagination
from identity.permission import ActionBasedPermissions, UserBasedPermissions, DeleteBasedPermissions
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from allauth.socialaccount.models import SocialApp, SocialAccount
import requests
from django_filters.rest_framework import DjangoFilterBackend
import json

# vikas yadu creation
from django.core.mail import send_mail
import random


class UserListView(generics.ListCreateAPIView):
    """Handles creating and listing Users."""
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        if data['user_profile'] == 'Student':
            new = {'is_approve': True}
            data.update(new)
        serializer = serializers.CreateuserSerializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Creating a User Retrieve Api
class User_ModelRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = serializers.ListuserSerializer

    def get_queryset(self):
        a = self.request.user
        return User.objects.filter(email=a)


def get_tokens(user):
    tokens = RefreshToken.for_user(user)
    refresh = str(tokens)
    access = str(tokens.access_token)
    data = {
        "refresh": refresh,
        "access": access
    }
    return data

# Creating A Token Generation Api


class UserloginViewset(ObtainAuthToken, APIView):
    serializer_class = serializers.AuthtokenSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token = get_tokens(user=user)
        if user.is_approve:
            return Response({

                'token': token,
                'user': {
                    'user_id': user.pk,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'contact_no': user.contact_no,
                    'user_profile': user.user_profile,
                    'is_staff': user.is_staff,
                    'is_approve': user.is_approve,
                    'created_at': user.created_at
                }})
        else:
            return Response({'Message': 'User is not Approved!'}, status=status.HTTP_401_UNAUTHORIZED)


# Change Password View Code
class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    serializer_class = serializers.ChangePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


############################################## API For Getting JWT Token For Google Logged In User#####################################################
def get_credentials(request):
    app = SocialApp.objects.get(provider='google')
    account = SocialAccount.objects.get(user=request.user)

    user_tokens = account.socialtoken_set.first()
    print(user_tokens)
    payload = {'access_token': user_tokens}  # validate the token
    r = requests.get(
        'https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
    data = json.loads(r.text)
    email = data['email']

    user = User.objects.get(email=data['email'])

    # generate token without username & password
    token = RefreshToken.for_user(user)
    response = {}
    response['email'] = email
    response['access_token'] = str(token.access_token)
    response['refresh_token'] = str(token)
    print(response)
    return HttpResponse(response)


########### Teacher List For admin ################
class TeacherListView(generics.ListCreateAPIView):
    """Handles listing All Teacher"""
    permission_classes = (IsAuthenticated, DeleteBasedPermissions)
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.filter(user_profile='Teacher')
    serializer_class = serializers.UserSerializer

# Update User


class UpdateUserViewset(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, DeleteBasedPermissions)
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = serializers.AdminUpdateUserSerializer


# Update User
class UpdateUserNormalViewset(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, ActionBasedPermissions)
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = serializers.UpdateUserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = queryset.filter(email=self.request.user)
        return queryset


# User Name Filter Dynamic Search Api
class GetUserFullnameAPIView(generics.ListAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    serializer_class = serializers.GetUserfullnameSerializer

    def get_queryset(self):
        data = self.request.data
        name = data['name']
        return User.objects.filter(user_profile='Teacher').filter(first_name=name)


########### Teacher List For admin ################
class Adminis_approveListView(generics.ListAPIView):
    """Handles listing All Users Approval"""
    permission_classes = (IsAuthenticated, DeleteBasedPermissions)
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomLimitOffsetPagination
    queryset = User.objects.all()
    serializer_class = serializers.AdminUserApproveSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_approve', 'on_hold', 'user_profile']

# Update Is approve User


class AdminUpdateApproveViewset(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, DeleteBasedPermissions)
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = serializers.AdminApproveUpdateSerializer


########### forget password ##################################


class UserForgetPasswordView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        if User.objects.filter(email__iexact=email):
            otp = str(random.randint(1000, 9999))
            email_otp = EmailOTP.objects.filter(email=email).first()
            if email_otp:
                email_otp.otp = otp
                email_otp.save()
            else:
                EmailOTP.objects.create(email=email, otp=otp)
            sender = 'soulblissmail@gmail.com'
            message = otp
            subject = 'Forget User Password'
            send_mail(subject, message, sender, [email])
            return Response({'message': 'otp sent'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not a Registered User'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, format=None):
        email = request.data.get('email')
        new_password = request.data.get('newPass')

        try:
            user_data = User.objects.get(email__iexact=email)
            user_data.set_password(new_password)
            user_data.save()
            return Response({'msg': 'Password changed successfully'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'msg': 'Invalid User'}, status=status.HTTP_400_BAD_REQUEST)


class VarifyOTPView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        otp = request.data.get('otp')
        if not email:
            return Response({'error': 'email is required'})
        if not otp:
            return Response({'error': 'otp is required'})
        email_otp = EmailOTP.objects.filter(email=email, otp=otp).first()
        if email_otp:
            return Response({'message': 'valid email and otp'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# email sending
class EmailView(APIView):
    def post(self, request, format=None):
        serializer = serializers.EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            subject = request.data.get('subject')
            email = request.data.get('email')
            sender_name = request.data.get('sender_name')
            msg = request.data.get('message')
            recipient = 'shivamsonideveloper@gmail.com'
            sender = 'soulblissmail@gmail.com'
            message = 'Sender Name {0} \n Email : {1} \n Message : {2}'.format(
                sender_name, email, msg)
            send_mail(subject, message, sender, [recipient])
            return Response({'message': 'Email sent'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
