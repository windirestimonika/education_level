from rest_framework import serializers 
#from rest_framework import User
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'