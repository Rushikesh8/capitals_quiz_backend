from commons.views import BaseView
from commons.api_response import api_error_response,api_success_response
from capitals.db_api import country_update_or_create
import requests

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
            country_name = country_data.get('name')
            capital_name = country_data.get('capital')

            country_update_or_create(
                name=country_name,
                defaults={'capital': capital_name}
            )

        return api_success_response(response_data={'message':"Capital fetch and stored successfully"})





