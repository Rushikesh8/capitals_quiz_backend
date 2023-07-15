from django.urls import path
from capitals.views import FetchAndStoreCapitals,QuizView


urlpatterns = [
    path('capitals/', FetchAndStoreCapitals.as_view(), name='capitals'),
    path('quiz/', QuizView.as_view(), name='quiz-details')

]