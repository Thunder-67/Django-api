from django.shortcuts import render
from .models import categories,meals,search
from .serializers import categoriesSerializer,mealsSerializer,searchSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
class categoryModelViewSet(viewsets.ModelViewSet):
    queryset=categories.objects.all()
    serializer_class=categoriesSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

class mealsModelViewSet(viewsets.ModelViewSet):
    queryset=meals.objects.all()
    serializer_class=mealsSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

class searchModelViewSet(viewsets.ModelViewSet):
    queryset=search.objects.all()
    serializer_class=searchSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
