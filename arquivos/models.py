from django.db import models

class Arquivo(models.Model):
    id = models.AutoField(primary_key=True)
    url_pdf = models.URLField()
    mes_publicacao = models.CharField(max_length=2, db_index=True)

    

