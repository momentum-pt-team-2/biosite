from django import forms
from django.db.models.fields import CharField
from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Tell me what you think'}))
    
# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = ["first_name", "last_name", "message"]
#         widgets = {
#             "message": Textarea(
#                 attrs={
#                     "placeholder": "Holler at me"
#                 }
#             )
#         }
    