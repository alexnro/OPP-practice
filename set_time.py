class Time():


    def __init__(self, hour, minutes, seconds):
        self.hour = 0
        self.minutes = 0
        self.seconds = 0


    def setTime(self, hour, minutes, seconds):
        if hour in range(0, 25):
            self.hour = hour
        else:
            self.hour = 00
        
        if minutes in range(0, 60):
            self.minutes = minutes
        else:
            self.minutes = 00

        if seconds in range(0, 60):
            self.seconds = seconds
        else:
            self.seconds = 00


    def getTime(self):
        return f'{self.hour}:{self.minutes}:{self.seconds}'


    def printTime(self):
        print(self.getTime())

 

if __name__ == '__main__':


    actualHour = Time(1, 2, 3)
    actualHour.setTime(2, 25, 36)
    assert actualHour.getTime() == "2:25:36"

    actualHour.setTime(25, 30, 30)
    assert actualHour.getTime() == "0:30:30"
    actualHour.setTime(2, 60, 60)
    assert actualHour.getTime() == "2:0:0"