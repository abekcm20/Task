from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewUserForm
from .models import tasks
from django.core.paginator import Paginator
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('users/login')
    else:
        form = NewUserForm()
    return render(request, 'users/register.html', {'form' : form})

def index(request):
    task_t = tasks.objects.all()
    paginator = Paginator(task_t, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'users/base.html', {'task':page_obj})
