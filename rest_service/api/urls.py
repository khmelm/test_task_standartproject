from django.urls import path
from .views import MLView


urlpatterns = [
    path('data/', MLView.as_view(), name='ML_data')
]
