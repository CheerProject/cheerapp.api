
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
    DivisionGroup,
    Status,
    LocationType,
    Location,
    ScoreSheetElement,
    ChampionshipScoreSheet,
    UserRegistrationRound
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
        fields = ('id', 'gender', 'level', 'division', 'category', 'institution')
        required_fields = ('gender', 'level', 'division', 'caegory', 'institution')

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
        #fields = ('id', 'scoresheetelement', 'userregistrationround')
        fields = ('id', 'scoresheetelement')
        #required_fields = ('scoresheetelement', 'userregistrationround')
        required_fields = ('scoresheetelement')

#done
class ChampionshipScoreSheetWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChampionshipScoreSheet
        fields = ('id', 'championship', 'scoresheet')
        required_fields = ('championship', 'scoresheet')

#done
class ChampionshipWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Championship
        fields = ('id', 'name', 'date', 'address')
        required_fields = ('name', 'date', 'address')

#done
class RegistrationWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = ('id', 'total_men', 'total_women', 'coach', 'team', 'championshipscoresheet', 'divisiongroup', 'order')
        required_fields = ('date', 'total_men', 'total_women', 'coach', 'team', 'championshipscoresheet', 'divisiongroup', 'order')
        extra_kwargs = {
            'date': {'write_only': True}
        }

#done
class UserScoreSheetElementWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserScoreSheetElement
        #fields = ('id', 'value', 'userregistrationround', 'scoresheetelement')
        fields = ('id', 'value', 'scoresheetelement')
        #required_fields = ('value', 'userregistrationround', 'scoresheetelement')
        required_fields = ('value', 'scoresheetelement')

#done
class UserRegistrationRoundWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRegistrationRound
        fields = ('id', 'registration', 'round', 'status', 'user', 'is_active')
        required_fields = ('registration', 'round', 'status', 'user', 'is_active')

#Los read serializers

class ScoreCategoryReadSerializer(ScoreCategoryWriteSerializer):
    parentscorecategory = ParentScoreCategoryWriteSerializer(read_only=True)

class ScoreSheetReadSerializer(ScoreSheetWriteSerializer):
    scoresheettype = ScoreSheetTypeWriteSerializer(read_only=True)

class ChampionshipScoreSheetReadSerializer(ChampionshipScoreSheetWriteSerializer):
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
    institution = InstitutionWriteSerializer(read_only=True)

class RegistrationReadSerializer(RegistrationWriteSerializer):
    team = TeamReadSerializer(read_only=True)
    championshipscoresheet = ChampionshipScoreSheetReadSerializer(read_only=True)
    divisiongroup = DivisionGroupReadSerializer(read_only=True)

class UserRegistrationRoundReadSerializer(UserRegistrationRoundWriteSerializer):
    registration = RegistrationReadSerializer(read_only=True)
    round = RoundWriteSerializer(read_only=True)
    status = StatusWriteSerializer(read_only=True)

class ScoreSheetElementReadSerializer(ScoreSheetElementWriteSerializer):
    scoremetric = ScoreMetricWriteSerializer(read_only=True)
    scorecategory = ScoreCategoryReadSerializer(read_only=True)
    scoresheet = ScoreSheetReadSerializer(read_only=True)

class UserScoreSheetElementReadSerializer(UserScoreSheetElementWriteSerializer):
    scoresheetelement = ScoreSheetElementReadSerializer(read_only=True)
    #userregistrationround = UserRegistrationRoundReadSerializer(read_only=True)

class UserSkillPermissionReadSerializer(UserSkillPermissionWriteSerializer):
    scoresheetelement = ScoreSheetElementReadSerializer(read_only=True)
    #userregistrationround = UserRegistrationRoundReadSerializer(read_only=True)
