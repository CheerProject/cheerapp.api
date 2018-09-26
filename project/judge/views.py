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
from rest_framework.renderers import JSONRenderer
#from .schemas import get_predictor_schema
from decimal import Decimal

import json

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

#done
class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionWriteSerializer

#done
class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderWriteSerializer

#done
class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelWriteSerializer

#done
class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionWriteSerializer

#done
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryWriteSerializer

#done
class RoundViewSet(viewsets.ModelViewSet):
    queryset = Round.objects.all()
    serializer_class = RoundWriteSerializer

#done
class ScoreSheetTypeViewSet(viewsets.ModelViewSet):
    queryset = ScoreSheetType.objects.all()
    serializer_class = ScoreSheetTypeWriteSerializer

#done
class ScoreMetricViewSet(viewsets.ModelViewSet):
    queryset = ScoreMetric.objects.all()
    serializer_class = ScoreMetricWriteSerializer

#done
class LocationTypeViewSet(viewsets.ModelViewSet):
    queryset = LocationType.objects.all()
    serializer_class = LocationTypeWriteSerializer

#done
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusWriteSerializer

#done
class ParentScoreCategoryViewSet(viewsets.ModelViewSet):
    queryset = ParentScoreCategory.objects.all()
    serializer_class = ParentScoreCategoryWriteSerializer

#done
class DivisionGroupViewSet(viewsets.ModelViewSet):
    queryset = DivisionGroup.objects.all()
    serializer_class = DivisionGroupWriteSerializer

#done
class ScoreCategoryViewSet(viewsets.ModelViewSet):
    queryset = ScoreCategory.objects.all()
    serializer_class = ScoreCategoryWriteSerializer

#done
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationWriteSerializer

#done
class ScoreSheetViewSet(viewsets.ModelViewSet):
    queryset = ScoreSheet.objects.all()
    serializer_class = ScoreSheetWriteSerializer

#done
class ScoreSheetElementViewSet(viewsets.ModelViewSet):
    queryset = ScoreSheetElement.objects.all()
    serializer_class = ScoreSheetElementWriteSerializer

#done
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamWriteSerializer

#done
class UserSkillPermissionViewSet(viewsets.ModelViewSet):
    queryset = UserSkillPermission.objects.all()
    serializer_class = UserSkillPermissionWriteSerializer

#done
class ChampionshipViewSet(viewsets.ModelViewSet):
    queryset = Championship.objects.all()
    serializer_class = ChampionshipWriteSerializer

#done
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationWriteSerializer

#done
class UserScoreSheetElementViewSet(viewsets.ModelViewSet):
    queryset = UserScoreSheetElement.objects.all()
    serializer_class = UserScoreSheetElementWriteSerializer

#done
class ChampionshipScoreSheetViewSet(viewsets.ModelViewSet):
    queryset = ChampionshipScoreSheet.objects.all()
    serializer_class = ChampionshipScoreSheetWriteSerializer

#done
class RegistrationRoundViewSet(viewsets.ModelViewSet):
    queryset = RegistrationRound.objects.all()
    serializer_class = RegistrationRoundWriteSerializer

#creación de dashboard

class ScoreSheetUserViewSet(APIView):

    def get_scoresheets_1(self, pk1, pk2):
        try:
            return UserScoreSheetElement.objects.filter(user__id=pk1, registrationround__id=pk2)
        except UserScoreSheetElement.DoesNotExist:
            logger.error("User not found")
            raise Http404

    def get_scoresheets_2(self, pk1, pk2):
        try:
            return UserSkillPermission.objects.filter(user__id=pk1, registrationround__id=pk2)
        except UserSkillPermission.DoesNotExist:
            logger.error("User not found")
            raise Http404


    def get(self, request, pk1, pk2, pk3, format=None):
        #scoresheet = self.get_scoresheets_1(request.user.id, pk3)
        scoresheet = self.get_scoresheets_1(1, pk3)
        serializer = UserScoreSheetElementReadSerializer(scoresheet, many=True)
        
        if (serializer.data == []):
            #scoresheet = self.get_scoresheets_2(request.user.id, pk3)
            scoresheet = self.get_scoresheets_2(1, pk3)
            serializer = UserSkillPermissionReadSerializer(scoresheet, many=True)
            
            for scorecategory in serializer.data:
                scorecategory['value'] = ''
            
        return Response(serializer.data, status=status.HTTP_200_OK)

#done
class TabsViewSet(APIView):

    def get_registrationrounds(self, pk1, pk2):
        try:
            return RegistrationRound.objects.filter(registration__championshipscoresheet__championship__id=pk1, registration__divisiongroup__id=pk2)
        except UserScoreSheetElement.DoesNotExist:
            logger.error("Divsion not found")
    
    def get(self, request, pk1, pk2, format=None):
        registrationrounds = self.get_registrationrounds(pk1, pk2)
        serializer1 = RegistrationRoundReadSerializer(registrationrounds, many=True)
        
        for data in serializer1.data:
            reg_id= data['registration']['id']
            
            userscoresheetelements = self.get_userscoresheetelements(reg_id)
            serializer2 = UserScoreSheetElementWriteSerializer(userscoresheetelements, many=True)

            points = 0
            for metric in serializer2.data:
                she = ScoreSheetElement.objects.get(pk=metric['scoresheetelement'])
                if not (she.scorecategory.name == 'observations'):
                    points = points + float(metric['value'])
                
            data['points'] = points
        return Response(serializer1.data, status=status.HTTP_200_OK)

#done
class DashboardViewSet(APIView):

    def get_registrations(self, pk1):
        try:
            return RegistrationRound.objects.filter(registration__championshipscoresheet__championship__id=pk1)
        except RegistrationRound.DoesNotExist:
            logger.error("Championship not found")
            raise Http404
    

    def get(self, request, pk1, format=None):
        registrations = self.get_registrations(pk1)
        reg_list1 = []
        reg_list2 = set()
        reg_list3 = dict()

        for reg in registrations:
            reg_list1.append(reg.registration.divisiongroup.division)
            reg_list2.add(reg.registration.divisiongroup.division)
            
            participantes = reg_list1.count(reg.registration.divisiongroup.division)
            pendientes = reg_list3.get(reg.registration.divisiongroup.division.name, [0,0,0])[2] + (1 if reg.status.name=='on time' else 0)
            reg_list3[reg.registration.divisiongroup.division.name] = [reg.registration.divisiongroup.division, participantes, pendientes]
        
        serializer = DivisionWriteSerializer(reg_list2, many=True)

        for data in serializer.data:
            name = data['name']
            data['participantes'] = reg_list3[name][1]
            data['pendientes'] = reg_list3[name][2]

        return Response(serializer.data, status=status.HTTP_200_OK)
