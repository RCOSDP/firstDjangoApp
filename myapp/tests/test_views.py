from django.test import TestCase
from myapp.models import Message


class ViewTests(TestCase):

    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        msg = Message.objects.create(text='testtest')
        response = self.client.get('/')
        self.assertContains(response, msg.text)
