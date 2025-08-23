from rest_framework import serializers
from .models import Arquivo

class ArquivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arquivo
        fields = ['url_pdf', 'mes_publicacao']
