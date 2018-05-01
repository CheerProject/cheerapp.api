from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SEX_CHOICES = (
('F', 'Female'),
('M', 'Male'),
)

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)

    first_name = models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    def __str__(self):
        return self.username

class ParentScoreCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=250)

    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    def __str__(self):
        return self.name

class ScoreCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=250)
    
    parentscorecategory = models.ForeignKey(ParentScoreCategory, on_delete=models.CASCADE)

    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    def __str__(self):
        return self.name

class ScoreMetric(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=250)

    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=250)

    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=150, unique=True)
    total_men = models.IntegerField()
    total_women = models.IntegerField()
    coach = models.CharField(max_length=150)
    description = models.CharField(max_length=250)

    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Round(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=250)

    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Championship(models.Model):
    name = models.CharField(max_length=150, unique=True)
    date = models.DateField()
    address = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Registration(models.Model):
    date = models.DateField()

    championship = models.ForeignKey(Championship, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    def __str__(self):
        return 'championship id: %i team id: %i' % (self.championship, self.team)

class UserScoreCategoryChampionship(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scorecategory = models.ForeignKey(ScoreCategory, on_delete=models.CASCADE)
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE)

    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    def __str__(self):
        return 'user id: %i scorecategory id: %i championship id: %i' % (self.user, self.scorecategory, self.championship)

class ScoreSheet(models.Model):
    min_score = models.DecimalField(max_digits=10, decimal_places=3)
    max_score = models.DecimalField(max_digits=10, decimal_places=3)
    score = models.DecimalField(max_digits=10, decimal_places=3)

    championship = models.ForeignKey(Championship, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    scorecategory = models.ForeignKey(ScoreCategory, on_delete=models.CASCADE)
    scoremetric = models.ForeignKey(ScoreMetric, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'championship id: %i round id: %i team id: %i scorecategory id: %i scoremetric id: %i user id: %i' % (self.championship, self.round, self.team, self.scorecategory, self.scoremetric, self.user)