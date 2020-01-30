from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            # try to log in the user
            # cleaned_data is only accessible after you do form.is_valid()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        
    else:
        # create an instance of the user creation form
        form = UserCreationForm()
        return render(request, 'users/signup.template.html',{
            'form':form
        })
        
@login_required
def profile(request):
    # to access the logged in user
    current_user = request.user
    return render(request, 'users/profile.template.html', {
        'current_user':current_user
    })