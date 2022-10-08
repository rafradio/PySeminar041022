from cmath import pi
import os

class InitSets:
    def __init__(this):
        clear = lambda: os.system("CLS")
        clear()
        this.strLegend = "Введите пожалуйста положительное дробное число, меньшее 1: "
        this.InputFunc()

    def InputFunc(this):
            while True:
                try:
                    this.D = float(input(this.strLegend))        
                except:
                    print("Вы ввели не соответсвующую запись! Попробуйте еще раз")
                else: 
                    if this.D < 1: return
                    else: print("Вы ввели некорректное число! Попробуйте еще раз")

class ExecModule:
    def __init__(this, initObj):
        this.D = initObj.D
        print("Ваша заданная точность - ", this.D)
        this.N = 0
        this.FindN()

    def FindN(this):
        while this.D < 10:
            this.N += 1
            this.D = this.FindPi(this.D)()
        print(f"Число пи с заданной точностью: {str(this.piD)[:-1]}")

    def FindPi(this, d):
        this.piD = round(pi, this.N)
        return lambda : d * 10

