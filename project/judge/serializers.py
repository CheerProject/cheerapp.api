
from rest_framework import serializers

from ..api_auth.serializers import (
    UserSerializer
)
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
    ScoreSheetType,
    Group,
    DivisionGroup,
    Status,
    LocationType,
    Location,
    ScoreSheetElement
)

#done
class GenderReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gender
        fields = ('id', 'name')
        required_fields = ('name')

#done
class LevelReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ('id', 'name')
        required_fields = ('name')

#done
class DivisionReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Division
        fields = ('id', 'name')
        required_fields = ('name')

#done
class CategoryReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')
        required_fields = ('name')

#done
class GroupReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name')
        required_fields = ('name')

#done
class RoundReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Round
        fields = ('id', 'name')
        required_fields = ('name')

#done
class ScoreSheetTypeReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScoreSheetType
        fields = ('id', 'name')
        required_fields = ('name')

#done
class ScoreMetricReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ScoreMetric
        fields = ('id', 'name')
        required_fields = ('name')

#done
class LocationTypeReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LocationType
        fields = ('id', 'name')
        required_fields = ('name')

#done
class StatusReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Status
        fields = ('id', 'name')
        required_fields = ('name')

#done
class ParentScoreCategoryReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParentScoreCategory
        fields = ('id', 'name')
        required_fields = ('name')

#done
class DivisionGroupReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = DivisionGroup
        fields = ('id', 'gender', 'level', 'division', 'category', 'group')
        required_fields = ('gender', 'level', 'division', 'caegory', 'group')

#done
class ScoreCategoryReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScoreCategory
        fields = ('id', 'name', 'parentscorecategory')
        required_fields = ('name', 'parentscorecategory')

#done
class LocationReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('id', 'name', 'locationtype', 'location')
        required_fields = ('name', 'locationtype', 'location')

#done
class ScoreSheetReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScoreSheet
        fields = ('id', 'name', 'scoresheettype')
        required_fields = ('name', 'scoresheettype')

#done
class ScoreSheetElementReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ScoreSheetElement
        fields = ('id', 'min_score', 'max_score', 'scoremetric', 'scorecategory', 'scoresheet')
        required_fields = ('min_score', 'max_score', 'scoremetric', 'scorecategory', 'scoresheet')

#done
class TeamReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('id', 'name', 'location')
        required_fields = ('name', 'location')

#done
class UserSkillPermissionReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSkillPermission
        fields = ('id', 'user', 'scorecategory')
        required_fields = ('user', 'scorecategory')

#done
class ChampionshipReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Championship
        fields = ('id', 'name', 'date', 'address', 'scoresheet')
        required_fields = ('name', 'date', 'address', 'scoresheet')

#done
class RegistrationReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = ('id', 'date', 'total_men', 'total_women', 'coach', 'team', 'championship', 'divisiongroup', 'status')
        required_fields = ('date', 'total_men', 'total_women', 'coach', 'team', 'championship', 'divisiongroup', 'status')

#done
class UserScoreSheetElementReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserScoreSheetElement
        fields = ('id', 'score', 'completed', 'registration', 'scoresheetelement', 'user', 'round')
        required_fields = ('score', 'completed', 'registration', 'scoresheetelement', 'user', 'round')