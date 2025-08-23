from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Arquivo
from .serializers import ArquivoSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ArquivoViewSet(viewsets.ModelViewSet):
    queryset = Arquivo.objects.all()
    serializer_class = ArquivoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['mes_publicacao']
    search_fields = ['url_pdf']

