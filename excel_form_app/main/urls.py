from django.contrib import admin
from django.urls import path, include
from . import views
from .views import upload_excel, show_people, SignUpView

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('people/', show_people, name='people'),
    path('upload/', upload_excel, name='upload_excel'),
    path('add/', views.add_person, name='add_person'),
]
