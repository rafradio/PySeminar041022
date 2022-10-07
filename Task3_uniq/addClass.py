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
                    break     
                except:
                    print("Вы ввели не соответсвующую запись! Попробуйте еще раз")
            
            this.initArray = []        
            for i in range(this.N):
                this.initArray.append(random.randrange(0, 10))
            
            

class ExecModule:
    def __init__(this, initObj):
        this.simpleD = initObj.N
        this.initArray = initObj.initArray
        print(this.initArray)
        this.cacheList = this.initArray.copy()
        this.newList = filter(this.Exec, this.initArray)
        print(list(this.newList))

    def Exec(this, x):
        this.cacheList.remove(x)
        if x in this.cacheList: 
            this.cacheList.append(x)
            return False
        else: 
            this.cacheList.append(x)
            return True

        