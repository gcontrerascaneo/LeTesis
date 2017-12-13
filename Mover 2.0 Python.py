#!/usr/bin/env python
import nxt.locator
import consola_io
from nxt.motor import *
import time

def menu():
  print """ 
     Menu de opciones
     ________________
    
     Derecha    a
     Izquierda  d           W
     Avanzar    w       A   S   D
     Detener    s
     Mostrar    menu
     Terminar   s
  """
 
def derecha(b):
    motor_direccion = Motor(R2D2, PORT_B)
    motor_direccion.turn(100, 360)
    time.sleep(1)
    motor_direccion.idle()
    print "Derecha"
   
def izquierda(b):
    motor_direccion = Motor(R2D2, PORT_C)
    motor_direccion.turn(100, 360)
    time.sleep(1)
    motor_direccion.idle()
    print "Izquierda"

def avanzar(b):
    motor_traccion = Motor(R2D2, PORT_C)
    motor_traccion2 = Motor(R2D2, PORT_B)
    motor_traccion.run(100)
    motor_traccion2.run(100)
    time.sleep(1)
    motor_traccion.idle()
    motor_traccion2.idle()
    
    print "Avanzar"
   
def retroceder(b):
    motor_traccion = Motor(R2D2, PORT_C)
    motor_traccion2 = Motor(R2D2, PORT_B)
    motor_traccion.run(-100)
    motor_traccion2.run(-100)
    time.sleep(1)
    motor_traccion.idle()
    motor_traccion2.idle()
               
    print "Retroceder"

def detener(b):
    motor_traccion = Motor(R2D2, PORT_C)
    Trac[0] = 0
    motor_traccion.idle()
    print "Detener"

Direc = [0, 60]
Trac = [0, 50]
R2D2 = nxt.locator.find_one_brick()

menu()

while 1:
    
    c = consola_io.getkey()
    
    if c=='d':
        derecha(R2D2)
    elif c=='a':
        izquierda(R2D2)
    elif c=='w':
        avanzar(R2D2)
    elif c=='s':
        retroceder(R2D2)
    elif c=='n':
        retroceder(R2D2)
    elif c==' ':
        detener(R2D2)
        menu()
    elif c=='q':
        detener(R2D2)
        break   

        
