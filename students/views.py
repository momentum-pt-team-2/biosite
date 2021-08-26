from django.shortcuts import render
from .models import User

def daniel_page(request):
    daniel = User.objects.get(username='danielshearin')
    return render(request, 'daniel_page.html', {'daniel': daniel})
