
import datetime
from datetime import time


class Auto():
    def __init__(self, placa_auto):
        self.placa = placa_auto                   #Set the number of the "placa" for every car called

    def getPlaca(self):
        return self.placa                         #Get the number if it's necesary

    def setDiasPico(self):
        lastDigit = self.placa[-1]                  # Just take the last number to evaluate
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
            self.dia = "libre"                  # For saturday and sunday

    def getIsPico(self,fecha,hora):
        self.setDiasPico()                      # When evaluate first set the prohibited day of the car
        year, month, day = (int(x) for x in fecha.split('-'))
        theDay = datetime.date(year, month, day).weekday()  # Get the prohibited day of that dat

        # Evaluate the range of hours to apply "Pico y Placa"
        if time(7,0) <= time(int(hora.split(":")[0]),int(hora.split(":")[1])) <= time(9,30) or time(16,0) <= time(int(hora.split(":")[0]),int(hora.split(":")[1])) <= time(19,30):
            horaProhibida = True
        else:
            horaProhibida = False

        if theDay == self.dia:
            diaProhibido = True
        else:
            diaProhibido = False

        if diaProhibido and horaProhibida: # If day of car and prohibited day are the same, and the hour is on range, the car can't road
            return "No Circula"

        else:
            return "Puede Circular"


def main():
    mio = Auto("AAA-553")
    print mio.getIsPico("2017-10-31","19:32")


if __name__ == '__main__':
    main()
