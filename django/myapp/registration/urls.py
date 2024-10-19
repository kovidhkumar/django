from django.urls import path
from .views import RegistrationListView, RegistrationDetailView, RegistrationCreateView, RegistrationUpdateView

urlpatterns = [
    path('registration/', RegistrationListView.as_view(), name='registration-list'),  # GET all
    path('registration/<int:id>/', RegistrationDetailView.as_view(), name='registration-detail'),  # GET by ID
    path('registration/create/', RegistrationCreateView.as_view(), name='registration-create'),  # POST
    path('registration/update/<int:id>/', RegistrationUpdateView.as_view(), name='registration-update'),  # PUT
]
