from operator import concat
import os
import random

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
        this.D = initObj.N
        this.arrKoeff = [random.randrange(0, 100) for i in range(this.D + 1)]
        print(this.arrKoeff)
        this.znaki = ["*", "x", "^", "i", " + "]
        this.CreatString()
        this.PushToFile()

    def CreatString(this):
        this.string = ""

        for i in range(len(this.arrKoeff)):
            if this.arrKoeff[i] == 0: continue
            this.string += str(this.arrKoeff[i])

            for j in range(len(this.znaki)):
                this.string += this.znaki[j]

            this.string = this.string.replace("i", str(len(this.arrKoeff) - i - 1))
            
            
        this.string = this.string.replace("^1", "")
        this.string = this.string[:-7] + " = 0"
        print(this.string)

    def PushToFile(this):
        try:
            f = open("myfile.txt", "x")
            f.write(this.string)
            f.close()
        except:
            f = open("myfile.txt", "w")
            f.write(this.string)
            f.close()
            print("Файл уже существует")


       


        