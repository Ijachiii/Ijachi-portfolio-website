from django.shortcuts import render, redirect
from basicapp.forms import ContactForm
from basicapp.models import Contact
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    model = Contact
    if request.method == "POST":
        form = ContactForm(request.POST)
        form.save()
        # name = form["name"].data
        #
        # subject = f"Message from {name}"
        # message = form["message"].data
        # email_from = settings.EMAIL_HOST_USER
        # recipient = ["davidaudu1010@gmail.com"]
        # send_mail(subject, message, email_from, recipient)
        return redirect("home")
    else:
        form = ContactForm()

    return render(request, "index.html", {"form": form})
