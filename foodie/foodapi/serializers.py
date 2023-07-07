from rest_framework import serializers
from .models import foods,cartitems,UserSignup,reviews

class RegSerializer(serializers.ModelSerializer):
    class Meta:
        model = foods
        fields = '__all__'

class RugSerializer(serializers.ModelSerializer):
    class Meta:
        model = cartitems
        fields = '__all__'

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSignup
        fields = '__all__'

class FugSerializer(serializers.ModelSerializer):
    class Meta:
        model = reviews
        fields = '__all__'