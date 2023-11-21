## Light Control System

### Description

This is a repository which contains the code and instructions needed to run an
application which allows the user to control an LED light using Django's framework
as a backend and a simple frontend UI as a dashboard. The LED's behavior is enabled
by an LDR sensor all which have been wired and ocnfigured using a Raspberry Pi and 
a breadboard. <br>

The dashboard is a UI controlled by the user which provides 2 separate functionalities.
The first being that the user can toggle the LED on/off by clicking 'state' button, and
the second being that the user can control the LED's behavior by clicking the 'mode' 
button; the LED can then be set to manual/auto. 

## Configuring the LED/LDR

To wire the system appropriately, follow these steps:
- Take an LED and place its shorter leg (cathode) on the negative column of a breadboard
- Take the LED's longer leg (positive/anode) and place it in-line within a row of the breadboard
- Take a 1K ohm resistor and place one end next to the positive leg of the LED and place the other end somewhere down the same column of the breadboard
- 


