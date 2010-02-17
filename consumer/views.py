from django.http import HttpResponse
from consumer.models import Text

def index(request):
    return HttpResponse("Hello, world. You're at the consumer index.")

def add(request, phone_number, message):
    t = Text(number=phone_number, text=message)
    t.save()
    t = u'\u2a06\u3306\u2c06\u4a06\u4406'
    print str(t)

    return HttpResponse(message)
