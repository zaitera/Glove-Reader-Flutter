from Imu import Imu
from random import randint

class HandReading():
    
    def __init__(self):
        self.timestamp = int
        self.imus = [Imu(), Imu(), Imu(), Imu(), Imu()]
    
    def getRandom(self):
        self.imus = [imu.getRandom(finger) for finger, imu in enumerate(self.imus)]
        self.timestamp = randint(0, 500000)
        return self
    
    def __str__(self):
        return f"""HandReading: 
        Timestamp = {self.timestamp}
        HandImus:
            Finger 1 = {self.imus[0]}
            Finger 2 = {self.imus[1]}
            Finger 3 = {self.imus[2]}
            Finger 4 = {self.imus[3]}
            Finger 5 = {self.imus[4]}
        """
    