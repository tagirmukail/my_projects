from datetime import datetime
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .models import Category, Blog, BlogPostForm
from .form import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q

# страница категорий
def BlogList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    blogs = Blog.objects.filter()
    # передача обьекта пользователя, анонимного и авторизованного
    user = request.user.username
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        blogs = blogs.filter(category=category)
    return render(request, 'vision/blogs/list.html', {
        'category': category,
        'categories': categories,
        'form': BlogPostForm(),
        'blogs': blogs,
        'user': user,
    })

# Страница статьи
def BlogDetail(request, id, slug):
    user = request.user.username
    blog = get_object_or_404(Blog, id=id, slug=slug)
    return render(request, 'vision/blogs/detail.html', {
        'blog': blog,
        'user': user,
    })

# register
class RegisterFormView(FormView):
    form_class = UserCreationForm

    # ссылка для перенаправления пользователя в случае успеха
    success_url = '/login/'

    # шаблон для отображения
    template_name = 'vision/registration/register.html'

    def form_valid(self, form):
        # создаем пользователя, если данные коректны
        form.save()
        # вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = 'vision/registration/login.html'

    # в случае успеха перенаправим на главную
    success_url = '/'

    def form_valid(self, form):
        # получаем обьект пользователя на основе введенных в форму данных
        self.user = form.get_user()
        # выполняем аутентификацию ползователя
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

def create_blogpost(request):

    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created = datetime.now()
            post.save()
    return render(request, 'vision/blogs/create_blog.html',
                  {'form': BlogPostForm},
                  RequestContext(request))

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # если форма заполнена корректно сохраняем введенные пользователем данные
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recipients = ['mukailov1991@mail.ru']
            # если пользователь хочет получить копию
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:# защита от уязвимости
                return HttpResponse('invalid header found')
            # переходим на другую страницу если сообщение отправленно
            return render(request, 'vision/outcal/tanks.html')
    else:
        # заполняем форму
        form = ContactForm()
    # отправляем форму на страницу
    return render(request, 'vision/outcal/call.html', {'form': form})

# поиск
class SearchListView(ListView):
    model = Blog
    template_name = 'vision/blogs/result_search.html'

    def get_queryset(self):
        # неотфильтрованый кверисет всех обьектов
        queryset = super(SearchListView, self).get_queryset()
        q = self.request.GET.get('q')
        q_lst = q.split(",")
        if q:
            # фильтруем кверисет по данным из 'q'
            return queryset.filter(Q(name__in=q_lst)|
                                   Q(description__in=q_lst))
        return queryset
