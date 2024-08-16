from django.db import models

class CitySearch(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.CharField(max_length=10)  # Assuming temperature is stored as a string like "20°C"
    search_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} ({self.temperature})"
