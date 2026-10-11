from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    # return HttpResponse("Is this your Home?")
    return render(request, "prodman/index.html")

