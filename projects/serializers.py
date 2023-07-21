from rest_framework import serializers
from .models import Project
#convierte el modelo en datos que pueden ser consultados
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        #estos son los campos que podrá consultar el project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        #le diré cuáles son los campos de solo lectura
        read_only_fields = ('created_at',)
