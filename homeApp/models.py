from django.db import models

# used to identify if automatic or manual

class Setting(models.Model):
    # Add fields relevant to your application's settings
    led_state = models.BooleanField(default=False)  # Example field for LED state
    auto_mode = models.BooleanField(default=False)  # Example field for auto/manual mode

    # Add any other fields or configurations relevant to your application

class Mode(models.Model):
    name = models.CharField(max_length=50)

# used to identify if light is on or off

class State(models.Model):
    name = models.CharField(max_length=50)