# Light Control System

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

## Configuring the LED

To wire the LED appropriately, follow these steps:
- Take an LED and place its shorter leg (cathode) on the negative column of a breadboard
- Take the LED's longer leg (positive/anode) and place it in-line within a row of the breadboard
- Take a 1K ohm resistor and place one end next to the positive leg of the LED and place the other end somewhere down the same column of the breadboard
- Take a male to female pin and place it next to that other end of the resistor and take the female end and attach it to the GPIO21 (Refer to Raspberry Pi GPIO Pinout)

## Configuring the LDR

To wire the LDR appropriately, follow these steps:
- Place the Photo Light Sensor module somewhere away from the LED configuration vertically along the inner breadboard
- Take a male to female pin and place it in front of the VCC pin of the module and take the female end and attach it to a 5V pin (Refer to Raspberry Pi GPIO Pinout)
- Take a male to female pin and place it in front of the GND pin of the module and take the female end and attach it to one of the GND pins on the Raspberry Pi board
- Take one more male/female pin and place it in front of the Digital Output pin (DO) and take the female end and attach it to GPIO23 on the Raspberry Pi board

Sources: https://pinout.xyz/

## Executing the Program

Clone the repository:
```
git clone https://github.com/JadEletry/SOFE4610U_IoT_3.git
cd SOFE4610U_IoT_3
```
Install the required dependencies
```
pip install -r requirements.txt
```


