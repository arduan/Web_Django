from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Имя клиента')
    last_name = forms.CharField(label='Фамилия клиента')
    age = forms.IntegerField(label='Возраст клиента')