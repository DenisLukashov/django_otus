# from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Author
from .forms import AuthorForm


app_name = 'authors'


class IndexView(ListView):

    template_name = 'authors/index.html'

    model = Author
    context_object_name = 'authors'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['authors'] = Author.objects.all()
    #     return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(email__endswith='otus.ru')
    #     return queryset


class CreateAutherView(TemplateView):
    template_name = 'authors/create.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthorForm()
        return context

