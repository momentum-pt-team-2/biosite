from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import ContactForm
from .models import User, Contact
# Create your views here.

def maraspage(request):
    mara_user = User.objects.get(username='marabrie')
    return render(request, 'students/mara_page.html', {'mara_user': mara_user})



def daniel_page(request):
    daniel = User.objects.get(username='danielshearin')
    return render(request, 'daniel_page.html', {'daniel': daniel})


def work(request):
    return render(request, 'work.html', {'work': work})

def bio(request):
    return render(request, 'bio.html', {'bio': bio})

# class ContactCreate(CreateView):
#     model = Contact
#     fields = ["first_name", "last_name", "message"]
#     success_url = reverse_lazy("thanks")
    
# def thanks(request):
#     return HttpResponse("Thank you! Will get in touch soon.")

def contact(request):
    name=''
    email=''
    message=''
    
    form=ContactForm(request.POST or None)
    if form.is_valid():
        name= form.cleaned_data.get("name")
        email= form.cleaned_data.get("email")
        message= form.cleaned_data.get("message")

        # if request.user.is_authenticated():
        #     subject= str(request.user) + "'s Message"
        # else:
        #     subject= "A Visitor's Message"
        
        subject= "A Visitor's Message"
            
        message= name + email + message
        send_mail(subject, message, email, ['danielshearin@gmail.com'])


        context= {'form': form}

        return render(request, 'contact.html', context)

    else:
        context= {'form': form}
        return render(request, 'contact.html', context)
