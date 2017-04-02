from django.http import HttpResponse


import random


def hello_world(request):
    return HttpResponse("Hello world")

def root_page (req):
    return HttpResponse("ROOT PAGE")

def random_number(req, maxrand=100):
    random_num = random.randrange(0, int( maxrand ))
    msg = "Random number between 0 and %s : %d" % (maxrand, random_num)
    return HttpResponse(msg)

