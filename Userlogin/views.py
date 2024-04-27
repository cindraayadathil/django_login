from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from django.contrib.auth import authenticate, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.exceptions import ValidationError

class CustomerSignup(APIView):
    def post(self, request, format=None):
        serializer = CustemerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.instance
            token, created = Token.objects.get_or_create(user=user)
            return Response({"user": serializer.data, "token": token.key,"message":"---SUCCESSFULLY signup--"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AdminSignup(APIView):
    def post(self, request, format=None):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.instance
            token, created = Token.objects.get_or_create(user=user)
            return Response({"user": serializer.data, "token": token.key,"message":"---SUCCESSFULLY signup by admin--"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SalesSignup(APIView):
    def post(self, request, format=None):
        serializer = SalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.instance
            token, created = Token.objects.get_or_create(user=user)
            return Response({"user": serializer.data, "token": token.key,"message":"---SUCCESSFULLY signup by sales--"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class Login(APIView):
#     def post(self, request, format=None):
#         data = request.data
#         user = authenticate(username=data.get('username'), password=data.get('password'))
#         if user:
#             serializer = UserSerializer(user)
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({"user": serializer.data, "token": token.key,"message":"---SUCCESSFULLY LOGIN--"}, status=status.HTTP_200_OK)
#         return Response({"details": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    


class TestView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        user = request.user
        user_data = {
            "username": user.username,
            "email": user.email,
        }
        return Response({"user": user_data, "message": "---Test view---"})


class Logout(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        try:
            request.user.auth_token.delete()
        except AttributeError:
            raise ValidationError("User has no auth_token.")
        logout(request)
        return Response({"message": "---Logout was successful.--"})