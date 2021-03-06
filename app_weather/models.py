###############################################################################
"""
Django models for the Weather app
"""
# IMPORTED RESOURCES #

# EXTERNAL:
from django.db import models

###############################################################################


class DataAndTimeForData(models.Model):
    """
    Model for Date and Time Data/Table
    """
    # Primary key (id field) automatically added my Django
    date = models.DateField(max_length=200)
    time = models.TimeField(default="00:00:00", max_length=200)

    def __str__(self):
        return f"Date: {self.date}; time: {self.time}"


class WindData(models.Model):
    """
    Model for Wind Data/Table
    """
    # Primary key (id field) automatically added my Django
    wind_rec_id = models.ForeignKey(
        DataAndTimeForData, on_delete=models.CASCADE
    )
    wind_speed = models.FloatField(max_length=200)
    wind_direction = models.FloatField(max_length=200)

    def __str__(self):
        return f"Wind speed: {self.wind_speed}; wind dir:{self.wind_direction}"


class TemperatureData(models.Model):
    """
    Model for Temperature Data/Table
    """
    # Primary key (id field) automatically added my Django
    temp_rec_id = models.ForeignKey(
        DataAndTimeForData,
        on_delete=models.CASCADE
    )
    temperature = models.FloatField(max_length=200)
    feels_like = models.FloatField(max_length=200)
    temperature_max = models.FloatField(max_length=200)
    temperature_min = models.FloatField(max_length=200)

    def __str__(self):
        return f"Temperature: {self.temperature}"


class OtherWeatherData(models.Model):
    """
    Model for All Other Weather Data/Table
    """
    # Primary key (id field) automatically added my Django
    other_rec = models.ForeignKey(
        DataAndTimeForData,
        on_delete=models.CASCADE,
        default=352
    )
    pressure = models.FloatField(max_length=200)
    humidity = models.FloatField(max_length=200)
    visibility = models.FloatField(max_length=200)
    sky = models.CharField(max_length=200)
    main = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    sunrise = models.CharField(max_length=200)
    sunset = models.CharField(max_length=200)

    def __str__(self):
        return f"Other weather data"
