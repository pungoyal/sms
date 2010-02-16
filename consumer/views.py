from django.http import HttpResponse
from consumer.models import Text

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def add(request, phone_number, message):
    print "***************ENTERED*************"
    
    t = Text(number=phone_number, text=message)
    t.save()