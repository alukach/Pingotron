from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class PlayerProfile(models.Model):
    user = models.OneToOneField(User)
    alias = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(upload_to="avatar", blank=True)
    quote = models.CharField(max_length=240, blank=True)

    def __unicode__(self):
        if self.alias:
            return self.alias
        else:
            return self.user.username
    class Meta:
        verbose_name_plural = "Player Profiles"

# Django-Profiles stuff: https://bitbucket.org/ubernostrum/django-profiles/src/tip/docs/overview.txt
def create_player_with_user(sender, **kwargs):
    """When creating a new user, make a profile for him or her."""
    u = kwargs["instance"]
    if not PlayerProfile.objects.filter(user=u):
        PlayerProfile(user=u).save()

# Signal - Create PlayerProfile when User is created
post_save.connect(create_player_with_user, sender=User)

class Game(models.Model):
    winner = models.ForeignKey(User, related_name='win')
    winnerScore = models.IntegerField()
    loser = models.ForeignKey(User, related_name='loss')
    loserScore = models.IntegerField()
    targetScore = models.IntegerField(default="11", choices=((11, 11),(21, 21))) #What score you're playing to
    gameDateTime = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    dateCreated = models.DateTimeField(default=datetime.datetime.now(), auto_now_add=True)
    #createdBy = models.ForeignKey(User, related_name="created%(app_label)s_%(class)s_related")

    lastModified = models.DateTimeField(blank=True, null=True)
    #modifiedBy = models.ForeignKey(User, related_name="modified%(app_label)s_%(class)s_related", blank=True, null=True)

    UNITS = (
        (u'B', u'Standard Beer Units'),
        (u'$', u'Dollars'),
        (u'L', u'Lunch'),
        (u'JJ', u'Jimmy John\'s'),
    )
    stakeValue = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    stakeUnit = models.CharField(max_length=2,choices=UNITS, blank=True, null=True)

    def save(self, **kwargs):
        """
        Some basic last-minute validation and fill in possible missing data.
        Data should fully be cleaned at the form: https://docs.djangoproject.com/en/1.1/ref/forms/validation/#form-field-default-cleaning
        """
        if not self.datetime:
            self.datetime = datetime.datetime.now()
        super(Game, self).save()

    def __unicode__(self):
        if self.stakeValue:
            return "%s - %s (%s) vs %s (%s) for %s %s" % (self.datetime.strftime('%Y-%m-%d %I:%M%p'), self.winner, self.winnerScore, self.loser, self.loserScore, self.stakeValue, self.stakeUnit)
        else:
            return "%s - %s (%s) vs %s (%s)" % (self.datetime.strftime('%Y-%m-%d %I:%M%p'), self.winner, self.winnerScore, self.loser, self.loserScore)
