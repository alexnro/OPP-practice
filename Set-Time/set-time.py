class Time():

    def __init__(self, hour, minutes, seconds):
        self.hour = 0
        self.minutes = 0
        self.seconds = 0

    def setTime(self, hour, minutes, seconds):
        if hour in range(0, 25):
            self.hour = hour
        else:
            self.hour = 0
        
        if minutes in range(0, 60):
            self.minutes = minutes
        else:
            self.minutes = 0

        if seconds in range(0, 60):
            self.seconds = seconds
        else:
            self.seconds = 0

    def getTime(self):
        return f'{self.hour}:{self.minutes}:{self.seconds}'

    def printTime(self):
        print(getTime())



if __name__ == '__main__':

    actualHour = Time()
    assert actualHour(5, 20, 35) == '5:20:35'
    assert actualHour(26, 50, 60) == '0:50:0'
    assert actualHour(26, 61, 60) == '26:61:60'