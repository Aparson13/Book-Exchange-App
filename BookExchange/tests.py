from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Textbooks
from .serializers import TextbooksSerializer

class FirstTest(TestCase):
    def testFour(self):
        four = 2+2
        tFour = (four == 4)
        self.assertIs(tFour, True)

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def add_textbook(name="", author="", condition=""):
        if name!= "" and author!= "" and condition!= "":
            Textbooks.objects.create(name=name, author=author, condition=condition)

    def setUp(self):
        self.add_textbook("physics", "john", "good")
        self.add_textbook("math", "sue", "poor")
        self.add_textbook("english", "amy", "new")

class GetAllTextbooksTest(BaseViewTest):

    def test_get_all_textbooks(self):
        response = self.client.get(
            reverse("textbooks-all", kwargs={"version": "v1"})    
        )

        expected = Textbooks.objects.all()
        serialized = TextbooksSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)