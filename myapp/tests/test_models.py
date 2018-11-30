from django.test import TestCase
from myapp.models import Message


class MessageModelTests(TestCase):

    def test_is_empty(self):
        messages = Message.objects.all()
        self.assertEqual(messages.count(), 0)

    def test_is_not_empty(self):
        msg = Message(text='hello world')
        msg.save()
        messages = Message.objects.all()
        self.assertEqual(messages.count(), 1)

    def test_save_and_retrieve(self):
        text = "hello world"
        msg = Message()
        msg.text = text
        msg.save()

        messages = Message.objects.all()
        msg = messages[0]
        self.assertEqual(msg.text,text)
