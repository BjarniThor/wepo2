from django.shortcuts import render_to_response
from django.template import RequestContext
from Examtool.models import *
from datetime import datetime
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    post = Exam.objects.all()   
    #quest = Question.objects.get(pk=1)
    model = { "post" : post }
             # "quest" : quest }
    # print post.text
    return render_to_response("base.html", model)

@login_required
def home(request):
    user = User.username
    return render_to_response("home.html", context_instance = RequestContext( request, user ))
