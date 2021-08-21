from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def sign_up(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully..!')
            fm.save()
    else:
        fm=UserCreationForm()
    return render(request,'signup.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                pwd=fm.cleaned_data['password']
                user=authenticate(username=uname,password=pwd)
                if user is not None:
                    login(request,user)
                    return redirect('/list')
        else:
            fm=AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    else:
        return redirect('/list')

def user_logout(request):
    logout(request)
    return redirect('/')

def user_changepwd(request):
    if request.method == 'POST':
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/login')
    else:
        fm=PasswordChangeForm(user=request.user)
    return render(request,'changepwd.html',{'form':fm})







