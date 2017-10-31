#Python example of oriented programming code

class Auto():
    def __init__(self, placa_auto):
        self.placa = placa_auto

    def getPlaca(self):
        return self.placa

    def setDiasPico(self):
        lastDigit = self.placa[-1]
        if lastDigit == "1" or lastDigit == "2":
            self.dia = 0
        elif lastDigit == "3" or lastDigit == "4":
            self.dia = 1
        elif lastDigit == "5" or lastDigit == "6":
            self.dia = 2
        elif lastDigit == "7" or lastDigit == "8":
            self.dia = 3
        elif lastDigit == "9" or lastDigit == "0":
            self.dia = 4
        else:
            self.dia = "libre"

    def getIsPico(self,fecha,hora):
        dt = '2001-10-18'
        year, month, day = (int(x) for x in fecha.split('-'))
        theDay = datetime.date(year, month, day).weekday()

        
