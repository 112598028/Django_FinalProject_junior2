from django.shortcuts import render, redirect
from . import models
from . import forms

from login.models import Members

from django.contrib.auth import login as dcalogin
from django.contrib import messages

# Create your views here.
def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
        
    members = Members.objects.all()
    return render(request, 'login/index.html', { 'members': members })

def login(request):
    if request.session.get('is_login', None):  # 不允許重複登入
        return redirect('/index/')
    if request.method == "POST":
        login_form = forms.MemberForm(request.POST)
        message = '請確認輸入內容是否正確！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = models.Members.objects.get(name=username)
            except:
                message = '使用者不存在！'
                return render(request, 'login/login.html', locals())
            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = '密碼不正確！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())
    login_form = forms.MemberForm()
    return render(request, 'login/login.html', locals())

def register(request):
    if request.method == "POST":
        register_form = forms.NewMemberForm(data=request.POST)
        print("register_form.is_valid()", register_form.is_valid())
        if register_form.is_valid():
            data = register_form.save()
            user = Members(name=data.name, email=data.email, password=data.password)
            user.save()
            # dcalogin(request, user)
            messages.success(request, "Registration successful." )
            return redirect("/login/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    register_form = forms.NewMemberForm(data=request.POST)
    return render(request=request, template_name="login/register.html", context={"register_form":register_form})

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")