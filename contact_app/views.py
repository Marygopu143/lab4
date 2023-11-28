from django.shortcuts import render
from .models import Contact
# Create your views here.
def index(request):
    return render(request, 'contact_app/index.html')

def help(request):
    return render(request, 'contact_app/help.html')

def contacts(request):
    contact_list = Contact.objects.order_by('first_name')
    contact_dict = {'contacts': contact_list}
    return render(request, 'contact_app/contacts.html', context=contact_dict)