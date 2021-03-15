# Utils
from django.contrib import admin

# Models
from django.contrib.auth.models import Group
from .models import TestProjectUser

# Добавляем отображение моделей в админку
admin.site.register(TestProjectUser)

# Убираем отображение групп
admin.site.unregister(Group)
