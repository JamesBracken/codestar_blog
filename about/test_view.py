from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm

class TestAboutViews(TestCase):

    def setUp(self):
        self.about_content = About(
            title="About title",
            content="This is some fantastic fucking content innit mate. GEE WHIZ",
        )
        self.about_content.save()

    def test_render_about_page(self):
        # response = self.client.get(reverse("about"))
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"GEE WHIZ", response.content)
        self.assertIsInstance(
            response.context["collaboration_form"], CollaborateForm
        )



# The about page loads successfully.
# The about page contains text from the mock About instance.
# The collaborate_form context for this view is an instance of CollaborateForm.
# title
# updated_on MIGHT NOT HAVE TO
# content
# profile_image MIGHT NOT HAVE TO
