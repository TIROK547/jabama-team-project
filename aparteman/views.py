from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def aparteman_view_royayee(request):
    return HttpResponse("آپارتمان با ویو رویایی")
def aparteman_sargarmi(request):
    return HttpResponse("آپارتمان با سرگرمی")