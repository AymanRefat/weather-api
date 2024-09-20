from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
import requests 
from django.conf import settings

class WeatherAPIView(APIView):
    def get(self, request, city):
        cache_key = f"weather_{city}"
        cached_data = cache.get(cache_key)
        
        if cached_data:
            return Response(cached_data)

        # Fetch data from the external API
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHER_API_KEY}"
        response = requests.get(api_url)
        if response.status_code == 200:
            weather_data = response.json()
            # Cache the data for 10 minutes
            cache.set(cache_key, weather_data, timeout=600)
            return Response(weather_data)
        return Response({'error': 'City not found'}, status=404)
