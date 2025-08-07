from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    def clean_password2(self):
        data = self.cleaned_data
        if data['password2'] and data['password1'] and data['password2'] != data['password1']:
            raise forms.ValidationError('Please Check your password')
        else:
            return data['password2']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'work_position')
        
        
class EditUserForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField
    
    def clean_password(self):
        return self.initial['password']
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'work_position')