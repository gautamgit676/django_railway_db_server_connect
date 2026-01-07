from django.shortcuts import render
from app.models import Usercustome
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login,logout
import logging
from .serializers import *
# Create your views here.


def home(request):
    user = Usercustome.objects.all()
    return render(request, 'home.html', {'user': user})


def creaetusers(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        role = request.POST.get('role')
        password = request.POST.get('password')

        Usercustome.objects.create(
            username=username,
            email=email,
            phone_number=phone_number,
            role=role,
            password=password
        )
    return render(request, 'create_user.html')



# create api view for usercustome model
class UsercustomeAPIView(APIView):
    def get(self, request):
        users = Usercustome.objects.all()
        serializer = UsercustomeSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsercustomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
class Userlogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = UsercustomeSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=400)
            
    
class userlogout(APIView):
    def post(self, request):
        try:
            logout(request)
            return Response({'message': 'Logged out successfully'})
        except Exception as e:
            logging.error(f"Logout failed: {e}")
            return Response({'error': 'Logout failed'}, status=500)
        
        
class UserProfile(APIView):
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
       


