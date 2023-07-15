from capitals.models import Country
from django.db.models import QuerySet

def get_all_countries() -> QuerySet:
    return Country.objects.all()

def get_country(*args,**kwargs) -> Country:
    return Country.objects.get(*args,**kwargs)

def country_create(*args,**kwargs) -> Country:
    return Country.objects.create(*args,**kwargs)