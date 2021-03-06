# Generated by Django 3.1.7 on 2021-03-15 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestProjectUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_login', models.CharField(db_index=True, max_length=155, unique=True, verbose_name='Логин')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Почта')),
                ('photo', models.ImageField(default='user_profile_photo.png', upload_to='users_profile_photos', verbose_name='Фото')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('status', models.CharField(blank=True, max_length=155, verbose_name='Статус')),
                ('description', models.TextField(blank=True, verbose_name='О Себе')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('date_registration', models.DateTimeField(auto_now_add=True, verbose_name='Зарегистрирован')),
                ('last_visit', models.DateTimeField(auto_now_add=True, verbose_name='Посещение')),
                ('active', models.BooleanField(default=True, verbose_name='Авторизован')),
                ('staff', models.BooleanField(default=False, verbose_name='Модератор')),
                ('admin', models.BooleanField(default=False, verbose_name='Админ')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
