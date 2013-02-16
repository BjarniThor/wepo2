# Create your views here.
from Examtool.models import *
from django.shortcuts import *

def index(request):
    post = Examtool.objects.get(pk=1)
    model = { "post" : post }
    # print post.text
    return render_to_response("index.html", model)
