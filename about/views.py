from django.shortcuts import render
from django.views import generic
from .models import About
from .forms import CollaborateForm

# Create your views here.

def about_me(request):
    """
    Renders the About page
    """

    about = About.objects.all().order_by('updated_on').first()
    collaboration_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
        #  "collaboration_request": collaboration_request,
         "collaboration_form": collaboration_form,
         }
    )



