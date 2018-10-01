from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

#done
class BaseModel(models.Model):
    description = models.CharField(max_length=250, blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

#done
class Institution(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

#done
class ScoreSheetType(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

#done
class ParentScoreCategory(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

#done
class Round(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

#done
class ScoreMetric(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

#done
class Gender(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

#done
class Level(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

#done
class Division(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

#done
class Category(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

#done
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

#done
class LocationType(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

#done
class Location(BaseModel):
    name = models.CharField(max_length=150)
    
    locationtype = models.ForeignKey(LocationType, related_name='locations', on_delete=models.CASCADE)
    location = models.ForeignKey('self', related_name='locations', on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return '[ {} ] - [ {} ] - [ {} ]'.format(self.name, self.locationtype, self.location)
    
    class Meta:
        unique_together = (('name', 'locationtype'),)

#done
class Team(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    location = models.ForeignKey(Location, related_name='teams', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ]'.format(self.name, self.location)
    
    class Meta:
        unique_together = (('name', 'location'),)

#done
class ScoreSheet(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    scoresheettype = models.ForeignKey(ScoreSheetType, related_name='score_sheets', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ]'.format(self.name, self.scoresheettype)

#done
class ScoreCategory(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    parentscorecategory = models.ForeignKey(ParentScoreCategory, related_name ='score_categories', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ]'.format(self.name, self.parentscorecategory)

#done
class Status(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '[ {} ]'.format(self.name)

#done
class Championship(BaseModel):
    name = models.CharField(max_length=150)
    date = models.DateField(default=timezone.now)
    address = models.CharField(max_length=250)

    def __str__(self):
        return '[ {} ] - [ {} ] - [ {} ]'.format(self.name, str(self.date), self.address)
    
    class Meta:
        unique_together = (('name', 'date'),)

#done    
class ChampionshipScoreSheet(BaseModel):

    championship = models.ForeignKey(Championship, related_name='championship_scoresheet', on_delete=models.CASCADE)
    scoresheet = models.ForeignKey(ScoreSheet, related_name='championship_scoresheet', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ]'.format(self.championship, self.scoresheet)
    
    class Meta:
        unique_together = (('championship', 'scoresheet'),)

#done
class Registration(BaseModel):
    date = models.DateTimeField(auto_now_add=True)
    total_men = models.IntegerField()
    total_women = models.IntegerField()
    coach = models.CharField(max_length=150)
    order = models.IntegerField()
    
    team = models.ForeignKey(Team, related_name='registrations', on_delete=models.CASCADE)
    championshipscoresheet = models.ForeignKey(ChampionshipScoreSheet, related_name='registrations', on_delete=models.CASCADE)
    divisiongroup = models.ForeignKey(DivisionGroup, related_name='registrations', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ] - [ {} ] - [ {} ] - [ {} ] - [ {} ] - [ {} ]- [ {} ]'.format(str(self.date), self.total_men, self.total_women, self.coach, self.team, self.championshipscoresheet, self.divisiongroup, self.order)
    
    class Meta:
        unique_together = (('team', 'championshipscoresheet', 'divisiongroup'),)

#done
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

#done
class UserRegistrationRound(BaseModel):
    is_active = models.BooleanField(default=True)

    registration = models.ForeignKey(Registration, related_name='registration_rounds', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, related_name='registration_rounds', on_delete=models.CASCADE)
    round = models.ForeignKey(Round, related_name='registration_rounds', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='registration_rounds', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ] - [ {} ] - [ {} ] - [ {} ]'.format(self.registration, self.status, self.round, self.user, self.is_active)
    
    class Meta:
        unique_together = (('registration', 'user', 'round'),)

#done
class UserScoreSheetElement(BaseModel):
    value = models.CharField(max_length=750)

    userregistrationround = models.ForeignKey(UserRegistrationRound, related_name='user_score_sheet_elements', on_delete=models.CASCADE)
    scoresheetelement = models.ForeignKey(ScoreSheetElement, related_name='user_score_sheet_elements', on_delete=models.CASCADE)
        
    def __str__(self):
        return '[ {} ] - [ {} ] - [ {} ]'.format(self.value, self.userregistrationround, self.scoresheetelement)
    
    class Meta:
        unique_together = (('userregistrationround', 'scoresheetelement'),)

#done
class UserSkillPermission(BaseModel):

    userregistrationround = models.ForeignKey(UserRegistrationRound, related_name='user_skill_permissions', on_delete=models.CASCADE)
    scoresheetelement = models.ForeignKey(ScoreSheetElement, related_name='user_skill_permissions', on_delete=models.CASCADE)

    def __str__(self):
        return '[ {} ] - [ {} ]'.format(self.userregistrationround, self.scoresheetelement)
    
    class Meta:
        unique_together = (('userregistrationround', 'scoresheetelement'),)