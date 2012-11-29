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
            form.save()
            return HttpResponse('<p>Form saved!</p>')
        else:
            raise
    else:
        form = CreateGameForm() # An unbound form
    return render(request, 'record/create_game.html', {'form': form,})

@login_required
def edit_profile(request):
    profile = get_object_or_404(PlayerProfile, user=request.user)
    if request.method == 'POST': # If the form has been submitted...
        form = EditProfile(request.POST, instance=profile) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponse('<p>Form saved!</p>')
        else:
            raise
    else:
        form = EditProfile(instance=profile) # An unbound form
    return render(request, 'profiles/edit_profile.html', {'user': profile.user, 'form': form,})