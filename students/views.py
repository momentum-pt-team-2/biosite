from django.shortcuts import render
from .models import User
# Create your views here.

def maraspage(request):
    mara_user = User.objects.get(username='marabrie')
    return render(request, 'students/mara_page.html', {'mara_user': mara_user})


