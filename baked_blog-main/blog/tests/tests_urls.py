from django.test import SimpleTestCase
from django.urls import resolve,reverse
from blog.views import index,AllPostView,PostView,contact,RegistrationView

class TestUrls(SimpleTestCase):
    def test_urls_main_page(self):
        url = reverse("main_page")
        self.assertEqual(resolve(url).func,index)

    def test_urls_all_posts(self):
        url = reverse("all_posts")
        self.assertEqual(resolve(url).func.view_class,AllPostView)

    def test_urls_posts(self):
        url = reverse("post",args=["slug"])
        self.assertEqual(resolve(url).func.view_class,PostView)
    
    def test_urls_contact(self):
        url = reverse("contact")
        self.assertEqual(resolve(url).func,contact)

    def test_urls_registration(self):
        url = reverse("registration")
        self.assertEqual(resolve(url).func.view_class,RegistrationView)
    



    
        