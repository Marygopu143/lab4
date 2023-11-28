from django.urls import path
from .views import index, help, contacts

urlpatterns = [
    path("", index, name="index"),
    path("help/", help, name="help"),
    path("contacts/", contacts, name="contacts"),
    # Add other paths as needed
]