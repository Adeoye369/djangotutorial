import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=300)
    published_date= models.DateTimeField("published date")

    def __str__(self)-> str:
        return self.question_text

    @admin.display(
            boolean=True, 
            ordering="published_date", 
            description="Published recently"
            )
    def was_published_recently(self) -> bool:
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.published_date <= now

class ChoiceSelection(models.Model):
    question   = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes      = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"choice: {self.choice_text} votes: {self.votes}\n"
    

