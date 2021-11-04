from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Имя клиента')
    age = forms.IntegerField(label='Возраст клиента')
    basket =forms.BooleanField(label='Положить товар в корзину', required=False)
    vyb = forms.NullBooleanField(label='Вы поедите в Сочи этим летом.')
    email = forms.EmailField(label='Электронный адрес', help_text='Обязательный символ @')
    ip_address = forms.GenericIPAddressField(label='IP адрес', help_text='Примерный формат 192.0.2.0')
    file_path = forms.FilePathField(label='Выберите файл', path='C:', allow_files='True', allow_folders='True')
    file = forms.FileField(label='Файл')
    img_file = forms.ImageField(label='Изображение')
