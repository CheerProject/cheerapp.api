from django.contrib import admin


from .models import (
    Institution,
    ScoreSheetType,
    ParentScoreCategory,
    ScoreMetric,
    Gender,
    Level,
    Division,
    Category,
    DivisionGroup,
    Team,
    Status,
    LocationType,
    Location,
    ScoreSheet,
    ScoreCategory,
    Championship,
    Registration,
    ScoreSheetElement,
    UserScoreSheetElement,
    UserSkillPermission,
)

# Admin models

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'order')
    list_display_links = ('order',)

class ScoreSheetTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

class ParentScoreCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

class ScoreMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name', 'description')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

class DivisionGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender', 'level', 'division', 'category','institution')
    list_display_links = ('gender', 'level', 'division', 'category', 'institution',)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    list_display_links = ('name', 'location',)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

class LocationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'locationtype', 'location')
    list_display_links = ('name', 'locationtype', 'location',)

class ScoreSheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'scoresheettype')
    list_display_links = ('name', 'scoresheettype',)

class ScoreCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parentscorecategory')
    list_display_links = ('name', 'parentscorecategory',)

class ChampionshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'address')
    list_display_links = ('name', 'date', 'address')

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'total_men', 'total_women', 'coach', 'team', 'championshipscoresheet', 'divisiongroup', 'status', 'order')
    list_display_links = ('date', 'total_men', 'total_women', 'coach', 'team', 'championshipscoresheet', 'divisiongroup', 'status', 'order',)

class ChampionshipScoreSheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'championship', 'scoresheet')
    list_display_links = ('championship', 'scoresheet')

class ScoreSheetElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'min_score', 'max_score', 'scoremetric', 'scorecategory', 'scoresheet')
    list_display_links = ('min_score', 'max_score', 'scoremetric', 'scorecategory', 'scoresheet',)

class UserScoreSheetElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'round', 'registration', 'user', 'scoresheetelement')
    list_display_links = ('value', 'round', 'registration', 'user', 'scoresheetelement',)

class UserSkillPermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'scorecategory', 'round', 'scoresheet')
    list_display_links = ('user', 'scorecategory', 'round', 'scoresheet')


# register your models here.
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(ScoreSheetType, ScoreSheetTypeAdmin)
admin.site.register(ParentScoreCategory, ParentScoreCategoryAdmin)
admin.site.register(ScoreMetric, ScoreMetricAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(DivisionGroup, DivisionGroupAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(LocationType, LocationTypeAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(ScoreSheet, ScoreSheetAdmin)
admin.site.register(ScoreCategory, ScoreCategoryAdmin)
admin.site.register(Championship, ChampionshipAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(ScoreSheetElement, ScoreSheetElementAdmin)
admin.site.register(UserScoreSheetElement, UserScoreSheetElementAdmin)
admin.site.register(UserSkillPermission, UserSkillPermissionAdmin)