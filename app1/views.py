from django.shortcuts import render
from rest_framework.response import Response
# from .models import *
# from .serializers import *
# from rest_framework.permissions import IsAuthenticated,AllowAny
# from django.contrib.auth import authenticate
# from django.core.paginator import Paginator, EmptyPage
# from rest_framework_simplejwt.authentication import JWTAuthenticationj
# from django.db.models import Q,Count
# from django.contrib.auth.models import AnonymousUser
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework import generics, status
# from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import *
from .models import *
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth import get_user_model
# User = get_user_model()
# from django.contrib.auth.hashers import make_password
# from django.shortcuts import get_object_or_404

"""Internal Imports"""
class HelloWorld(generics.ListAPIView):
    def list(self,request,**kwargs):
        data = "Hellow World"
        # print("data",data)
        return Response(data, status=200)
    
# class ProfileCreateApi(generics.CreateAPIView):
#     serializer_class = ProfileSerializer
#     def create(self,request,**kwargs):
#         data = request.data
#         serializer = self.get_serializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response("success", status=200)
#         else:
#             return Response(serializer.errors, status=400)
class ProfileCreateApi(generics.CreateAPIView):
    serializer_class = ProfileSerializer
        
# class ProfileUpdateApi(generics.UpdateAPIView):
#     serializer_class = ProfileSerializer
#     def update(self,request,**kwargs):
#         data = request.data
#         id = kwargs.get("pk")
#         try:
#             instance = UserProfile.objects.get(id=id)
#         except UserProfile.DoesNotExist:
#             return Response({}, status=404)
#         serializer = self.get_serializer(instance,data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response("success", status=200)
#         else:
#             return Response(serializer.errors, status=400)
class ProfileUpdateApi(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

class ProfileApi(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
        
# class AllProfileViewApi(generics.ListAPIView):
#     serializer_class = ProfileSerializer
#     def list(self,request,**kwargs):
#         data = UserProfile.objects.all()
#         serializer = self.get_serializer(instance=data,many=True)
#         if serializer:
#             return Response(serializer.data, status=200)
#         else:
#             return Response({}, status=400)
    
class AllProfileViewApi(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
        
# class ProfileViewApi(generics.ListAPIView):
#     serializer_class = ProfileSerializer
#     def list(self,request,**kwargs):
#         id = kwargs.get("pk")
#         try:
#             data = UserProfile.objects.get(id=id)
#         except UserProfile.DoesNotExist:
#             return Response({}, status=404)
#         serializer = self.get_serializer(instance=data)
#         if serializer:
#             return Response(serializer.data, status=200)
#         else:
#             return Response({}, status=404)
    
class ProfileViewApi(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
        
# class ProfileDeleteApi(generics.DestroyAPIView):
#     def destroy(self,request,**kwargs):
#         id = kwargs.get("pk")
#         try:
#             data = UserProfile.objects.get(id=id)
#         except UserProfile.DoesNotExist:
#             return Response({}, status=404)
#         data.delete()
#         return Response("Success", status=200)
    
class ProfileDeleteApi(generics.DestroyAPIView):
    queryset = UserProfile.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response("Success", status=status.HTTP_200_OK)

# Create your views here.
