import datetime

from django.utils import timezone

from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.db.models import F, QuerySet
from django.urls import reverse
from django.views import generic

from .models import Question, ChoiceSelection


class IndexView(generic.ListView):
    template_name="polls/index.html"
    context_object_name="latest_qlist"

    def get_queryset(self)-> QuerySet[Question]:
        """
        Return the last five published questions.
        (not including those set to be published in the future).
        """
        return Question.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")



class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    context_object_name = "q"

    def get_queryset(self)->QuerySet:
        """ Excludes any questions that aren't published yet """
        return Question.objects.filter(published_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    context_object_name = "q"


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
    

