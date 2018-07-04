from django.contrib import admin


from .models import (
    ScoreSheetType,
    ParentScoreCategory,
    Round,
    ScoreMetric,
    Gender,
    Level,
    Division,
    Category,
    Team,
    ScoreSheet,
    ScoreCategory,
    Championship,
    Registration,
    ScoreSheetElement,
    UserScoreSheetElement,
    UserSkillPermission,
)

# Admin models

class ScoreSheetTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name')

class ParentScoreCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name')

class RoundAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name')

class ScoreMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name')

class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name')

class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name')

class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name')

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'total_men', 'total_women', 'coach')
    list_display_links = ('name', 'total_men', 'total_women', 'coach')

class ScoreSheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'scoresheettype')
    list_display_links = ('name', 'scoresheettype')

class ScoreCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parentscorecategory')
    list_display_links = ('name', 'parentscorecategory')

class ChampionshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'address', 'scoresheet')
    list_display_links = ('name', 'date', 'address', 'scoresheet')

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'gender', 'level', 'division', 'category', 'team', 'championship')
    list_display_links = ('date', 'gender', 'level', 'division', 'category', 'team', 'championship')

class ScoreSheetElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'min_score', 'max_score', 'scoremetric', 'scorecategory', 'scoresheet')
    list_display_links = ('min_score', 'max_score', 'scoremetric', 'scorecategory', 'scoresheet')

class UserScoreSheetElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'score', 'completed', 'round', 'registration', 'user', 'scoresheetelement')
    list_display_links = ('score', 'completed', 'round', 'registration', 'user', 'scoresheetelement')

class UserSkillPermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'scoresheetelement')
    list_display_links = ('user', 'scoresheetelement')


# register your models here.

admin.site.register(ScoreSheetType, ScoreSheetTypeAdmin)
admin.site.register(ParentScoreCategory, ParentScoreCategoryAdmin)
admin.site.register(Round, RoundAdmin)
admin.site.register(ScoreMetric, ScoreMetricAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(ScoreSheet, ScoreSheetAdmin)
admin.site.register(ScoreCategory, ScoreCategoryAdmin)
admin.site.register(Championship, ChampionshipAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(ScoreSheetElement, ScoreSheetElementAdmin)
admin.site.register(UserScoreSheetElement, UserScoreSheetElementAdmin)
admin.site.register(UserSkillPermission, UserSkillPermissionAdmin)