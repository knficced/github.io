from django.shortcuts import render, redirect

from .forms import ArticleForm


def new_home(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'
    form = ArticleForm()
    data = {'form': form, 'error': error}
    return render(request, 'new/new_home.html', data)
