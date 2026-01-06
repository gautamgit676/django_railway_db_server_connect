from django.shortcuts import render
from app.models import Usercustome
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