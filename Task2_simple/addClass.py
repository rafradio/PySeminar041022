import os

class InitSets:
    def __init__(this):
        clear = lambda: os.system("CLS")
        clear()
        this.strLegend = "Введите пожалуйста положительное целое число: "
        this.InputFunc()

    def InputFunc(this):
            while True:
                try:
                    this.N = float(input(this.strLegend))
                    this.N = int(this.N)   
                    return     
                except:
                    print("Вы ввели не соответсвующую запись! Попробуйте еще раз")
                
class ExecModule:
    def __init__(this, initObj):
        this.simpleD = initObj.N
        this.D = list(range(2, initObj.N + 1))
        this.simple = list(filter(this.Dividers, this.D))
        this.simpleDiveders = filter(this.Exec, this.simple)
        print(list(this.simpleDiveders))

    def Dividers(this, x):
        for j in range(2, x):
            if x % j == 0:
                return False
        else:
            return True

    def Exec(this, x):      
        if this.simpleD % x == 0: return True
        else: return False
        