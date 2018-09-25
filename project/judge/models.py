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

class Institution(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

class ScoreSheetType(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

class ParentScoreCategory(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

class Round(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

class ScoreMetric(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

class Gender(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

class Level(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

class Division(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

class Category(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

class DivisionGroup(BaseModel):

    gender = models.ForeignKey(Gender, related_name='division_groups', on_delete=models.CASCADE)
    level = models.ForeignKey(Level, related_name='divison_groups', on_delete=models.CASCADE)
    division = models.ForeignKey(Division, related_name='division_groups', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='division_groups', on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, related_name='division_group', on_delete=models.CASCADE)    

    def __str__(self):
        return '[ {} ] - [ {} ] - [ {} ] - [ {} ] - [ {} ]'.format(self.gender, self.level, self.division, self.category, self.institution)

    class Meta:
        unique_together = (('gender', 'level', 'division', 'category', 'institution'),)

class LocationType(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

class Location(BaseModel):
    name = models.CharField(max_length=150)
    
    locationtype = models.ForeignKey(LocationType, related_name='locations', on_delete=models.CASCADE)
    location = models.ForeignKey('self', related_name='locations', on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return '[ {} ] - [ {} ] - [ {} ]'.format(self.name, self.locationtype, self.location)
    
    class Meta:
        unique_together = (('name', 'locationtype'),)

class Team(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    location = models.ForeignKey(Location, related_name='teams', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ]'.format(self.name, self.location)
    
    class Meta:
        unique_together = (('name', 'location'),)

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
        return '[ {} ]'.format(self.name)

class Championship(BaseModel):
    name = models.CharField(max_length=150)
    date = models.DateField(default=timezone.now)
    address = models.CharField(max_length=250)

    def __str__(self):
        return '[ {} ] - [ {} ] - [ {} ]'.format(self.name, str(self.date), self.address)
    
    class Meta:
        unique_together = (('name', 'date'),)
    
class ChampionshipScoreSheet(BaseModel):

    championship = models.ForeignKey(Championship, related_name='championship_scoresheet', on_delete=models.CASCADE)
    scoresheet = models.ForeignKey(ScoreSheet, related_name='championship_scoresheet', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ]'.format(self.championship, self.scoresheet)
    
    class Meta:
        unique_together = (('championship', 'scoresheet'),)

class Registration(BaseModel):
    date = models.DateTimeField(auto_now_add=True)
    total_men = models.IntegerField()
    total_women = models.IntegerField()
    coach = models.CharField(max_length=150)
    order = models.IntegerField()
    
    team = models.ForeignKey(Team, related_name='registrations', on_delete=models.CASCADE)
    championshipscoresheet = models.ForeignKey(ChampionshipScoreSheet, related_name='registrations', on_delete=models.CASCADE)
    divisiongroup = models.ForeignKey(DivisionGroup, related_name='registrations', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, related_name='registrations', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ] - [ {} ] - [ {} ] - [ {} ] - [ {} ] - [ {} ]- [ {} ] - [ {} ]'.format(str(self.date), self.total_men, self.total_women, self.coach, self.team, self.championshipscoresheet, self.divisiongroup, self.status, self.order)
    
    class Meta:
        unique_together = (('team', 'championshipscoresheet', 'divisiongroup'),)

class ScoreSheetElement(BaseModel):
    min_score = models.DecimalField(max_digits=10, decimal_places=3)
    max_score = models.DecimalField(max_digits=10, decimal_places=3)

    scoremetric = models.ForeignKey(ScoreMetric, related_name='score_sheet_elements', on_delete=models.CASCADE)
    scorecategory = models.ForeignKey(ScoreCategory, related_name='score_sheet_elements', on_delete=models.CASCADE)
    scoresheet = models.ForeignKey(ScoreSheet, related_name='score_sheet_elements', on_delete=models.CASCADE)
    
    def __str__(self):
        return '[ {} ] - [ {} ] - [ {} ] - [ {} ] - [ {} ]'.format(self.min_score, self.max_score, self.scoremetric, self.scorecategory, self.scoresheet)
    
    class Meta:
        unique_together = (('scoremetric', 'scorecategory', 'scoresheet'),)

class UserScoreSheetElement(BaseModel):
    value = models.CharField(max_length=750)

    registration = models.ForeignKey(Registration, related_name='user_score_sheet_elements', on_delete=models.CASCADE)
    scoresheetelement = models.ForeignKey(ScoreSheetElement, related_name='user_score_sheet_elements', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='user_score_sheet_elements', on_delete=models.CASCADE)
    round = models.ForeignKey(Round, related_name='user_score_sheet_elements', on_delete=models.CASCADE)
    
    def __str__(self):
        return '[ {} ] - [ {} ] - [ {} ] - [ {} ] - [ {} ]'.format(self.value, self.round, self.registration, self.user, self.scoresheetelement)
    
    class Meta:
        unique_together = (('registration', 'scoresheetelement', 'user', 'round'),)

class UserSkillPermission(BaseModel):

    round = models.ForeignKey(Round, related_name='user_skill_permissions', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='user_skill_permissions', on_delete=models.CASCADE)
    scorecategory = models.ForeignKey(ScoreCategory, related_name='user_skill_permissions', on_delete=models.CASCADE)
    scoresheet = models.ForeignKey(ScoreSheet, related_name='user_skill_permissions', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ] - [ {} ] - [ {} ]'.format(self.round, self.user, self.scorecategory, self.scoresheet)
    
    class Meta:
        unique_together = (('round', 'user', 'scorecategory', 'scoresheet'),)
