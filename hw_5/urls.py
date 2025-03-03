from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from todos import views  # 🔹 'todos' қосымшасының views модулін импорттау

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='todos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.todo_list, name='home'),
    path('todos/', include('todos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # 🔹 Django аутентификация маршрутын қосу
]
