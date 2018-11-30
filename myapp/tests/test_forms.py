from django.test import TestCase
from myapp.models import Message
from myapp.forms import MessageForm


class MessageFormTests(TestCase):

    def test_form_validateion(self):
        msg = Message.objects.create(text='hello')
        form = MessageForm({'text': msg.text}, instance=msg)
        self.assertTrue(form.is_valid())

        msg = Message.objects.create()
        form = MessageForm({'text': ''}, instance=msg)
        self.assertFalse(form.is_valid())
