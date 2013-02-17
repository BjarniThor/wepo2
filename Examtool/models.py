from django.db import models
import datetime

# Create your models here.
class Exam(models.Model):
    e_name = models.CharField(max_length=128)
    e_author = models.CharField(max_length=128)
    e_course = models.CharField(max_length=256)
    e_datecreated = models.DateField(default = datetime.datetime.now())
    e_expire = models.DateTimeField('date published')

class Question(models.Model):
    e_id = models.ForeignKey(Exam)
    q_name = models.CharField(max_length=64)
    q_text = models.CharField(max_length=256)

class QuestionChoices(models.Model):
    q_id = models.ForeignKey(Question)
    q_option = models.CharField(max_length=256)
    q_outcome = models.BooleanField()


