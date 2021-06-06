from django.views import generic
from django.contrib.auth.models import User

class IndexView(generic.ListView):
    template_name = 'places/index.html'
    context_object_name = 'places_list'
    model = User
    def get_queryset(self):
        return self.request.user.profile.place_set.all()
