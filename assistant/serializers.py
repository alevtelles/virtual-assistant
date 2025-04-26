from rest_framework import serializers
from .models import Assistente, Documento

class AssistenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistente
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'
