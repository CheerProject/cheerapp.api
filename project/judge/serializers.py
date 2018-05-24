from rest_framework import serializers
from .models import (
    ParentScoreCategory,
    Round,
    ScoreMetric,
    Championship,
    Gender,
    Level,
    Division,
    Category,
    Team,
    ScoreCategory,
    UserScoreCategory,
    Registration,
    ScoreSheet
)


class ScoreSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScoreSheet
        fields = ('id', 'min_score', 'max_score', 'score', 'round', 'scoremetric', 'registration', 'championship', 'user', 'scorecategory')
        required_fields = ('score', 'round', 'scoremetric', 'registration', 'championship', 'user', 'scorecategory')

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = ('id', 'date', 'gender', 'level', 'division', 'category', 'team')
        required_fields = ('gender', 'level', 'division', 'category', 'team')

class UserScoreCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserScoreCategory
        fields = ('id', 'user', 'scorecategory')
        required_fields = ('user', 'scorecategory')

class ScoreCategorySerializer(serializers.ModelSerializer):
    user_score_categories = UserScoreCategorySerializer(many=True)
    score_sheets = ScoreSheetSerializer(many=True)

    class Meta:
        model = ScoreCategory
        fields = ('id', 'name', 'parentscorecategory', 'user_score_categories', 'score_sheets')
        required_fields = ('name', 'parentscorecategory', 'user_score_categories', 'score_sheets')

class ParentScoreCategorySerializer(serializers.ModelSerializer):
    score_categories = ScoreCategorySerializer(many=True)
    
    class Meta:
        model = ParentScoreCategory
        fields = ('id', 'name', 'score_categories')
        required_fields = ('name', 'score_categories')

class RoundSerializer(serializers.ModelSerializer):
    score_sheets = ScoreSheetSerializer(many=True)

    class Meta:
        model = Round
        fields = ('id', 'name', 'score_sheets')
        required_fields = ('name', 'score_sheets')

class ScoreMetricSerializer(serializers.ModelSerializer):
    score_sheets = ScoreSheetSerializer(many=True)
    
    class Meta:
        model = ScoreMetric
        fields = ('id', 'name', 'score_sheets')
        required_fields = ('name', 'score_sheets')

class ChampionshipSerializer(serializers.ModelSerializer):
    score_sheets = ScoreSheetSerializer(many=True)
    
    class Meta:
        model = Championship
        fields = ('id', 'name', 'date', 'address', 'score_sheets')
        required_fields = ('name', 'score_sheets')

class GenderSerializer(serializers.ModelSerializer):
    registrations = RegistrationSerializer(many=True)

    class Meta:
        model = Level
        fields = ('id', 'name', 'registrations')
        required_fields = ('name', 'registrations')

class LevelSerializer(serializers.ModelSerializer):
    registrations = RegistrationSerializer(many=True)

    class Meta:
        model = Level
        fields = ('id', 'name', 'registrations')
        required_fields = ('name', 'registrations')

class DivisionSerializer(serializers.ModelSerializer):
    registrations = RegistrationSerializer(many=True)

    class Meta:
        model = Level
        fields = ('id', 'name', 'registrations')
        required_fields = ('name', 'registrations')

class CategorySerializer(serializers.ModelSerializer):
    registrations = RegistrationSerializer(many=True)

    class Meta:
        model = Level
        fields = ('id', 'name', 'registrations')
        required_fields = ('name', 'registrations')

class TeamSerializer(serializers.ModelSerializer):
    registrations = RegistrationSerializer(many=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'total_men', 'total_women', 'coach', 'registrations')
        required_fields = ('name', 'registrations')
