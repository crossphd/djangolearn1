"""
Definition of models.
"""

from django.db import models
from django.db.models import Sum

class Poll(models.Model):
    """A poll object for use in the application views and repository."""
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=100, blank=True)

    def total_votes(self):
        """Calculates the total number of votes for this poll."""
        return self.choice_set.aggregate(Sum('votes'))['votes__sum']

    def __unicode__(self):
        """Returns a string representation of a poll."""
        return self.text

class Choice(models.Model):
    """A poll choice object for use in the application views and repository."""
    poll = models.ForeignKey(Poll)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def votes_percentage(self):
        """Calculates the percentage of votes for this choice."""
        total = self.poll.total_votes()
        return self.votes / float(total) * 100 if total > 0 else 0

    def __unicode__(self):
        """Returns a string representation of a choice."""
        return self.text

class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    shares = models.IntegerField(default=0)
    price = models.FloatField()
    dividend_yield = models.FloatField()
    dividend_amount = models.FloatField()
    pub_date = models.DateTimeField('date published')
    def value(self):
        return shares * price

    def annual_dividend(self):
        return dividend_amount * shares

    def __unicode__(self):
        """Returns a string representation of a poll."""
        return self.text

class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    stock = models.ForeignKey(Stock)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        """Returns a string representation of a poll."""
        return self.text

   

