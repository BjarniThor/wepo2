from django.db import models
from django.forms import ModelForm
from django import forms
import datetime

# Create your models here.
class Exam(models.Model):
    e_name = models.CharField(max_length=128)
    e_author = models.CharField(max_length=128)
    e_course = models.CharField(max_length=256)
    e_datecreated = models.DateField(default = datetime.datetime.now())
    e_expire = models.DateTimeField('date published')

    def __unicode__(self):
        return self.e_name

class Question(models.Model):
    e_id = models.ForeignKey(Exam)
    q_name = models.CharField(max_length=64)
    q_text = models.CharField(max_length=256)

    def __unicode__(self):
        return self.q_name

class QuestionChoices(models.Model):
    q_id = models.ForeignKey(Question)
    q_option = models.CharField(max_length=256)
    q_outcome = models.BooleanField()

    def __unicode__(self):
        return self.q_option

class Linq(models.Model):
    user_id = models.IntegerField()
    exam_id = models.IntegerField()

class ExamForm(ModelForm):
    class Meta:
        model = Exam
'''
class ExamForm(forms.Form):
    e_name = forms.CharField(max_length=100)
    e_author = forms.CharField(max_length=100)
    e_course = forms.DateField(required=False)
'''
