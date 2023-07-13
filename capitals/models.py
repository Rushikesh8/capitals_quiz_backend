from django.db import models

class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        
class Country(BaseModel):
    name = models.CharField(max_length=120)
    capital = models.CharField(max_length=120)