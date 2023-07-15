from django.test import TestCase,Client
from rest_framework import status
from rest_framework.test import APIClient
from capitals.db_api import country_create
from django.urls import reverse

class QuizViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.country_instance = country_create(name="dummy",capital="fake")

        
    def test_get(self):
        response = self.client.get(reverse('quiz-details'),content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('country_name', response.data['data'])

    def test_post_correct_guess(self):
        payload = {
            'country_name': self.country_instance.name,
            'guess': self.country_instance.capital,
        }
        response = self.client.post(reverse('quiz-details'), data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['message'], 'Guessed Capital is Correct')

    def test_post_incorrect_guess(self):
        payload = {
            'country_name': self.country_instance.name,
            'guess': 'Real Capital',
        }
        response = self.client.post(reverse('quiz-details'), data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data['data'])

    def test_post_invalid_country(self):
        payload = {
            'country_name': 'Unknow Country',
            'guess': 'Capital',
        }
        response = self.client.post(reverse('quiz-details'), data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data['data'])