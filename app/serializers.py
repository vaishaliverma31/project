
from rest_framework import serializers
from .models import *

class  studentdetailserializer(serializers.ModelSerializer):
    class Meta:
        model=  studentdetail
        fields=  '__all__'