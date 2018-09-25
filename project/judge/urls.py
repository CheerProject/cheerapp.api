from django.conf.urls import url, include
from rest_framework import routers
from project.api_auth import views
from rest_framework.urlpatterns import format_suffix_patterns


from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import  TokenRefreshView

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
#catalogs
router.register(r'institution', InstitutionViewSet)
router.register(r'gender', GenderViewSet)
router.register(r'level', LevelViewSet)
router.register(r'division', DivisionViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'round', RoundViewSet)
router.register(r'score-sheet-type', ScoreSheetTypeViewSet)
router.register(r'score-metric', ScoreMetricViewSet)
router.register(r'location-type', LocationTypeViewSet)
router.register(r'status', StatusViewSet)
router.register(r'parent-score-category', ParentScoreCategoryViewSet)
router.register(r'division-group', DivisionGroupViewSet)
router.register(r'score-category', ScoreCategoryViewSet)
router.register(r'location', LocationViewSet)
router.register(r'score-sheet', ScoreSheetViewSet)
router.register(r'score-sheet-element', ScoreSheetElementViewSet)
router.register(r'team', TeamViewSet)
router.register(r'user-skill-permission', UserSkillPermissionViewSet)
router.register(r'championship', ChampionshipViewSet)
router.register(r'registration', RegistrationViewSet)
router.register(r'user-score-sheet-element', UserScoreSheetElementViewSet)
router.register(r'championship-score-sheet', ChampionshipScoreSheetViewSet)



urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^championships/(?P<pk1>[0-9]+)/divisions$', DashboardViewSet.as_view()),
    url(r'^championships/(?P<pk1>[0-9]+)/divisions/(?P<pk2>[0-9]+)/registrations$', TabsViewSet.as_view()),
    url(r'^championships/(?P<pk1>[0-9]+)/divisions/(?P<pk2>[0-9]+)/registrations/(?P<pk3>[0-9]+)/rounds/(?P<pk4>[0-9]+)/scoresheets$', ScoreSheetUserViewSet.as_view()),
]
