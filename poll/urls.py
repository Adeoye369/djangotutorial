from django.urls import path
# from debug_toolbar.toolbar import debug_toolbar_urls
from . import views
from django.conf import settings

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
] 

# Add this safety check at the very bottom of the file
if settings.DEBUG:
    try:
        from debug_toolbar.toolbar import debug_toolbar_urls
        urlpatterns += debug_toolbar_urls()
    except ImportError:
        pass