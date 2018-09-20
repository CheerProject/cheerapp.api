from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
#from .schemas import get_predictor_schema
from decimal import Decimal

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderWriteSerializer

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelWriteSerializer

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionWriteSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryWriteSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupWriteSerializer

class RoundViewSet(viewsets.ModelViewSet):
    queryset = Round.objects.all()
    serializer_class = RoundWriteSerializer

class ScoreSheetTypeViewSet(viewsets.ModelViewSet):
    queryset = ScoreSheetType.objects.all()
    serializer_class = ScoreSheetTypeWriteSerializer

class ScoreMetricViewSet(viewsets.ModelViewSet):
    queryset = ScoreMetric.objects.all()
    serializer_class = ScoreMetricWriteSerializer

class LocationTypeViewSet(viewsets.ModelViewSet):
    queryset = LocationType.objects.all()
    serializer_class = LocationTypeWriteSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusWriteSerializer

class ParentScoreCategoryViewSet(viewsets.ModelViewSet):
    queryset = ParentScoreCategory.objects.all()
    serializer_class = ParentScoreCategoryWriteSerializer

class DivisionGroupViewSet(viewsets.ModelViewSet):
    queryset = DivisionGroup.objects.all()
    serializer_class = DivisionGroupWriteSerializer

class ScoreCategoryViewSet(viewsets.ModelViewSet):
    queryset = ScoreCategory.objects.all()
    serializer_class = ScoreCategoryWriteSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationWriteSerializer

class ScoreSheetViewSet(viewsets.ModelViewSet):
    queryset = ScoreSheet.objects.all()
    serializer_class = ScoreSheetWriteSerializer

class ScoreSheetElementViewSet(viewsets.ModelViewSet):
    queryset = ScoreSheetElement.objects.all()
    serializer_class = ScoreSheetElementWriteSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamWriteSerializer

class UserSkillPermissionViewSet(viewsets.ModelViewSet):
    queryset = UserSkillPermission.objects.all()
    serializer_class = UserSkillPermissionWriteSerializer

class ChampionshipViewSet(viewsets.ModelViewSet):
    queryset = Championship.objects.all()
    serializer_class = ChampionshipWriteSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationWriteSerializer

class UserScoreSheetElementViewSet(viewsets.ModelViewSet):
    queryset = UserScoreSheetElement.objects.all()
    serializer_class = UserScoreSheetElementWriteSerializer

#creación de dashboard

class DashboardViewSet(APIView):

    def get_registrations(self, pk):
        try:
            return Registration.objects.filter(championship__id=pk)
        except Registration.DoesNotExist:
            logger.error("Registration not found")
            raise Http404
    

    def get(self, request, pk, format=None):
        registration = self.get_registrations(pk)
        serializer = RegistrationReadSerializer(registration, many=True)
        return Response(serializer.data)

