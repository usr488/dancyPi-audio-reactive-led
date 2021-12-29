import RPi.GPIO as GPIO  ## Importieren der GPIO Bibliothek
import subprocess
from time import sleep

# Zaehler-Variable, global
Counter = 0
Pid = 0
GPIO_switch = 24 # GPIO Port where switch is attached



GPIO.setmode(GPIO.BCM) ## Verwende die Nummerierung der Pins
GPIO.setup(GPIO_switch, GPIO.IN)  ## Setze GPIO Pin 24 auf Eingangssignal (Taster)


# Callback-Funktion
def Interrupt(channel):
        global Counter
  # Counter um eins erhoehen und ausgeben

        if Counter == 0:
                #subprocess.call(["do 1!"])
                print("scroll")
                subprocess.Popen(['sudo killall python3; sudo python3 /home/pi/dancyPi-audio-reactive-led/python/visualization.py scroll'], shell = True)
                #print(process.pid)
                #Pid = process.pid
                Counter += 1
        elif Counter == 1:
                #subprocess.call(["do 2!"])
                print("spectrum")
                subprocess.Popen(['sudo killall python3; sudo python3 /home/pi/dancyPi-audio-reactive-led/python/visualization.py spectrum'], shell = True)
                #print(process.pid)
                #Pid = process.pid
                Counter += 1
        elif Counter == 2:
                #subprocess.call(["do 3!"])
                print("energy")
                subprocess.Popen(['sudo killall python3; sudo python3 /home/pi/dancyPi-audio-reactive-led/python/visualization.py energy'], shell = True)
                Counter += 1 
        elif Counter == 3:
                #subprocess.call(["do 3!"])
                print("off")
                subprocess.Popen(['sudo killall python3; sudo python3 /home/pi/dancyPi-audio-reactive-led/python/off.py'], shell = True)
                Counter = 0 
        else:
                print("counter error")



# Interrupt-Event hinzufuegen, steigende Flanke
GPIO.add_event_detect(GPIO_switch, GPIO.RISING, callback = Interrupt, bouncetime = 250)  

# Endlosschleife, bis Strg-C gedrueckt wird
try:
        subprocess.Popen(['sudo killall python3; sudo python3 /home/pi/dancyPi-audio-reactive-led/python/off.py'], shell = True)
        while True:
    # nix Sinnvolles tun
                sleep(1)

except KeyboardInterrupt:
        subprocess.Popen(['sudo killall python3; sudo python3 /home/pi/dancyPi-audio-reactive-led/python/off.py'], shell = True)
        GPIO.cleanup()
        print ("\nBye")






