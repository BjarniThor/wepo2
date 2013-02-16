# Create your views here.
from Examtool.models import *
from django.shortcuts import *

def index(request):
    post = Examtool.objects.get(pk=1)
    quest = Question.objects.get(pk=1)
    model = { "post" : post,
              "quest" : quest }
    # print post.text
    return render_to_response("index.html", model)
