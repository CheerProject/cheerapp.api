from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class BaseModel(models.Model):
    description = models.CharField(max_length=250, blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

class ScoreSheetType(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class ParentScoreCategory(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Round(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class ScoreMetric(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Gender(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Level(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Division(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Group(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class DivisionGroup(BaseModel):

    gender = models.ForeignKey(Gender, related_name='division_groups', on_delete=models.CASCADE)
    level = models.ForeignKey(Level, related_name='divison_groups', on_delete=models.CASCADE)
    division = models.ForeignKey(Division, related_name='division_groups', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='division_groups', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='division_group', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ]- [ {} ]- [ {} ]- [ {} ]'.format(self.gender, self.level, self.division, self.category, self.group)

class LocationType(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Location(BaseModel):
    name = models.CharField(max_length=150)
    
    locationtype = models.ForeignKey(LocationType, related_name='locations', on_delete=models.CASCADE)
    location = models.ForeignKey('self', related_name='locations', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Team(BaseModel):
    name = models.CharField(max_length=150, unique=True)
    total_men = models.IntegerField()
    total_women = models.IntegerField()
    coach = models.CharField(max_length=150)

    location = models.ForeignKey(Location, related_name='teams', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ScoreSheet(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    scoresheettype = models.ForeignKey(ScoreSheetType, related_name='score_sheets', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ]'.format(self.name, self.scoresheettype)

class ScoreCategory(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    parentscorecategory = models.ForeignKey(ParentScoreCategory, related_name ='score_categories', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ]'.format(self.name, self.parentscorecategory)

class Status(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Championship(BaseModel):
    name = models.CharField(max_length=150)
    date = models.DateField(default=timezone.now)
    address = models.CharField(max_length=250)

    scoresheet = models.ForeignKey(ScoreSheet, related_name='championships', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ] - [ {} ]'.format(self.name, str(self.date), self.scoresheet)
    
    class Meta:
        unique_together = (('name', 'date'),)

class Registration(BaseModel):
    date = models.DateTimeField(auto_now_add=True)

    team = models.ForeignKey(Team, related_name='registrations', on_delete=models.CASCADE)
    championship = models.ForeignKey(Championship, related_name='registrations', on_delete=models.CASCADE)
    divisiongroup = models.ForeignKey(DivisionGroup, related_name='registrations', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, related_name='registrations', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ] - [ {} ] - [ {} ]- [ {} ]'.format(str(self.date), self.team, self.championship, self.divisiongroup, self.status)

class ScoreSheetElement(BaseModel):
    min_score = models.DecimalField(max_digits=10, decimal_places=3)
    max_score = models.DecimalField(max_digits=10, decimal_places=3)

    scoremetric = models.ForeignKey(ScoreMetric, related_name='score_sheet_elements', on_delete=models.CASCADE)
    scorecategory = models.ForeignKey(ScoreCategory, related_name='score_sheet_elements', on_delete=models.CASCADE)
    scoresheet = models.ForeignKey(ScoreSheet, related_name='score_sheet_elements', on_delete=models.CASCADE)
    
    def __str__(self):
        return '[ {} ] - [ {} ] - [ {} ]'.format(self.scoremetric, self.scorecategory, self.scoresheet)

class UserScoreSheetElement(BaseModel):
    score = models.DecimalField(max_digits=10, decimal_places=3)
    completed = models.BooleanField(default=False)

    registration = models.ForeignKey(Registration, related_name='user_score_sheet_elements', on_delete=models.CASCADE)
    scoresheetelement = models.ForeignKey(ScoreSheetElement, related_name='user_score_sheet_elements', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='user_score_sheet_elements', on_delete=models.CASCADE)
    round = models.ForeignKey(Round, related_name='user_score_sheet_elements', on_delete=models.CASCADE)
    
    def __str__(self):
        return '[ {} ] - [ {} ] - [ {} ] - [ {} ] - [ {} ] - [ {} ]'.format(self.score, self.completed, self.round, self.registration, self.user, self.scoresheetelement)

class UserSkillPermission(BaseModel):

    user = models.ForeignKey('auth.User', related_name='user_score_sheets', on_delete=models.CASCADE)
    scorecategory = models.ForeignKey(ScoreCategory, related_name='user_score_sheets', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ]'.format(self.user, self.scorecategory)