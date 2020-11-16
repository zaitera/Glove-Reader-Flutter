from HandReading import HandReading
import csv

OBJECT_SIZE = 34
DATA_FILENAME = 'data.csv'

def partition(array, sliceSize):
    division = len(array) / sliceSize
    if (not division.is_integer()):
        raise ValueError("Data file does not contain a valid quantitiy of bytes for a whole number of reading objects")

    return [array[sliceSize * i:sliceSize * (i + 1)] for i in range(round(division))]

if __name__ == "__main__":

    with open(DATA_FILENAME) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        bytesData = bytearray()
        for sublist in csv_reader:
            for item in sublist:
                bytesData += (bytes([int(item)]))
    
    byteObjects = partition(bytesData, OBJECT_SIZE)

    readings = list()
    
    for byteobject in byteObjects:
        reading = HandReading()
        reading.timestamp = int.from_bytes(byteobject[0:4], "big", signed = False)
        currentByte = 4
        for imu in reading.imus:
            imu.accel.append(int(byteobject[currentByte]))
            currentByte+=1
            imu.accel.append(int(byteobject[currentByte]))
            currentByte+=1
            imu.accel.append(int(byteobject[currentByte]))
            currentByte+=1
            imu.gyro.append(int(byteobject[currentByte]))
            currentByte+=1
            imu.gyro.append(int(byteobject[currentByte]))
            currentByte+=1
            imu.gyro.append(int(byteobject[currentByte]))
            currentByte+=1
        readings.append(reading)
        del reading

    [ print(reading) for reading in readings ]
        
    pass
