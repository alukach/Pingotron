from django.db import models
from django.forms import ModelForm
from Pingotron.record.models import *

class PlayerForm(ModelForm):
	class Meta:
		model = Player