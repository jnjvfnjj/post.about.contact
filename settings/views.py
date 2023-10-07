from django.shortcuts import render
from settings.models import Settings

# Create your views here.
def index(request):
    settings = Settings.objects.latest("id")
    return render(request, "index-2.html", locals())

def contact(request):
    settings = Settings.objects.latest("id")
    return render(request, "contact.html", locals())

def about(request):
    settings = Settings.objects.latest("id")
    return render(request, "about.html", locals())
