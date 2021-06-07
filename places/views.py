from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import PlaceForm
from django.views import generic
from .models import Place
from django.views import generic
from django.contrib.auth.models import User

class IndexView(generic.ListView):
    template_name = 'places/index.html'
    context_object_name = 'places_list'
    model = User
    def get_queryset(self):
        return self.request.user.profile.place_set.all()

class DetailView(generic.DetailView):
    model = Place
    template_name = 'places/detail.html'
    context_object_name = 'place'
    def get_queryset(self):
        return Place.objects.all()

def get_new_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            request.user.profile.place_set.create(name_text=form.cleaned_data['name_text'], comment_text=form.cleaned_data['comment_text'])
            return HttpResponseRedirect('/places/')
    else:
        form = PlaceForm()

    return render(request, 'places/new_place.html', {'form': form})


def gmap(request):
    template_name = 'places/map.html'
    return render(request, template_name)
