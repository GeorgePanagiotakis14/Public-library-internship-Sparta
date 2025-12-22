from django.db import models

class Person(models.Model):
    ari8mosEisagoghs = models.CharField(unique=True, max_length=200, null=True, blank=True)
    hmeromhnia_eis = models.CharField(max_length=200, null=True, blank=True)
    syggrafeas = models.CharField(max_length=200, null=True, blank=True)
    koha = models.CharField(max_length=200, null=True, blank=True)
    titlos = models.CharField(max_length=200, null=True, blank=True)
    ekdoths = models.CharField(max_length=200, null=True, blank=True)
    ekdosh = models.CharField(max_length=200, null=True, blank=True)
    etosEkdoshs = models.CharField(max_length=20, null=True, blank=True)
    toposEkdoshs = models.CharField(max_length=200, null=True, blank=True)
    sxhma = models.CharField(max_length=200, null=True, blank=True)
    selides = models.CharField(max_length=50, null=True, blank=True)
    tomos = models.CharField(max_length=50, null=True, blank=True)
    troposPromPar = models.CharField(max_length=200, null=True, blank=True)
    ISBN = models.CharField(max_length=50, null=True, blank=True)
    sthlh1 = models.CharField(max_length=200, null=True, blank=True)
    sthlh2 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name