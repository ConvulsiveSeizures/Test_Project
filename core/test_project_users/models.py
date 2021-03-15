# Models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Routing
from django.urls import reverse


class TestProjectUserManager(BaseUserManager):
    """
    Менеджер создания кастомной модели пользователя
    """
    def create_user(self, email, user_login=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Поле "Почта" должно быть заполненно корректно')
        if not password:
            raise ValueError('Поле "Пароль" должно быть заполненно корректно')

        user = self.model(
            email=self.normalize_email(email),
            user_login=user_login
        )
        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_login=None, password=None):
        user = self.create_user(
            email,
            user_login=user_login,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class TestProjectUser(AbstractBaseUser):
    """
    Кастомная модель пользователя
    + индексирование по уникальному полю почты
    + распределение прав пользователей
    """
    user_login = models.CharField('Логин', max_length=155, db_index=True, unique=True)
    email = models.EmailField('Почта', max_length=255, db_index=True, unique=True)
    photo = models.ImageField('Фото', default='user_profile_photo.png', upload_to='users_profile_photos')

    first_name = models.CharField('Имя', max_length=255, blank=True)
    last_name = models.CharField('Фамилия', max_length=255, blank=True)
    patronymic = models.CharField('Отчество', max_length=255, blank=True)
    status = models.CharField('Статус', max_length=155, blank=True)
    description = models.TextField('О Себе', blank=True)
    date_of_birth = models.DateField('Дата рождения', blank=True, null=True)

    date_registration = models.DateTimeField('Зарегистрирован', auto_now_add=True)
    last_visit = models.DateTimeField('Посещение', auto_now=True)

    active = models.BooleanField('Авторизован', default=True)

    staff = models.BooleanField('Модератор', default=False)
    admin = models.BooleanField('Админ', default=False)

    # Поле иднтификации + обязательное поле
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_login']

    objects = TestProjectUserManager()

    def __str__(self):
        """
        Переопределение метода отображения данных о пользователе
        """
        return f'ЛОГИН: {self.user_login}, ПОЧТА: {self.email}, Аторизация: {self.active}'

    def get_slug(self):
        """
        Почта пользователя как уникальный идентификатор
        """
        return f'{self.email}'

    def get_short_name(self):
        return f'{self.last_name} {self.first_name}'

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.user_login} ПОЧТА: {self.email}'

    def get_absolute_url(self):
        """
        URL профиля пользователя (видит авторизированный пользователь)
        """
        return reverse('user_profile_page', args=[str(self.email)])

    def get_public_url(self):
        """
        URL публичного профиля (видят все зарегистрированные пользователи)
        """
        return reverse('user_public_profile_page', args=[str(self.email)])

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
