from django.shortcuts import render
from .models import User

# Create your views here.

def clarissa_page(request):
    clarissa_user = User.objects.get(username='crodri')
    return render(request, 'clarissa_page.html', {'clarissa_user': clarissa_user})

