from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def aparteman(request, type):
    if type == 0:
        return HttpResponse("آپارتمان با ویو رویایی")
    elif type == 1:
        return HttpResponse("آپارتمان با سرگرمی")
        