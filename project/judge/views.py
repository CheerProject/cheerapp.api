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

#done
class ScoreSheetUserViewSet(APIView):

    def get_user_scoresheet_element(self, pk_user_scoresheet_element):
        try:
            return UserScoreSheetElement.objects.get(pk=pk_user_scoresheet_element)
        except UserScoreSheetElement.DoesNotExist:
            logger.error("Calification not found")
            raise Http404

    def put(self, request, pk_championship, pk_division, pk_registrationround, format=None):
        
        validated = []
        ok_response = []
        errors = []

        for data in request.data:
            
            pk_user_scoresheet_element = data['id']
            user_scoresheet_element = self.get_user_scoresheet_element(pk_user_scoresheet_element)
            user_scoresheet_element.value = data['value']
            
            serializer = UserScoreSheetElementWriteSerializer(user_scoresheet_element, data=data)
            
            if serializer.is_valid():
                validated.append(serializer)
            else:
                errors.append(serializer.errors)
        
        if not errors:
            for serializer in validated:
                instance = serializer.save()
                read_serializer = UserScoreSheetElementReadSerializer(instance)
                ok_response.append(read_serializer.data)
            return Response(ok_response)
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


            

    def post(self, request, pk_championship, pk_division, pk_registrationround, format=None):
        user = User.objects.get(pk=request.user.id)
        #user = User.objects.get(pk=1)
        #registrationround = RegistrationRound.objects.get(pk=pk_registrationround)
        estado = 'delayed' if request.query_params.get('pending') else 'checked'
        bulk = isinstance(request.data, list)
        if bulk:
            serializer = UserScoreSheetElementWriteSerializer(data=request.data, many=True)
            if serializer.is_valid():
                for data in serializer.validated_data:
                    data['user'] = user
                instance = serializer.save()
                read_serializer = UserScoreSheetElementReadSerializer(instance, many=True)

                RegistrationRound.objects.filter(pk=pk3).update(status = Status.objects.get(name=estado))
                
                return Response(read_serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserScoreSheetElementWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = user
            instance = serializer.save()
            read_serializer = UserScoreSheetElementReadSerializer(instance)

            RegistrationRound.objects.filter(pk=pk3).update(status = Status.objects.get(name=estado))

            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_scoresheets_1(self, pk_user, pk_registrationround):
        try:
            return UserScoreSheetElement.objects.filter(user__id=pk_user, registrationround__id=pk_registrationround)
        except UserScoreSheetElement.DoesNotExist:
            logger.error("User not found")
            raise Http404

    def get_scoresheets_2(self, pk_user, pk_registrationround):
        try:
            return UserSkillPermission.objects.filter(user__id=pk_user, registrationround__id=pk_registrationround)
        except UserSkillPermission.DoesNotExist:
            logger.error("User not found")
            raise Http404

    def get(self, request, pk_championship, pk_division, pk_registrationround, format=None):
        
        scoresheet = self.get_scoresheets_1(request.user.id, pk_registrationround)
        #scoresheet = self.get_scoresheets_1(1, pk_registrationround)
        serializer = UserScoreSheetElementReadSerializer(scoresheet, many=True)
        
        if not serializer.data:
            scoresheet = self.get_scoresheets_2(request.user.id, pk_registrationround)
            #scoresheet = self.get_scoresheets_2(1, pk_registrationround)
            serializer = UserSkillPermissionReadSerializer(scoresheet, many=True)
            
            for scorecategory in serializer.data:
                scorecategory['value'] = ''
            
        return Response(serializer.data, status=status.HTTP_200_OK)

#done
class TabsWriteViewSet(APIView):
    
    def put(self, request, pk_championship, pk_division, pk_registrationround, format=None):
       estado = 'delayed' if request.query_params.get('pending') else 'on time'
       registrationround = RegistrationRound.objects.filter(pk=pk_registrationround).update(status = Status.objects.get(name=estado))
       serializer = RegistrationRoundReadSerializer(registrationround)
       return Response(serializer.data)

#done
class TabsReadViewSet(APIView):

    def get_registrationrounds(self, pk_championship, pk_division):
        try:
            return RegistrationRound.objects.filter(registration__championshipscoresheet__championship__id=pk_championship, registration__divisiongroup__division__id=pk_division)
        except RegistrationRound.DoesNotExist:
            logger.error("Divsion not found")

    def get_userscoresheetelements(self, pk_user, pk_division):
        try:
            return UserScoreSheetElement.objects.filter(user__id=pk_user, registrationround_id=pk_division)
        except UserScoreSheetElement.DoesNotExist:
            logger.error("User not found")
    
    def get(self, request, pk_championship, pk_division, format=None):
        registrationrounds = self.get_registrationrounds(pk_championship, pk_division)
        
        serializer1 = RegistrationRoundReadSerializer(registrationrounds, many=True)
        
        for data in serializer1.data:
            reg_id= data['id']
            print(reg_id)
            userscoresheetelements = self.get_userscoresheetelements(request.user.id, reg_id)
            #userscoresheetelements = self.get_userscoresheetelements(1, reg_id)
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

    def get_registrations(self, pk_championship):
        try:
            return RegistrationRound.objects.filter(registration__championshipscoresheet__championship__id=pk_championship)
        except RegistrationRound.DoesNotExist:
            logger.error("Championship not found")
            raise Http404
    

    def get(self, request, pk_championship, format=None):
        registrations = self.get_registrations(pk_championship)
        registration_list1 = []
        registration_list2 = set()
        registration_list3 = dict()

        for registration in registrations:
            registration_list1.append(registration.registration.divisiongroup.division)
            registration_list2.add(registration.registration.divisiongroup.division)
            
            participantes = registration_list1.count(registration.registration.divisiongroup.division)
            pendientes = registration_list3.get(registration.registration.divisiongroup.division.name, [0,0,0])[2] + (1 if registration.status.name=='on time' else 0)
            registration_list3[registration.registration.divisiongroup.division.name] = [registration.registration.divisiongroup.division, participantes, pendientes]
        
        serializer = DivisionWriteSerializer(registration_list2, many=True)

        for data in serializer.data:
            name = data['name']
            data['participantes'] = registration_list3[name][1]
            data['pendientes'] = registration_list3[name][2]

        return Response(serializer.data, status=status.HTTP_200_OK)
