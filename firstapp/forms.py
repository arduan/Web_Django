from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Имя клиента')
    age = forms.IntegerField(label='Возраст клиента')
    basket =forms.BooleanField(label='Положить товар в корзину', required=False)
    vyb = forms.NullBooleanField(label='Вы поедите в Сочи этим летом.')
    email = forms.EmailField.validate(label='Электронный адрес')