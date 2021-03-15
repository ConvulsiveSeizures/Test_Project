# Utils
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

# Routing
from django.urls import path

# Views
from test_project_users import views as users_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_view.index_page, name='index_page'),
    path('registration/', users_view.registration_view, name='registration_page'),
    path('login/', users_view.login_view, name='login_page'),
    path('<str:email>/', users_view.user_profile, name='user_profile_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
