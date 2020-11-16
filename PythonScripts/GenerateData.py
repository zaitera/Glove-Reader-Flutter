from HandReading import HandReading
from Imu import Imu

if __name__ == "__main__":
    reading = HandReading().getRandom()
    print(reading)