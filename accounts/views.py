from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import ghasedak_sms


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'شما به وب سایت گروه داروئی آژند وارد شدید.')
                return redirect('home:home_page')
            else:
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
    else:
        form = LoginForm()
    context = {'login_form': form}
    return render(request, 'accounts/user_login.html', context)


@login_required(login_url='accounts:user_login')
def user_logout(request):
    logout(request)
    messages.success(request, 'با موفقیت از حساب کاربری خارج شدید')
    return redirect('home:home_page')


@login_required(login_url='accounts:user_login')
def user_profile(request):
    url = request.META.get('HTTP_REFERER')
    user = request.user
    
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'کلمه عبور شما با موفقیت تغییر یافت')
            update_session_auth_hash(request, request.user)
            return redirect(url)
    else:
        form = ChangePasswordForm(user=request.user)
    
    context = {
        'user': user,
        'form': form
    }
    return render(request, 'accounts/user_profile.html', context)