import datetime
from django.utils import timezone
from django.db import models


class Question(models.Model):
   question_text = models.CharField(max_length=200)
   pub_date = models.DateTimeField('date published')

   def __str__(self):
       return self.question_text

   def was_published_recently(self):
       now = timezone.now()
       return now - datetime.timedelta(days=1) <= self.pub_date <= now

   was_published_recently.admin_order_field = 'pub_date'
   was_published_recently.boolean = True
   was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING,)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class TodoItem1(models.Model):
    Title=models.CharField(max_length=100, null=True)
    description=models.CharField(max_length=100,null=True)
    date_time=models.DateField(auto_now_add=True)

    status=models.CharField(max_length=100)
    created_modified=models.DateField(auto_now_add=True)



    def __str__(self):
        return self.Title


