from django.db import models
from django.forms import ModelForm
from pingotron.record.models import *

class PlayerForm(ModelForm):
	class Meta:
		model = PlayerProfile

class CreateGameForm(ModelForm):
    class Meta:
        model = Game
