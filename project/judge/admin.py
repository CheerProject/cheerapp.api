from django.contrib import admin


from .models import (
    Institution,
    ScoreSheetType,
    ParentScoreCategory,
    ScoreMetric,
    Gender,
    Round,
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
    ChampionshipScoreSheet,
    UserRegistrationRound
)

# Admin models

#done
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

#done
class ScoreSheetTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

#done
class ParentScoreCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

#done
class ScoreMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

#done
class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

#done
class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

#done
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

#done
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name', 'description')

#done
class RoundAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

#done
class DivisionGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender', 'level', 'division', 'category','institution')
    list_display_links = ('gender', 'level', 'division', 'category', 'institution',)

#done
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    list_display_links = ('name', 'location',)

#done
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

#done
class LocationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

#done
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'locationtype', 'location')
    list_display_links = ('name', 'locationtype', 'location',)

#done
class ScoreSheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'scoresheettype')
    list_display_links = ('name', 'scoresheettype',)

#done
class ScoreCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parentscorecategory')
    list_display_links = ('name', 'parentscorecategory',)

#done
class ChampionshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'address')
    list_display_links = ('name', 'date', 'address')

#done
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'total_men', 'total_women', 'coach', 'team', 'championshipscoresheet', 'divisiongroup', 'order')
    list_display_links = ('date', 'total_men', 'total_women', 'coach', 'team', 'championshipscoresheet', 'divisiongroup', 'order',)

#done
class ChampionshipScoreSheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'championship', 'scoresheet')
    list_display_links = ('championship', 'scoresheet')

#done
class ScoreSheetElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'min_score', 'max_score', 'scoremetric', 'scorecategory', 'scoresheet')
    list_display_links = ('min_score', 'max_score', 'scoremetric', 'scorecategory', 'scoresheet',)

#done
class UserScoreSheetElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'userregistrationround', 'scoresheetelement')
    list_display_links = ('value', 'userregistrationround', 'scoresheetelement',)

#done
class UserSkillPermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'userregistrationround', 'scoresheetelement')
    list_display_links = ('userregistrationround', 'scoresheetelement')

#done
class UserRegistrationRoundAdmin(admin.ModelAdmin):
    list_display = ('id', 'round', 'status', 'registration', 'user', 'is_active')
    list_display_links = ('round', 'status', 'registration', 'user', 'is_active')


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
admin.site.register(ChampionshipScoreSheet, ChampionshipScoreSheetAdmin)
admin.site.register(UserRegistrationRound, UserRegistrationRoundAdmin)
admin.site.register(Round, RoundAdmin)