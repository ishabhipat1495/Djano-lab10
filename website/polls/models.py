import datetime
from django.db import models
from django.utils import timezone
#from django import forms
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# class PostForm(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     your_answer = models.CharField(label='Your answer', max_length=200)
#     your_name = models.CharField(label='Your name', max_length=20)
#     def __str__(self):
#         return self.your_answer
#     def __str__(self):
#         return self.your_name


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    author_text = models.CharField(max_length=20)
    def __str__(self):
        return self.answer_text
    def __str__(self):
        return self.author_text
"""
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text"""
# Create your models here.
