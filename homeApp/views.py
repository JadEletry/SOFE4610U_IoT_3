from django.shortcuts import render
import requests
import json
from rest_framework import viewsets
from homeApp.models import Mode, State
from homeApp.serializers import ModeSerializer, StateSerializer
from homeApp.gpio_config import light_off, light_on, auto_mode

# Django Rest Framework ViewSets for Mode and State models
class ModeViewSet(viewsets.ModelViewSet): 
    queryset = Mode.objects.all() 
    serializer_class = ModeSerializer

class StateViewSet(viewsets.ModelViewSet): 
    queryset = State.objects.all() 
    serializer_class = StateSerializer

def toggle_state(request):
    current_state = requests.get('http://127.0.0.1:8000/api/state/1/').json()
    current_state_name = current_state['name']

    # Control LED state based on the received state change
    if current_state_name == 'on':
        light_on()  # Turn on the LED using GPIO function
    elif current_state_name == 'off':
        light_off()  # Turn off the LED using GPIO function

    # Toggle the state
    new_state = 'off' if current_state_name == 'on' else 'on'
    requests.put('http://127.0.0.1:8000/api/state/1/', json={'name': new_state})

    return render(request, 'dashboard.html', {})


# Toggle mode function to change the mode of the application
def toggle_mode(request):

    # Get the current mode from the API
    current_mode = requests.get('http://127.0.0.1:8000/api/mode/1/').json()
    current_mode_name = current_mode['name']

    # Toggle the mode
    new_mode = 'manual' if current_mode_name == 'auto' else 'auto'

    if new_mode == 'auto':
        auto_mode()

    requests.put('http://127.0.0.1:8000/api/mode/1/', json={'name': new_mode})

    return render(request, 'dashboard.html', {})  # Render appropriate response or redirect

# Main view for the application
def homeApp(request):

    # Get the current mode and state from the API
    current_mode = requests.get('http://127.0.0.1:8000/api/mode/1/').json()
    current_state = requests.get('http://127.0.0.1:8000/api/state/1/').json()

    current_mode_name = current_mode['name']
    current_state_name = current_state['name']

    # Prepare context with current mode and state to pass to the template
    context = {
        'currentMode': current_mode_name,
        'currentState': current_state_name
    }

    return render(request, 'dashboard.html', context)
