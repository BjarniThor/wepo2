from django.db import models
#from wepo.db import *

# Create your models here.
class Examtool (models.Model):
    #e_author = models.ForeignKey(auth_user)
    name = models.CharField(max_length=64)
    e_course = models.CharField(max_length=200)
    e_expire = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question

class Question(models.Model):
    e_q = models.ForeignKey(Examtool)
    q_text = models.CharField(max_length=200)
    def __unicode__(self):
        return self.q_text


class Choice(models.Model):
    c_to_q = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    c_value = models.BooleanField()
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text


