import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

#Question is name of the table. CharField is a character field
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#on delete is if we delete that question, it will delete the choices)
class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text