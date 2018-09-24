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

import json

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionWriteSerializer

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

class TabsViewSet(APIView):

    def get_registrations(self, pk1, pk2):
        try:
            return Registration.objects.filter(championship__id=pk1, divisiongroup__division__id=pk2)
        except Registration.DoesNotExist:
            logger.error("Division not found")
            raise Http404
    
    def get(self, request, pk1, pk2, format=None):
        registrations = self.get_registrations(pk1, pk2)
        serializer = RegistrationReadSerializer(registrations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DashboardViewSet(APIView):

    def get_registrations(self, pk1):
        try:
            return Registration.objects.filter(championship__id=pk1)
        except Registration.DoesNotExist:
            logger.error("Championship not found")
            raise Http404
    

    def get(self, request, pk1, format=None):
        registrations = self.get_registrations(pk1)
        reg_list1 = []
        reg_list2 = set()
        reg_list3 = dict()

        for reg in registrations:
            reg_list1.append(reg.divisiongroup.division)
            reg_list2.add(reg.divisiongroup.division)
            
            participantes = reg_list1.count(reg.divisiongroup.division)
            pendientes = reg_list3.get(reg.divisiongroup.division.name, [0,0,0])[2] + (1 if reg.status.name=='on time' else 0)
            reg_list3[reg.divisiongroup.division.name] = [reg.divisiongroup.division, participantes, pendientes]
        
        serializer = DivisionWriteSerializer(reg_list2, many=True)

        for data in serializer.data:
            name = data['name']
            data['participantes'] = reg_list3[name][1]
            data['pendientes'] = reg_list3[name][2]

        return Response(serializer.data, status=status.HTTP_200_OK)



