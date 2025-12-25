from rest_framework import serializers
from api.models import Company  # Importing here to avoid circular imports



class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"