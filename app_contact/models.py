###############################################################################
"""
Django models for the Contact app
"""
# IMPORTED RESOURCES #

# EXTERNAL:
from django.db import models

###############################################################################


class DataFromContactForm(models.Model):
    """
    A contact form class for the data of the contact form
    Primary key (id field) automatically added my Django
    """
    date = models.DateField(max_length=200)
    time = models.TimeField(default="00:00:00", max_length=200)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return f"Contact form from {self.name} {self.surname}"
