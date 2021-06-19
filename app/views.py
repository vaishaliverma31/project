from django.shortcuts import render
from .models import studentdetail
from .serializers import *
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class studentapi(ListCreateAPIView):
    queryset = studentdetail.objects.all()
    serializer_class = studentdetailserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]