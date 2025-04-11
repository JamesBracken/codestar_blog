from django.shortcuts import render
from django.views import generic
from .models import About
from .forms import CollaborateForm
from django.contrib import messages

# Create your views here.

def about_me(request):
    """
    Renders the About page
    """

    about = About.objects.all().order_by('updated_on').first()

    if request.method == "POST":
        collaboration_form = CollaborateForm(data=request.POST)
        if collaboration_form.is_valid():
            collaboration_form = collaboration_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )

    collaboration_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
        #  "collaboration_request": collaboration_request,
         "collaboration_form": collaboration_form,
         }
    )



