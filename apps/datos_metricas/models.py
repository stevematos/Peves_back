from django.db import models
from apps.EESS.models import Eess

# Create your models here.
class Indicador(models.Model):
    idindicador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicador'

class Atributo(models.Model):
    idatributo = models.AutoField(primary_key=True)
    atributo = models.CharField(max_length=20, blank=True, null=True)
    idindicador = models.ForeignKey(Indicador,on_delete=models.CASCADE, db_column='idindicador')

    class Meta:
        managed = False
        db_table = 'atributo'

class MesesYear(models.Model):
    idfecha = models.AutoField(primary_key=True)
    mes = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'meses-year'

class Valor(models.Model):
    idvalor = models.AutoField(primary_key=True)
    dato = models.FloatField(blank=True, null=True)
    idfecha = models.ForeignKey(MesesYear,on_delete=models.CASCADE, db_column='idfecha')
    ideess = models.ForeignKey(Eess,on_delete=models.CASCADE, db_column='idEESS')  # Field name made lowercase.
    idatributo = models.ForeignKey(Atributo,on_delete=models.CASCADE, db_column='idatributo')

    class Meta:
        managed = False
        db_table = 'valor'
        #unique_together = (('idvalor','idfecha', 'ideess', 'idatributo'),)