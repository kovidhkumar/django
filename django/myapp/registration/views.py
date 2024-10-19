from urllib import response
from venv import logger
from rest_framework import generics
from .models import Registration
from .serializers import RegistrationSerializer
from rest_framework import status  # Add this import


# GET method for all registrations
class RegistrationListView(generics.ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

# GET method for single registration by ID
class RegistrationDetailView(generics.RetrieveAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    lookup_field = 'id'  # Use 'id' to match URL path

# POST method to create a new registration
class RegistrationCreateView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error creating registration: {str(e)}")
            return response({"error": "An error occurred while creating the registration."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) # type: ignore
# PUT method to update an existing registration
class RegistrationUpdateView(generics.UpdateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    lookup_field = 'id'  # To match the ID in the URL
