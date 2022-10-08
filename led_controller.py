from tkinter import OFF
import tinytuya
import time

d = tinytuya.BulbDevice('bffbe06971f41fa4c5z1nx', '192.168.1.36', 'd5bb8e1da22032e5')
d.set_version(3.3)  # IMPORTANT to set this regardless of version
d.set_socketPersistent(True)  # Optional: Keep socket open for multiple commands
data = d.status()

class led_controller:
    def InicioPartida():
        d.turn_on() 
        d.set_colour(0, 255, 0)
        d.set_brightness_percentage(50)    
    def Pausa():
        d.turn_on() 
        d.set_colour(255, 255, 255)
        d.set_brightness_percentage(50)  
    def Flash():
        d.set_colour(255, 255, 255)
        d.set_brightness_percentage(100)  
    def Molo():
        d.set_colour(255, 175, 0)
        d.set_brightness_percentage(100)  
    def Muerte():
        d.turn_off() 
    def FinRondaCT():
        d.set_colour(0, 0, 255)
        d.set_brightness_percentage(100)  
    def FinRondaT():
        d.set_colour(255, 175, 0)
        d.set_brightness_percentage(100) 
    def Planted():
        if d.colour_rgb() != '(255, 0, 0)':
            d.set_colour(255, 0, 0)
            d.set_brightness_percentage(100)   

