from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from todolistapp.forms import UserLoginForm, UserRegistrationForm, AddTodoItemForm
from todolistapp.models import TodoListModel

class IndexView(TemplateView):
    template_name = 'index.html'

def log_in(request):
    context = {}
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request=request, password=password, username=username)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('todoapp:profile'))
        else:
            context['errors'] = form.errors     
    else:
        form = UserLoginForm()
        context['form'] = form
    return render(request, 'login.html', context)

def sign_up(request):
    context = {}
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todoapp:login'))
        else:
            context['errors'] = form.error_messages
    form = UserRegistrationForm()
    context['form'] = form
    return render(request, 'signup.html', context)

@login_required(login_url='/login')
def profile(request):
    context = {
        'items': TodoListModel.objects.filter(user=request.user),
        'addtodoform': AddTodoItemForm()
    }
    return render(request, 'profile.html', context)

@login_required(login_url='/login')
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('todoapp:index'))

@login_required(login_url='/login')
def add_todo_item(request):
    if request.method == 'POST':
        text = request.POST['text']
        TodoListModel.objects.create(user=request.user, text=text)
    return HttpResponseRedirect(reverse('todoapp:profile'))

@login_required(login_url='/login')
def delete_todo_item(request, item_id):
    TodoListModel.objects.filter(id=item_id).delete()
    return HttpResponseRedirect(reverse('todoapp:profile'))