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
    RegistrationRound
)

# Admin models

#done
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

#done
class ScoreSheetTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

#done
class ParentScoreCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

#done
class RoundAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

#done
class ScoreMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

#done
class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

#done
class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

#done
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

#done
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

#done
class DivisionGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender', 'level', 'division', 'category','institution')
    list_display_links = ('gender', 'level', 'division', 'category', 'institution',)

#done
class LocationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

#done
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'locationtype', 'location')
    list_display_links = ('locationtype', 'location',)

#done
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    list_display_links = ('location',)

#done
class ScoreSheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'scoresheettype')
    list_display_links = ('scoresheettype',)

#done
class ScoreCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parentscorecategory')
    list_display_links = ('parentscorecategory',)

#done
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

#done
class ChampionshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'address')

#done
class ChampionshipScoreSheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'championship', 'scoresheet')
    list_display_links = ('championship', 'scoresheet')

#done
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'total_men', 'total_women', 'coach', 'order', 'team', 'championshipscoresheet', 'divisiongroup')
    list_display_links = ('team', 'championshipscoresheet', 'divisiongroup',)

#done
class ScoreSheetElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'min_score', 'max_score', 'scoremetric', 'scorecategory', 'scoresheet')
    list_display_links = ('scoremetric', 'scorecategory', 'scoresheet',)

#done
class RegistrationRoundAdmin(admin.ModelAdmin):
    list_display = ('id', 'round', 'status', 'registration')
    list_display_links = ('round', 'status', 'registration')

#done
class UserScoreSheetElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'registrationround', 'user', 'scoresheetelement')
    list_display_links = ('registrationround', 'user', 'scoresheetelement',)

#done
class UserSkillPermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'registrationround', 'scoresheetelement')
    list_display_links = ('user', 'registrationround', 'scoresheetelement')


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
admin.site.register(RegistrationRound, RegistrationRoundAdmin)
admin.site.register(Round, RoundAdmin)