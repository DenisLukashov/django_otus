from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView
from .models import Author
from .forms import AuthorForm


app_name = 'authors'


class IndexView(ListView):

    template_name = 'authors/index.html'

    model = Author
    context_object_name = 'authors'


class CreateAutherView(TemplateView):
    template_name = 'authors/create.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthorForm()
        return context
        
    def post(self, request):
        form = AuthorForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})
        new_author = form.save(commit=False)
        new_author.level = 'J'
        new_author.save()
        return redirect(reverse('index'))
        

