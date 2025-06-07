from gpiozero import MotionSensor
from time import sleep
from gpiozero import TonalBuzzer 
from gpiozero.tones import Tone

pir = MotionSensor(4)
bz = TonalBuzzer(3)
print("start")
while True:
          if pir.motion_detected:
                    print("Motion detected!")
                    bz.play(Tone("A4"))
                    sleep(1)
                    bz.stop()
                    sleep(0.5)
          else:
                    sleep(0.5)
                    print("No motion")