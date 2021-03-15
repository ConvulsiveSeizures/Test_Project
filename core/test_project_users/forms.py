# Forms
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Models
from .models import TestProjectUser


class TestProjectDateInput(forms.DateInput):
    input_type = 'date'


class UserRegistrationForm(UserCreationForm):
    """
    Форма регистрации нового пользователя, наследуется от стандартной формы регистрации
    """
    # Кастомизация полей "email" и "user_login"
    email = forms.EmailField(label='Почта', required=True)
    user_login = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))

    class Meta:
        model = TestProjectUser
        fields = (
            'user_login',
            'email',
        )

    def save(self, commit=True):
        """
        Переопределение метода "save", перед сохранением полей почты и логина используем валидатор
        """
        user = super(UserRegistrationForm, self).save(commit=False)
        user.user_login = self.cleaned_data['user_login']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class UserProfileEditForm(forms.ModelForm):
    """
    Форма редактирования профиля пользователя
    """
    # Кастомизация указанных полей
    status = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Новый статус'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Введите Ваше имя'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Введите Вашу фамилию'}))
    patronymic = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Введите Ваше отчество'}))
    date_of_birth = forms.CharField(label='', widget=TestProjectDateInput())

    class Meta:
        model = TestProjectUser
        fields = (
            'status',
            'first_name',
            'last_name',
            'patronymic',
            'date_of_birth',
            'description',
        )


class UserAvatarEditForm(forms.ModelForm):
    """
    Модель смены аватарки пользователя
    """

    class Meta:
        model = TestProjectUser
        fields = (
            'photo',
        )
