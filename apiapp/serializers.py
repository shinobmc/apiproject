from rest_framework import serializers
from apiapp.models import SignupDetails

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignupDetails
        fields = ('id', 'f_name', 'l_name', 'email', 'gender')