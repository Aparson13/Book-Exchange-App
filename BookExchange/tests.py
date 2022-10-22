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
    def add_textbook(name="", author="", condition="", price=0):
        if name!= "" and author!= "" and condition!= "" and price!=-1:
            Textbooks.objects.create(name=name, author=author, condition=condition, price=price)

    def setUp(self):
        self.add_textbook("physics", "john", "good", 20.50)
        self.add_textbook("math", "sue", "poor", 18)
        self.add_textbook("english", "amy", "new", 16)

class GetAllTextbooksTest(BaseViewTest):

    def test_get_all_textbooks(self):
        response = self.client.get(
            reverse("textbooks-all", kwargs={"version": "v1"})    
        )

        expected = Textbooks.objects.all()
        serialized = TextbooksSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)