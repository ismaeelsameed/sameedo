from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext


def home(request, template_name='index.html'):
    return render_to_response(template_name, {}, context_instance=RequestContext(request))
