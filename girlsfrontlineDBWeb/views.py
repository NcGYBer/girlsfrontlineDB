from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main(request):
    return render(request, 'girlsfrontlineDBWeb/main.html', {})


def index(request):
    return HttpResponse("Index")