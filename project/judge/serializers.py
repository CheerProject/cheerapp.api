from rest_framework import serializers
from project.judge.models import ParentScoreCategory
from project.judge.models import ScoreCategory
from project.judge.models import ScoreMetric
from project.judge.models import Level
from project.judge.models import Team
from project.judge.models import Round
from project.judge.models import Championship
from project.judge.models import Registration
from project.judge.models import UserScoreCategoryChampionship
from project.judge.models import ScoreSheet


class ScoreSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScoreSheet
        fields = ('id', 'min_score', 'max_score', 'score', 'championship', 'round', 'team', 'scorecategory', 'scoremetric', 'user')
        required_fields = ('min_score', 'max_score', 'score')
        read_only_fields = ('championship', 'round', 'team', 'scorecategory', 'scoremetric', 'user')

class UserScoreCategoryChampionshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserScoreCategoryChampionship
        fields = ('id', 'user', 'scorecategory', 'championship')
        read_only_fields = ('user', 'scorecategory', 'championship')

class ScoreCategorySerializer(serializers.ModelSerializer):
    user_score_category_championships = UserScoreCategoryChampionshipSerializer(many=True)
    score_sheets = ScoreSheetSerializer(many=True)

    class Meta:
        model = ScoreCategory
        fields = ('id', 'name', 'description', 'parentscorecategory', 'user_score_category_championships', 'score_sheets')
        required_fields = ('name', 'description')
        read_only_fields = ('parentscorecategory', 'user_score_category_championships', 'score_sheets')

class ParentScoreCategorySerializer(serializers.ModelSerializer):
    score_categories = ScoreCategorySerializer(many=True)
    
    class Meta:
        model = ParentScoreCategory
        fields = ('id', 'name', 'description', 'score_categories')
        required_fields = ('name', 'description')
        read_only_fields = ('score_categories')

class ScoreMetricSerializer(serializers.ModelSerializer):
    score_sheets = ScoreSheetSerializer(many=True)
    
    class Meta:
        model = ScoreMetric
        fields = ('id', 'name', 'description', 'score_sheets')
        required_fields = ('name', 'description')
        read_only_fields = ('score_sheets')

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = ('id', 'date', 'championship', 'team')
        required_fields = ('date')
        read_only_fields = ('championship', 'team')

class TeamSerializer(serializers.ModelSerializer):
    registrations = RegistrationSerializer(many=True)
    score_sheets = ScoreSheetSerializer(many=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'total_men', 'total_women', 'coach', 'description', 'level', 'registrations', 'score_sheets')
        required_fields = ('name', 'total_men', 'total_women', 'coach', 'description')
        read_only_fields = ('level', 'registrations', 'score_sheets')

class LevelSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True)

    class Meta:
        model = Level
        fields = ('id', 'name', 'description', 'teams')
        required_fields = ('name', 'description')
        read_only_fields = ('teams')

class RoundSerializer(serializers.ModelSerializer):
    score_sheets = ScoreSheetSerializer(many=True)

    class Meta:
        model = Round
        fields = ('id', 'name', 'description', 'score_sheets')
        required_fields = ('name', 'description')
        read_only_fields = ('score_sheets')

class ChampionshipSerializer(serializers.ModelSerializer):
    registrations = RegistrationSerializer(many=True)
    user_score_category_championships = UserScoreCategoryChampionshipSerializer(many=True)
    score_sheets = ScoreSheetSerializer(many=True)
    
    class Meta:
        model = Championship
        fields = ('id', 'name', 'date', 'address', 'description', 'registrations', 'user_score_category_championships', 'score_sheets')
        required_fields = ('name', 'date', 'address', 'description')
        read_only_fields = ('registrations', 'user_score_category_championships', 'score_sheets')
