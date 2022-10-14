from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta():
        model = Contact
        fields = ("name", "email", "phone_number", "message")

        widgets = {
        "name": forms.TextInput(attrs={"class": "form-name form-control", "placeholder": "Name*", "style": "width: 500px; height:50px; background-color: #343A40; color: #E6E6E6"}),
        "email": forms.EmailInput(attrs={"class": "form-email form-control", "placeholder": "Email*", "style": "width: 500px; height:50px; background-color: #343A40; color: #E6E6E6"}),
        "phone_number": forms.TextInput(attrs={"class": "form-name form-control", "placeholder": "Phone Number*", "style": "width: 500px; height:50px; background-color: #343A40; color: #E6E6E6"}),
        "message": forms.Textarea(attrs={"class": "form-message form-control", "placeholder": "Message*", "style": "width: 500px; background-color: #343A40; color: #E6E6E6"})
        }
