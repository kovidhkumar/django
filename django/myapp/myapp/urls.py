from django.contrib import admin
from django.urls import path, include  # include is used to include app-specific urls

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin path
    path('api/', include('registration.urls')),  # Include the URLs from the registration app
]
