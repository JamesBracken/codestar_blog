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
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"GEE WHIZ", response.content)
        self.assertIsInstance(
            response.context["collaboration_form"], CollaborateForm
        )

    def test_successful_collaboration_request(self):
        self.client.login(username="myUsername", 
                          password="myPassword")
        post_data = {
            'name': "Johnny",
            'email': "Johhny@junkmail.com",
            'message': "Here is some spam for you mate, fyi not the kind you wanted",
            # 'read': False,
        }
        response = self.client.post(reverse(
            'about'), post_data )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Collaboration request received! I endeavour to respond within 2 working days.", response.content)

    # The assertions 
    # should check the about page request succeeded and 
    # that a success message of "Collaboration request received! I endeavour to respond within 2 working days." is included in the response's content.
    # name = models.CharField(max_length=200)
    # email = models.EmailField()
    # message = models.TextField()
    # read = models.BooleanField(default=False)
