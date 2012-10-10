from django.db import models
import datetime

# Create your models here.

# So, there's definitely a Player model, representing a person and their profile.
# There's a Match model, each Match is a set of games (1 or 3 or possibly more)

class Player(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(upload_to="avatar", blank=True)
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

    winnerScore = models.IntegerField()
    loserScore = models.IntegerField()

    targetScore = models.IntegerField(default="11") #What score you're playing to
    winBy = models.IntegerField(default="2")

    datetime = models.DateTimeField(blank=True)

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
        if (self.stakeValue and not self.stakeUnit) or (self.stakeUnit and not self.stakeValue):
            return
        if (self.loserScore > self.winnerScore):
            return
        if not (self.winnerScore - self.loserScore) >= self.winBy:
            return
        if not self.datetime:
            self.datetime = datetime.datetime.now()
        super(Game, self).save()

    def __unicode__(self):
        if self.stakeValue:
            return "%s - %s (%s) vs %s (%s) for %s %s" % (self.datetime.strftime('%Y-%m-%d %I:%M%p'), self.winner, self.winnerScore, self.loser, self.loserScore, self.stakeValue, self.stakeUnit)
        else:
            return "%s - %s (%s) vs %s (%s)" % (self.datetime.strftime('%Y-%m-%d %I:%M%p'), self.winner, self.winnerScore, self.loser, self.loserScore)
