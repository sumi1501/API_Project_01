from rest_framework import serializers
from app.models import *

class Schoolmodel(serializers.ModelSerializer):
    class Meta:
        model=School
        feilds='__all__'