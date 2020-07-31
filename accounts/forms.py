from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']

    #해당 필드 validation
    def clean_password2(self):
        cd = self.cleaned_data # 전체 데이터가 cd안에 딕셔너리타입으로 들어있음
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched')
        return cd['password2']