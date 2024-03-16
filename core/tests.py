from . models import Contact
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status



class ContactTestCase(APITestCase):

    """
    Test suite for Contact
    
    setUp overrides the setUp method of the APITestCase class. This method is executed before each test method in the test case.
    It initializes the APIClient instance self.client, sets up sample data for testing, and defines the URL to be used for making requests.
    """
    def setUp(self):
        self.client = APIClient()
        self.data = {
            "name": "Billy Smith",
            "message": "This is a test message",
            "email": "billysmith@test.com"
        }
        self.url = "/contact/"

    def test_create_contact(self):
        '''
        test ContactViewSet create method
        '''
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # It compares what it has got and expected value such as 200 OK status
        self.assertEqual(Contact.objects.count(), 1)  # The count answer expected to be 1...
        self.assertEqual(Contact.objects.get().title, "Billy Smith")

    def test_create_contact_without_name(self):
        '''
        test ContactViewSet create method when name is not in data
        '''
        data = self.data
        data.pop("name")  # The name is popped out from the list
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_when_name_equals_blank(self):
        '''
        test ContactViewSet create method when name is blank
        '''
        data = self.data
        data["name"] = ""  # The name field is blank
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_without_message(self):
        '''
        test ContactViewSet create method when message is not in data
        '''
        data = self.data
        data.pop("message")  # Pop message field
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_when_message_equals_blank(self):
        '''
        test ContactViewSet create method when message is blank
        '''
        data = self.data
        data["message"] = ""  # The message field is blank
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_without_email(self):
        '''
        test ContactViewSet create method when email is not in data
        '''
        data = self.data
        data.pop("email")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_when_email_equals_blank(self):
        '''
        test ContactViewSet create method when email is blank
        '''
        data = self.data
        data["email"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_when_email_equals_non_email(self):
        '''
        test ContactViewSet create method when email is not email
        '''
        data = self.data
        data["email"] = "test"
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)