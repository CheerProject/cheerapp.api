
from rest_framework import serializers

from ..api_auth.serializers import (
    UserSerializer
)

from .models import (
    Institution,
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

#Los write serializers

#done
class InstitutionWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = ('id', 'name')
        required_fields = ('name')

#done
class GenderWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gender
        fields = ('id', 'name')
        required_fields = ('name')

#done
class LevelWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ('id', 'name')
        required_fields = ('name')

#done
class DivisionWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Division
        fields = ('id', 'name')
        required_fields = ('name')

#done
class CategoryWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')
        required_fields = ('name')

#done
class GroupWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name')
        required_fields = ('name')

#done
class RoundWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Round
        fields = ('id', 'name')
        required_fields = ('name')

#done
class ScoreSheetTypeWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScoreSheetType
        fields = ('id', 'name')
        required_fields = ('name')

#done
class ScoreMetricWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ScoreMetric
        fields = ('id', 'name')
        required_fields = ('name')

#done
class LocationTypeWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LocationType
        fields = ('id', 'name')
        required_fields = ('name')

#done
class StatusWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Status
        fields = ('id', 'name')
        required_fields = ('name')

#done
class ParentScoreCategoryWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParentScoreCategory
        fields = ('id', 'name')
        required_fields = ('name')

#done
class DivisionGroupWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = DivisionGroup
        fields = ('id', 'gender', 'level', 'division', 'category', 'group', 'institution')
        required_fields = ('gender', 'level', 'division', 'caegory', 'group', 'institution')

#done
class ScoreCategoryWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScoreCategory
        fields = ('id', 'name', 'parentscorecategory')
        required_fields = ('name', 'parentscorecategory')

#done
class LocationWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('id', 'name', 'locationtype', 'location')
        required_fields = ('name', 'locationtype', 'location')

#done
class ScoreSheetWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScoreSheet
        fields = ('id', 'name', 'scoresheettype')
        required_fields = ('name', 'scoresheettype')

#done
class ScoreSheetElementWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ScoreSheetElement
        fields = ('id', 'min_score', 'max_score', 'scoremetric', 'scorecategory', 'scoresheet')
        required_fields = ('min_score', 'max_score', 'scoremetric', 'scorecategory', 'scoresheet')

#done
class TeamWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('id', 'name', 'location')
        required_fields = ('name', 'location')

#done
class UserSkillPermissionWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSkillPermission
        fields = ('id', 'user', 'scorecategory')
        required_fields = ('user', 'scorecategory')

#done
class ChampionshipWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Championship
        fields = ('id', 'name', 'date', 'address', 'scoresheet')
        required_fields = ('name', 'date', 'address', 'scoresheet')


#done
class RegistrationWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = ('id', 'date', 'total_men', 'total_women', 'coach', 'team', 'championship', 'divisiongroup', 'status', 'order')
        required_fields = ('date', 'total_men', 'total_women', 'coach', 'team', 'championship', 'divisiongroup', 'status', 'order')

#done
class UserScoreSheetElementWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserScoreSheetElement
        fields = ('id', 'score', 'completed', 'registration', 'scoresheetelement', 'user', 'round')
        required_fields = ('score', 'completed', 'registration', 'scoresheetelement', 'user', 'round')

#Los read serializers

class ScoreSheetReadSerializer(ScoreSheetWriteSerializer):
    scoresheettype = ScoreSheetTypeWriteSerializer(read_only=True)

class ChampionshipReadSerializer(ChampionshipWriteSerializer):
    scoresheet = ScoreSheetReadSerializer(read_only=True)

class LocationReadSerializer(LocationWriteSerializer):
    locationtype = LocationTypeWriteSerializer(read_only=True)

class TeamReadSerializer(TeamWriteSerializer):
    location = LocationReadSerializer(read_only=True)

class DivisionGroupReadSerializer(DivisionGroupWriteSerializer):
    gender = GenderWriteSerializer(read_only=True)
    level = LevelWriteSerializer(read_only=True)
    division = DivisionWriteSerializer(read_only=True)
    category = CategoryWriteSerializer(read_only=True)
    group = GroupWriteSerializer(read_only=True)

class RegistrationReadSerializer(RegistrationWriteSerializer):
    team = TeamReadSerializer(read_only=True)
    championship = ChampionshipReadSerializer(read_only=True)
    divisiongroup = DivisionGroupReadSerializer(read_only=True)
    status = StatusWriteSerializer(read_only=True)