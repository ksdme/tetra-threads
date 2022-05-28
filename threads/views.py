from django.views.generic import TemplateView
from django.views.generic import DetailView
from threads.models import Thread


class IndexView(TemplateView):
  template_name: str = 'index.html'


class ThreadDetailView(DetailView):
  template_name: str = 'detail.html'

  def get_object(self, *args):
    return Thread.objects.first()
