from HandReading import HandReading
import csv
import os

OBJECT_SIZE = 36
DATA_FILENAME = 'data.csv'

def partition(array, sliceSize):
    division = len(array) / sliceSize
    if (not division.is_integer()):
        raise ValueError("Data file does not contain a valid quantitiy of bytes for a whole number of reading objects")

    return [array[sliceSize * i:sliceSize * (i + 1)] for i in range(round(division))]

if __name__ == "__main__":

    csvLen = 0
    with open(DATA_FILENAME) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csvLen = sum(1 for row in csv_reader)
        csv_file.close()

    with open(DATA_FILENAME) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        bytesData = bytearray()
        
        for i,sublist in enumerate(csv_reader):
            for j,item in enumerate(sublist):
                if not(i == csvLen-1 and (j == len(sublist)-1)):
                    bytesData += (bytes([int(item)]))
                    
    
    byteObjects = partition(bytesData, OBJECT_SIZE)

    readings = list()
    
    for byteobject in byteObjects:
        reading = HandReading()
        reading.timestamp = int.from_bytes(byteobject[0:4], "little", signed = False)
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
