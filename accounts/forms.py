from django import forms
from django.contrib.auth import password_validation


class LoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری')
    password = forms.CharField(widget=forms.PasswordInput, label='گذرواژه')
    
    
class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='کلمه عبور فعلی', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='کلمه عبور جدید', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='تایید کلمه عبور جدید', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        
    def clean_old_password(self):
        old_password = self.cleaned_data['old_password']
        if not self.user.check_password(old_password):
            raise forms.ValidationError('کلمه عبور فعلی صحیح نیست')
        return old_password
    
    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data['new_password1']
        new_password2 = cleaned_data['new_password2']
        
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError('کلمه عبورهای جدید با هم مطابقت ندارند')
        
        password_validation.validate_password(new_password2, self.user)
        return cleaned_data
    
    def save(self, commit=True):
        password = self.cleaned_data['new_password2']
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user