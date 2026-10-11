from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls
from . import views

app_name = "polls"
urlpatterns = [
    # example: /polls/
    path("",                        views.IndexView.as_view(), name='index'),
    # example: /polls/8/
    path("<int:pk>/",               views.DetailView.as_view(), name="detail1"),
    path("<int:pk>/details/",       views.DetailView.as_view(), name="detail2"),
    #example: /polls/3/results/
    path("<int:pk>/results/",       views.ResultsView.as_view(), name="results"),
    #example: /polls/23/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"), 
] + debug_toolbar_urls()