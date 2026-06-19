from django import forms
from .models import Intro


class IntroForm(forms.ModelForm):
    class Meta:
        model = Intro
        fields = ['name', 'birthday', 'hobby']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '名前を入力してください。'
            }),
            'birthday': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'hobby': forms.Textarea(attrs={
                'rows': 10,
                'class': 'form-control',
                'placeholder': '趣味や特技などを自由に記入してください。'
            }),
        }