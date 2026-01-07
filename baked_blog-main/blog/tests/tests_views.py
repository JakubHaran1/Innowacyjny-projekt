from django.urls import reverse
from django.test import TestCase, Client
from blog.views import index
from blog.models import PostModel, CustomUserModel,TagModel
class TestView(TestCase):

   def set_up(self):
      self.client = Client()

      self.authorObj = CustomUserModel.objects.create(username="test", email="test@test.com",password="test123")

      self.tagObj = TagModel.objects.create(tag="test-tag")

      self.postObj = PostModel.objects.create(title="test",author=self.authorObj,slug="test",date="2026-01-07",excerpt="test excerpt test excerpt test excerpt",ingredients="Test ingredient",prepare="test prepare",image="../../../spaghetti.webp",tags=[self.tagObj])

      self.post_detail_Url = reverse("post", args=["test"])
       
   def test_main_view_GET(self):
      response =   self.client.get(reverse("main_page"))
      # post1= PostModel.objects.create()
      self.assertEqual(response.status_code,200)
      self.assertTemplateUsed("blog/index.html")
   

  
   
   




      



