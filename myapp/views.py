from django.http import HttpResponse
#  render template
from django.shortcuts import render


def index(request):
    return render(request, "shopify/index.html")
