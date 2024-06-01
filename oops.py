

from traceback import print_tb
from typing import Self


class Car():
    
    def __init__(self):
        print("BOOOM GRT ")
    
    def Speed(self,speed):
        self.speed = speed
        print(f"Car Max speed is above {self.speed}")
    
    def Brake(self):
        print("kerrrrrrrrr The Car Had Stopped")


GTR = Car()

GTR.Speed(200)
GTR.Brake()