from commons.views import BaseView
from commons.api_response import api_error_response,api_success_response
from capitals.db_api import country_update_or_create,get_all_countries,get_country
from django.core.exceptions import ObjectDoesNotExist
import requests
import random

COUNTRY_CAPITAL_API_URL = 'https://countriesnow.space/api/v0.1/countries/capital'

class FetchAndStoreCapitals(BaseView):
    def post(self, request):
        response = requests.get(COUNTRY_CAPITAL_API_URL)
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return api_error_response(error_message="Failed to fetch capital data")
            
        data = response.json()
        countries = data.get('data', [])
        
        for country_data in countries:
            country_name = country_data.get('name').lower()
            capital_name = country_data.get('capital','').lower()

            if not capital_name:        # if capital name is not present move to next country 
                continue

            country_update_or_create(
                name=country_name,
                defaults={'capital': capital_name}
            )

        return api_success_response(response_data={'message':"Capital fetch and stored successfully"})


class QuizView(BaseView):

    def get(self, request):
        countries = get_all_countries()
        if not countries.exists():
            return api_error_response(error_message="No records exist. Please add countries")
        country = random.choice(countries)
        return api_success_response(response_data={"country_name":country.name})
    
    def post(self,request):
        self.validate_field_in_params(request.data,['country_name','guess'])
        country_name = request.data.get('country_name')
        guess = request.data.get('guess')
        try:
            country = get_country(name=country_name)
        except ObjectDoesNotExist:
            return api_error_response(error_message=f"Country with name {country_name} does not exists")
        
        if country.capital.lower() == guess.lower():
            return api_success_response(response_data={"message": "Guessed Capital is Correct"})
        
        return api_error_response(error_message="Guessed Capital is Incorrect")






