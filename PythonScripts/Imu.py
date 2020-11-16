import ctypes
class Imu:
    
    def __init__(self):
        self.accel = list()
        self.gyro = list()
    
    def getRandom(self, factor):
        self.accel.append((factor+1)*11)
        self.accel.append((factor+1)*12)
        self.accel.append((factor+1)*13)
        self.gyro.append((factor+1)*21)
        self.gyro.append((factor+1)*22)
        self.gyro.append((factor+1)*23)
        return self

    def __str__(self):
        return f"""
                Accelerometers = {self.accel}
                Gyroscopes     = {self.gyro}"""