from django.db import models
from django.core.exceptions import ValidationError
import os,bcrypt,uuid,re
from django.contrib.auth.models import User

##########################################################################################################################

def validate_pdf(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf']
    if ext not in valid_extensions:
        raise ValidationError("File should be in pdf format")

##########################################################################################################################

class Conference(models.Model):
    fac_name=models.ForeignKey(User,on_delete=models.CASCADE)
    conference_id = models.CharField(primary_key=True,max_length=100)
    conference_name = models.CharField(max_length=255)
    conference_article = models.FileField(upload_to='conferences/',validators=[validate_pdf])
    conference_doi=models.IntegerField()
    ugc=(('Yes','Yes'),('No','No'))
    ugc_listed=models.CharField(max_length=10,choices=ugc)

    def __str__(self):
        return self.conference_name

##########################################################################################################################

class Journal(models.Model):
    fac_name=models.ForeignKey(User,on_delete=models.CASCADE)
    journal_id = models.CharField(primary_key=True,max_length=100)
    journal_name = models.CharField(max_length=255)
    journal_article = models.FileField(upload_to='journals/',validators=[validate_pdf])
    journal_doi=models.IntegerField()
    ugc=(('Yes','Yes'),('No','No'))
    ugc_listed=models.CharField(max_length=10,choices=ugc)

    def __str__(self):
        return self.journal_name

##########################################################################################################################