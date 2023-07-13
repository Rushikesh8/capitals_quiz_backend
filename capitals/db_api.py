from capitals.models import Country
from django.db.models import QuerySet

def country_update_or_create(*args,**kwargs) -> Country:
    return Country.objects.update_or_create(*args,**kwargs)