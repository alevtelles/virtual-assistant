from django.shortcuts import render

from rest_framework import viewsets
from .models import Assistente, Documento
from .serializers import AssistenteSerializer, DocumentoSerializer
from .langchain_service import processar_documento

class AssistenteViewSet(viewsets.ModelViewSet):
    queryset = Assistente.objects.all()
    serializer_class = AssistenteSerializer

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

    def perform_create(self, serializer):
        doc = serializer.save()
        processar_documento(doc)
