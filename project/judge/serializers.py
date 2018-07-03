'''
from rest_framework import serializers
from project.api_auth.serializers import UserSerializer
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
    ScoreSheet,
    UserScoreSheet
)

#done
class GenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ('id', 'name')
        required_fields = ('name')
#done
class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ('id', 'name')
        required_fields = ('name')
#done
class DivisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ('id', 'name')
        required_fields = ('name')
#done
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ('id', 'name')
        required_fields = ('name')
#done
class RoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Round
        fields = ('id', 'name')
        required_fields = ('name')
#done
class ScoreMetricSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ScoreMetric
        fields = ('id', 'name')
        required_fields = ('name')
##############################################################################done
#done
class UserScoreSheetSerializer(serializers.ModelSerializer):
    round = RoundSerializer(many=False)
    #registration = RegistrationSerializer(many=False)
    user = UserSerializer(many=False)
    #scoreSheet = ScoreSheetSerializer(many=False)

    class Meta:
        model = UserScoreSheet
        fields = ('id', 'score', 'round', 'registration', 'user', 'scoresheet')
        required_fields = ('score', 'round', 'registration', 'user', 'scoresheet')
#done
class RegistrationSerializer(serializers.ModelSerializer):
    gender = GenderSerializer(many=False)
    level = LevelSerializer(many=False)
    division = DivisionSerializer(many=False)
    category = CategorySerializer(many=False)

    user_score_sheets = UserScoreSheetSerializer(many=True)

    class Meta:
        model = Registration
        fields = ('id', 'date', 'gender', 'level', 'division', 'category', 'team', 'user_score_sheets')
        required_fields = ('gender', 'level', 'division', 'category', 'team')
        read_only_fields = ('user_score_sheets')
#done
class TeamSerializer(serializers.ModelSerializer):
    registrations = RegistrationSerializer(many=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'total_men', 'total_women', 'coach', 'registrations')
        required_fields = ('name')
        read_only_fields = ('registrations')
#done
class ScoreSheetSerializer(serializers.ModelSerializer):
    scoremetric = ScoreMetricSerializer(many=False)
    championship = ChampionshipSerializer(many=False)
    scorecategory = ScoreCategorySerializer(many=False)

    user_score_sheets = UserScoreSheetSerializer(many=True)

    class Meta:
        model = ScoreSheet
        fields = ('id', 'min_score', 'max_score', 'scoremetric', 'championship', 'scorecategory')
        required_fields = ('min_score', 'max_score', 'scoremetric', 'championship', 'scorecategory')
#done
class ScoreCategorySerializer(serializers.ModelSerializer):
    parentscorecategory = ParentScoreCategorySerializer(many=False)
    
    user_score_categories = UserScoreCategorySerializer(many=True)
    score_sheets = ScoreSheetSerializer(many=True)

    class Meta:
        model = ScoreCategory
        fields = ('id', 'name', 'parentscorecategory', 'user_score_categories', 'score_sheets')
        required_fields = ('name', 'parentscorecategory')
        read_only_fields = ('user_score_categories', 'score_sheets')
#done
class UserScoreCategorySerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    scorecategory = ScoreCategorySerializer(many=False)
    
    class Meta:
        model = UserScoreCategory
        fields = ('id', 'user', 'scorecategory')
        required_fields = ('user', 'scorecategory')
#done
class ParentScoreCategorySerializer(serializers.ModelSerializer):
    score_categories = ScoreCategorySerializer(many=True)
    
    class Meta:
        model = ParentScoreCategory
        fields = ('id', 'name', 'score_categories')
        required_fields = ('name')
        read_only_fields = ('score_categories')
#done
class ChampionshipSerializer(serializers.ModelSerializer):
    score_sheets = ScoreSheetSerializer(many=True)
    
    class Meta:
        model = Championship
        fields = ('id', 'name', 'date', 'address', 'score_sheets')
        required_fields = ('name')
        read_only_fields = ('score_sheets')
'''
