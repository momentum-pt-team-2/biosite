from django.shortcuts import render, get_object_or_404
from .models import User

def rebecca(request):
    rebecca = get_object_or_404(User, pk=1)
    return render(request, 'students/rebecca.html', {"rebecca":rebecca})
