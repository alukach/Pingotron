from django.db import models
import datetime

# Create your models here.

# So, there's definitely a Player model, representing a person and their profile.
# There's a Match model, each Match is a set of games (1 or 3 or possibly more)

class Player(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(upload_to="avatar")
    email = models.EmailField(blank=True)
    quote = models.CharField(max_length=240, blank=True)

    def __unicode__(self):
        if self.alias:
            return self.alias
        else:
            return self.name

    class Meta:
        verbose_name_plural = "Players"

class Game(models.Model):
    winner = models.ForeignKey(Player, related_name='win')
    loser = models.ForeignKey(Player, related_name='loss')

    targetScore = models.IntegerField() #What score you're playing to
    winnerScore = models.IntegerField()
    loserScore = models.IntegerField()

    datetime = models.DateTimeField(blank=True)

    UNITS = (
        (u'B', u'Standard Beer Units'),
        (u'$', u'Dollars'),
        (u'L', u'Lunch'),
        (u'JJ', u'Jimmy John\'s'),
    )
    stakeValue = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    stakeUnit = models.CharField(max_length=2,choices=UNITS, blank=True)

    def save(self, **kwargs):
        if not self.datetime:
            self.datetime = datetime.datetime.now()
        super(Game, self).save()
