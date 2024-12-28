from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name = 'Article'

class NewsUpdateView(UpdateView):
    model = Artiles
    template_name = 'news/create.html'
    form_class = ArtilesForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise Http404("Вы не можете изменить эту статью, так как вы не её автор.")
        return obj

class NewsDeleteView(DeleteView):
    model = Artiles
    template_name = 'news/delete.html'
    success_url = '/news'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise Http404("Вы не можете удалить эту статью, так как вы не её автор.")
        return obj

@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
        else:
            error = 'Форма заполнена неправильно'

    form = ArtilesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


