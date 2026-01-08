from django.shortcuts import render
from app.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login,logout
import logging
from .serializers import *
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
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



class Demoapi(APIView):
    def get(self, request):
        data = {
            "message": "Hello, this is a demo API response!"
        }
        return Response(data)

# create api view for usercustome model

class UsercustomeAPIView(APIView):
    permission_classes = [AllowAny]
    
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
    
    

class CurrentUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UsercustomeSerializer(request.user)
        return Response(serializer.data)
    
    
class Userlogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {"error": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,
                }
            },
            status=status.HTTP_200_OK
        )
    
class userlogout(APIView):
    def post(self, request):
        try:
            logout(request)
            return Response({'message': 'Logged out successfully'})
        except Exception as e:
            logging.error(f"Logout failed: {e}")
            return Response({'error': 'Logout failed'}, status=500)
        
        
class Userprofile(APIView):
    
    def get(self, request):
        profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
       


