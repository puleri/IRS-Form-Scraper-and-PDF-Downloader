from rest_framework import serializers

from .models.IRSpdf import IRSpdf

class IRSpdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = IRSpdf
        fields = ('form_number', 'form_title', 'min_year', 'max_year')
