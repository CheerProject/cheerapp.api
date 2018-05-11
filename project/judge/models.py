from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class ParentScoreCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=250)

    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

class ScoreCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=250)
    
    parentscorecategory = models.ForeignKey(ParentScoreCategory, related_name ='score_categories', on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

class ScoreMetric(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=250)

    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=250)

    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=150, unique=True)
    total_men = models.IntegerField()
    total_women = models.IntegerField()
    coach = models.CharField(max_length=150)
    description = models.CharField(max_length=250)

    level = models.ForeignKey(Level, related_name='teams', on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

class Round(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=250)

    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

class Championship(models.Model):
    name = models.CharField(max_length=150, unique=True)
    date = models.DateField(default=timezone.now)
    address = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

class Registration(models.Model):
    date = models.DateField(default=timezone.now)

    championship = models.ForeignKey(Championship, related_name='registrations', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name='registrations', on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return 'championship id: %i team id: %i' % (self.championship, self.team)

class UserScoreCategoryChampionship(models.Model):
    
    user = models.ForeignKey('auth.User', related_name='user_score_category_championships', on_delete=models.CASCADE)
    scorecategory = models.ForeignKey(ScoreCategory, related_name='user_score_category_championships',  on_delete=models.CASCADE)
    championship = models.ForeignKey(Championship, related_name='user_score_category_championships',  on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return 'user id: %i scorecategory id: %i championship id: %i' % (self.user, self.scorecategory, self.championship)

class ScoreSheet(models.Model):
    min_score = models.DecimalField(max_digits=10, decimal_places=3)
    max_score = models.DecimalField(max_digits=10, decimal_places=3)
    score = models.DecimalField(max_digits=10, decimal_places=3)

    championship = models.ForeignKey(Championship, related_name='score_sheets', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name='score_sheets', on_delete=models.CASCADE)
    round = models.ForeignKey(Round, related_name='score_sheets', on_delete=models.CASCADE)
    scorecategory = models.ForeignKey(ScoreCategory, related_name='score_sheets', on_delete=models.CASCADE)
    scoremetric = models.ForeignKey(ScoreMetric, related_name='score_sheets', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='score_sheets', on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return 'championship id: %i round id: %i team id: %i scorecategory id: %i scoremetric id: %i user id: %i' % (self.championship, self.round, self.team, self.scorecategory, self.scoremetric, self.user)