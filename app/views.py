from django.shortcuts import render
from app.models import Usercustome
# Create your views here.


def home(request):
    user = Usercustome.objects.all()
    return render(request, 'home.html', {'user': user})


