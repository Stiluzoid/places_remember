from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


def index(request):
    template_name = 'index.html'
    return render(request, template_name)
