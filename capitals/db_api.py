from capitals.models import Country
from django.db.models import QuerySet

def country_update_or_create(*args,**kwargs) -> Country:
    return Country.objects.update_or_create(*args,**kwargs)

def get_all_countries() -> QuerySet:
    return Country.objects.all()

def get_country(*args,**kwargs) -> Country:
    return Country.objects.get(*args,**kwargs)