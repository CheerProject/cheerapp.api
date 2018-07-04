from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

#from project.judge.serializers import UserScoreCategorySerializer
#from project.judge.serializers import ScoreSheetSerializer


import environ
from datetime import datetime, timedelta


class UserSerializer(serializers.ModelSerializer):
    #user_score_categories = UserScoreCategorySerializer(many=True)
    #score_sheets = ScoreSheetSerializer(many=True)

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(max_length=32,
                                     validators=[UniqueValidator(
                                         queryset=User.objects.all())]
                                     )

    password = serializers.CharField(
        min_length=8, write_only=True, required=True)


    def create(self, validated_data):

        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
            is_active=validated_data['is_active'])

        return user

    class Meta:
        model = User

        #fields = ('id', 'username', 'email', 'password', 'is_active', 'user_score_categories', 'score_sheets')
        #required_fields = ('username', 'password', 'email', 'user_score_categories', 'score_sheets')
