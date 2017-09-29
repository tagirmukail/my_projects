from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def logout_view(request):
    """Выход пользователя, завершение сеанса."""
    logout(request)
    return HttpResponseRedirect(reverse('journal:index'))

def register(request):
    """Регистрациия нового пользователя."""
    if request.method != 'POST':
        # Форма регистрации, если данные не отправленны.
        form = UserCreationForm()
    else:
        # Обработка заполненой формы.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу.
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            return HttpResponseRedirect(reverse('journal:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)