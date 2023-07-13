from django.urls import path
from capitals.views import FetchAndStoreCapitals


urlpatterns = [
    path('capitals/', FetchAndStoreCapitals.as_view(), name='capitals'),

]