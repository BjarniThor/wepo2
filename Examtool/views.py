from django.shortcuts import render_to_response
from django.template import RequestContext
from Examtool.models import *
from datetime import datetime
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from Examtool.models import ExamForm
from django.core.urlresolvers import reverse

@login_required
def home(request): 
    allExams = Exam.objects.all()

    examIds = Linq.objects.filter(user_id=request.user.id)
            
    userObj = { "user" : request.user,
                "exams" : allExams,
                "linq" : examIds }
    
    if not request.user.is_authenticated():
        return render_to_response('home.html', {'user': 'Not loggged in'}, )
    else:
        return render_to_response('home.html', userObj , RequestContext(request))

@login_required
def create(request):
    if request.method == 'POST':
        f = ExamForm(request.POST)        
        if f.is_valid():
            new_exam = f.save()
            return HttpResponseRedirect(reverse('Examtool.views.home'))
        else:
            return HttpResponseRedirect(reverse('Examtool.views.create'))
    else:
        f = ExamForm()
        fe = { "fex" : f }
        return render_to_response('create.html', fe, RequestContext(request))
    