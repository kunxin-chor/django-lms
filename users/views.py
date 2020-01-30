from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('/home/')
        else:
            return render(request, 'users/signup.template.html', {
                'form':form
            })
            
    else:
        form = UserCreationForm()
        return render(request, 'users/signup.template.html',{
            'form':form
        })
        
@login_required
def profile(request):
    return render(request, 'users/profile.template.html',{
        'current_user':request.user
    })