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
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupWriteSerializer

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
class UserRegistrationRoundViewSet(viewsets.ModelViewSet):
    queryset = UserRegistrationRound.objects.all()
    serializer_class = UserRegistrationRoundWriteSerializer

class ChampOfChampsViewSet(APIView):

    def get_status(self, status_name):
        try:
            return Status.objects.get(name=status_name)
        except Status.DoesNotExist:
            logger.error("Status not found")
    
    def get_scoresheet_element(self, pk_scoresheetelement):
        try:
            return ScoreSheetElement.objects.get(pk=pk_scoresheetelement)
        except ScoreSheetElement.DoesNotExist:
            logger.error("ScoreSheetElement not found")
    
    def get_registrations(self, pk_championship):
        try:
            return Registration.objects.filter(championshipscoresheet__championship__id=pk_championship)
        except Registration.DoesNotExist:
            logger.error("Registration not found")
            raise Http404

    def get_user_scoresheet_elements(self, pk_userregistrationround):
        try:
            return UserScoreSheetElement.objects.filter(userregistrationround__id=pk_userregistrationround)
        except UserScoreSheetElement.DoesNotExist:
            logger.error("UserScoreSheetElement not found")

    def get_user_registration_rounds(self, pk_registration, pk_status, is_active):
        try:
            return UserRegistrationRound.objects.filter(registration__id=pk_registration, status__id=pk_status, is_active=is_active)
        except Registration.DoesNotExist:
            logger.error("Registration not found")
            raise Http404
    
    def get(self, request, pk_championship, format=None):
        pk_status = self.get_status("checked").id
        
        registrations = self.get_registrations(pk_championship)
        serializer_registrations = RegistrationWriteSerializer(registrations, many=True)
        
        for registration in serializer_registrations.data:
            pk_registration = registration['id']
            
            userregistrationrounds = self.get_user_registration_rounds(pk_registration, pk_status, True)
            serializer_userregistrationrounds = UserRegistrationRoundWriteSerializer(userregistrationrounds, many=True)
            
            points = 0
            for userregistrationround in serializer_userregistrationrounds.data:
                pk_userregistrationround = userregistrationround['id']
                
                userscoresheetelements = self.get_user_scoresheet_elements(pk_userregistrationround)
                serializer_userscoresheetelements = UserScoreSheetElementWriteSerializer(userscoresheetelements, many=True)

                for userscoresheetelement in serializer_userscoresheetelements.data:
                    pk_scoresheetelement = userscoresheetelement['scoresheetelement']
                    scoresheetelement = self.get_scoresheet_element(pk_scoresheetelement)

                    if not (scoresheetelement.scorecategory.name == 'observations'):
                        points = points + float(userscoresheetelement['value'])
            
            registration['points'] = points
            print(sorted(serializer_registrations.data, key=lambda points: serializer_registrations.data['points']))
        return Response(serializer_registrations.data, status=status.HTTP_200_OK)

class LeaderBoardViewSet(APIView):

    def get_status(self, status_name):
        try:
            return Status.objects.get(name=status_name)
        except Status.DoesNotExist:
            logger.error("Status not found")
    
    def get_scoresheet_element(self, pk_scoresheetelement):
        try:
            return ScoreSheetElement.objects.get(pk=pk_scoresheetelement)
        except ScoreSheetElement.DoesNotExist:
            logger.error("ScoreSheetElement not found")
    
    def get_registrations(self, pk_championship, pk_division):
        try:
            return Registration.objects.filter(division_id=pk_division, championshipscoresheet__championship__id=pk_championship)
        except Registration.DoesNotExist:
            logger.error("Registration not found")
            raise Http404

    def get_user_scoresheet_elements(self, pk_userregistrationround):
        try:
            return UserScoreSheetElement.objects.filter(userregistrationround__id=pk_userregistrationround)
        except UserScoreSheetElement.DoesNotExist:
            logger.error("UserScoreSheetElement not found")

    def get_user_registration_rounds(self, pk_registration, pk_status, is_active):
        try:
            return UserRegistrationRound.objects.filter(registration__id=pk_registration, status__id=pk_status, is_active=is_active)
        except Registration.DoesNotExist:
            logger.error("Registration not found")
            raise Http404
    
    def get(self, request, pk_championship, pk_division, format=None):
        pk_status = self.get_status("checked").id
        
        registrations = self.get_registrations(pk_championship, pk_division)
        serializer_registrations = RegistrationWriteSerializer(registrations, many=True)
        
        for registration in serializer_registrations.data:
            pk_registration = registration['id']
            
            userregistrationrounds = self.get_user_registration_rounds(pk_registration, pk_status, True)
            serializer_userregistrationrounds = UserRegistrationRoundWriteSerializer(userregistrationrounds, many=True)
            
            points = 0
            for userregistrationround in serializer_userregistrationrounds.data:
                pk_userregistrationround = userregistrationround['id']
                
                userscoresheetelements = self.get_user_scoresheet_elements(pk_userregistrationround)
                serializer_userscoresheetelements = UserScoreSheetElementWriteSerializer(userscoresheetelements, many=True)

                for userscoresheetelement in serializer_userscoresheetelements.data:
                    pk_scoresheetelement = userscoresheetelement['scoresheetelement']
                    scoresheetelement = self.get_scoresheet_element(pk_scoresheetelement)

                    if not (scoresheetelement.scorecategory.name == 'observations'):
                        points = points + float(userscoresheetelement['value'])
            
            registration['points'] = points
        return Response(serializer_registrations.data, status=status.HTTP_200_OK)

#done
class ScoreSheetUserViewSet(APIView):

    def get_user_scoresheet_element(self, pk_scoresheet_element, pk_userregistrationround):
        try:
            return UserScoreSheetElement.objects.get(scoresheetelement__id=pk_scoresheet_element, userregistrationround__id=pk_userregistrationround)
        except UserScoreSheetElement.DoesNotExist:
            logger.error("Calification not found")
            raise Http404

    def put(self, request, pk_championship, pk_division, pk_userregistrationround, format=None):
        
        validated = []
        ok_response = []
        errors = []

        for data in request.data:
            pk_scoresheet_element = data['scoresheetelement']
            user_scoresheet_element = self.get_user_scoresheet_element(pk_scoresheet_element, pk_userregistrationround)
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

    def post(self, request, pk_championship, pk_division, pk_userregistrationround, format=None):
        
        estado = 'delayed' if request.query_params.get('pending') else 'checked'
        serializer = UserScoreSheetElementWriteSerializer(data=request.data, many=True)
        if serializer.is_valid():
            for data in serializer.validated_data:
                data['userregistrationround'] = UserRegistrationRound.objects.get(pk=pk_userregistrationround)
            instance = serializer.save()
            read_serializer = UserScoreSheetElementReadSerializer(instance, many=True)
            UserRegistrationRound.objects.filter(pk=pk_userregistrationround).update(status = Status.objects.get(name=estado))
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_scoresheets_user_scoresheet_element(self, pk_userregistrationround):
        try:
            return UserScoreSheetElement.objects.filter(userregistrationround__id=pk_userregistrationround)
        except UserScoreSheetElement.DoesNotExist:
            logger.error("User not found")
            raise Http404

    def get_scoresheets_user_skill_permission(self, pk_userregistrationround):
        try:
            return UserSkillPermission.objects.filter(userregistrationround__id=pk_userregistrationround)
        except UserSkillPermission.DoesNotExist:
            logger.error("User not found")
            raise Http404

    def get(self, request, pk_championship, pk_division, pk_userregistrationround, format=None):
        
        #scoresheet = self.get_scoresheets_userscoresheetelement(pk_userregistrationround)
        scoresheet = self.get_scoresheets_user_scoresheet_element(pk_userregistrationround)
        serializer = UserScoreSheetElementReadSerializer(scoresheet, many=True)
        
        if not serializer.data:
            #scoresheet = self.get_scoresheets_userskillpermission(pk_userregistrationround)
            scoresheet = self.get_scoresheets_user_skill_permission(pk_userregistrationround)
            serializer = UserSkillPermissionReadSerializer(scoresheet, many=True)
            
            for scorecategory in serializer.data:
                scorecategory['value'] = ''
            
        return Response(serializer.data, status=status.HTTP_200_OK)

#done
class TabsWriteViewSet(APIView):

    def get_status(self, status_name):
        try:
            return Status.objects.get(name=status_name)
        except Status.DoesNotExist:
            logger.error("Status not found")

    def get_user_registration_round(self, pk_userregistrationround):
        try:
            return UserRegistrationRound.objects.get(pk=pk_userregistrationround)
        except UserRegistrationRound.DoesNotExist:
            logger.error("UserRegistrationRound not found")
    
    def put(self, request, pk_championship, pk_division, pk_userregistrationround, format=None):
       estado = 'delayed' if request.query_params.get('pending') else 'on time'
       print(estado)
       userregistrationround = self.get_user_registration_round(pk_userregistrationround)
       userregistrationround.status = self.get_status(estado)
       serializer = UserRegistrationRoundReadSerializer(userregistrationround)
       return Response(serializer.data)

#done
class TabsReadViewSet(APIView):

    def get_user_registration_rounds(self, pk_championship, pk_division, pk_user, is_active):
        try:
            return UserRegistrationRound.objects.filter(registration__championshipscoresheet__championship__id=pk_championship, registration__division__id=pk_division, user__id=pk_user, is_active=is_active)
        except UserRegistrationRound.DoesNotExist:
            logger.error("Divsion not found")

    def get_user_scoresheet_elements(self, pk_userregistrationround):
        try:
            return UserScoreSheetElement.objects.filter(userregistrationround_id=pk_userregistrationround)
        except UserScoreSheetElement.DoesNotExist:
            logger.error("User not found")
    
    def get(self, request, pk_championship, pk_division, format=None):
        #userregistrationrounds = self.get_user_registration_rounds(pk_championship, pk_division, request.user.id, True)
        userregistrationrounds = self.get_user_registration_rounds(pk_championship, pk_division, 1, True)
        
        serializer1 = UserRegistrationRoundReadSerializer(userregistrationrounds, many=True)
        
        for data in serializer1.data:
            userregistrationround_id = data['id']
            userscoresheetelements = self.get_user_scoresheet_elements(userregistrationround_id)
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

    def get_user_registration_rounds(self, pk_championship):
        try:
            return UserRegistrationRound.objects.filter(registration__championshipscoresheet__championship__id=pk_championship)
        except UserRegistrationRound.DoesNotExist:
            logger.error("Championship not found")
            raise Http404
    

    def get(self, request, pk_championship, format=None):
        userregistrationrounds = self.get_user_registration_rounds(pk_championship)
        registration_list1 = []
        registration_list2 = set()
        registration_list3 = dict()

        for userregistrationround in userregistrationrounds:
            registration_list1.append(userregistrationround.registration.division)
            registration_list2.add(userregistrationround.registration.division)
            
            participantes = registration_list1.count(userregistrationround.registration.division)
            pendientes = registration_list3.get(userregistrationround.registration.division.name, [0,0,0])[2] + (1 if userregistrationround.status.name=='on time' else 0)
            registration_list3[userregistrationround.registration.division.name] = [userregistrationround.registration.division, participantes, pendientes]
        
        serializer = DivisionWriteSerializer(registration_list2, many=True)

        for data in serializer.data:
            name = data['name']
            data['participantes'] = registration_list3[name][1]
            data['pendientes'] = registration_list3[name][2]

        return Response(serializer.data, status=status.HTTP_200_OK)
