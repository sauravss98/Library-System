from rest_framework import serializers
from .models import *


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email',"password",]

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email',"first_name","last_name"]