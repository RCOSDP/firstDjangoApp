from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Message
from .forms import MessageForm


class ListAndCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = "form.html"
    success_url = reverse_lazy('list_and_create')

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Message.objects.order_by('id')
        return super(ListAndCreateView, self).get_context_data(**kwargs)
