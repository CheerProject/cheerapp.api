from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

import environ
from datetime import datetime, timedelta


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(max_length=32,
                                     validators=[UniqueValidator(
                                         queryset=User.objects.all())]
                                     )

<<<<<<< HEAD
    password = serializers.CharField(min_length=8, write_only=True, required=True)
=======
    password = serializers.CharField(
        min_length=8, write_only=True, required=True)
>>>>>>> origin/develop

    def create(self, validated_data):

        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
            is_active=validated_data['is_active'])

        return user

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ('id', 'username', 'email', 'password','is_active')
        required_fields = ('username','password','email')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  
    def validate(self,attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)

        env = environ.Env()
        expired_token = env('ACCESS_TOKEN_LIFETIME', default=5)
        nextTime = datetime.now() + timedelta(minutes = expired_token)
        time_stamp = str(int(nextTime.timestamp()))
        print('time stamp ' + time_stamp)
        
        data['expires_on'] = time_stamp

        return data

=======
        fields = ('id', 'username', 'email', 'password', 'is_active')
        required_fields = ('username', 'password', 'email')
>>>>>>> origin/develop
