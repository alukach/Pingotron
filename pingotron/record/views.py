# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from pingotron.record.forms import *

@login_required
def overview(request):
    return HttpResponse('<p>Some day this will be stats overview</p>')

@login_required
def create_game(request):
    if request.method == 'POST': # If the form has been submitted...
        form = CreateGameForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            #address = form.cleaned_data['address']
            #neighborhood = form.cleaned_data['neighborhood']
            #location = form.cleaned_data['location']
            form.save()
            #return HttpResponseRedirect(reverse('pingotron.record.views.overview')) # Redirect after POST
            render(request, 'record/create_game.html', {'form': form,})
            return HttpResponse('<p>Game created</p>')
    else:
        form = CreateGameForm() # An unbound form
    return render(request, 'record/create_game.html', {'form': form,})
