
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
    UserScoreSheetElement,
    Registration,
    ScoreSheet,
    UserSkillPermission,
    ScoreSheetType
)

#done
class GenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gender
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
        model = Division
        fields = ('id', 'name')
        required_fields = ('name')

#done
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
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

#done
class UserScoreSheetElementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserScoreSheetElement
        fields = ('id', 'score', 'completed')
        required_fields = ('score', 'completed')

#done
class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = ('id', 'date')
        required_fields = ('date')

#done
class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('id', 'name', 'total_men', 'total_women', 'coach')
        required_fields = ('name')

#done
class ScoreSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScoreSheet
        fields = ('id', 'name')
        required_fields = ('name')

#done
class ScoreSheetTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScoreSheetType
        fields = ('id', 'name')
        required_fields = ('name')

#done
class ScoreCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ScoreCategory
        fields = ('id', 'name')
        required_fields = ('name')

#done
class UserSkillPermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSkillPermission
        fields = ('id')

#done
class ParentScoreCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParentScoreCategory
        fields = ('id', 'name')
        required_fields = ('name')

#done
class ChampionshipSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Championship
        fields = ('id', 'name', 'date', 'address')
        required_fields = ('name')
