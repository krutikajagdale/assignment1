from django.shortcuts import render

from django.http import HttpResponse

def cse(request):
    return HttpResponse("Welcome on CSE page")
def etc(request):
    return HttpResponse("Welcome on ETC page")
def mech(request):
    return HttpResponse("Welcome on mech page")
def civil(request):
    return HttpResponse("Welcome on civil page")
