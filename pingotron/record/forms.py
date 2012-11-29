from django.db import models
from django import forms
from pingotron.record.models import *

class EditProfile(forms.ModelForm):
	class Meta:
		model = PlayerProfile

class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
    def clean(self):
        cleaned_data = super(CreateGameForm, self).clean()
        
        # If score difference isn't greater than 2 points, raise exception
        if not abs(self.cleaned_data['winnerScore'] - self.cleaned_data['loserScore']) >= 2:
            raise forms.ValidationError("A player must win by at least 2 points")
        
        # If loser has higher score than winner, switch loser and winner
        if (self.cleaned_data['loserScore'] > self.cleaned_data['winnerScore']):
            self.cleaned_data['winner'], self.cleaned_data['loser'] = self.cleaned_data['loser'], self.cleaned_data['winner']
            self.cleaned_data['loserScore'], self.cleaned_data['winnerScore'] = self.cleaned_data['winnerScore'],self.cleaned_data['loserScore']
        
        # If stake value given but no stake unit, or vice versa, raise exception
        if (bool(self.cleaned_data['stakeValue']) != bool(self.cleaned_data['stakeUnit'])):
            raise forms.ValidationError("Stake value and units do not match up (one given without the other)")
        return cleaned_data
