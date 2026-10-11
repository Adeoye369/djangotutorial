from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse

from .models import Question, ChoiceSelection


def index (request: HttpRequest) -> HttpResponse:
    qlist = get_list_or_404(Question.objects.order_by("-published_date"))
    context = {"latest_qlist": qlist}
    return render(request, "polls/index.html", context)



def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 
                  "polls/detail.html", 
                  {"q": question})


def results(request:HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"q": question})


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    try:
        sel_choice = question.choiceselection_set.get(pk=request.POST["choice"])
    except(KeyError, ChoiceSelection.DoesNotExist):
        return render(request,
                      "polls/detail.html",
                      {"q": question,
                       "error_message" : "Guy, You no select any choice na!"
                       })
    else:
        sel_choice.votes = F("votes") + 1
        sel_choice.save()

        return  HttpResponseRedirect(reverse("polls:results", args=[question.id]))
    

