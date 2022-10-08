from operator import concat
import os
import random

class InitSets:
    def __init__(this):
        clear = lambda: os.system("CLS")
        clear()

class ExecModule:
    def __init__(this):
        this.koeff = []
        this.myFilestxt = ["myfile.txt", "myfile1.txt"]
        this.FindFiles()
        this.FindSum()
        print(this.koeff)
        print("Сумма равна: ", this.sum)
        this.PushToFile()

    def FindFiles(this):
        for i in range(2):
            this.ReadFiles(this.myFilestxt[i])
            this.AnalyseStrings()

    def ReadFiles(this, filename):
        f = open(filename, "r")
        this.strFile1 = f.read()
        f.close()
        this.strFile1 = this.strFile1.replace(" ", "")
        print(this.strFile1)

    def AnalyseStrings(this):
        posInt = ""
        prev = ""
        for i in this.strFile1:
            try:
                num = int(i)
                checkFlag = True
            except:
                checkFlag = False

            if checkFlag: 
                posInt += str(num)
            else:
                if len(posInt) != 0:
                    if i == "*" or i == "=":
                        this.koeff.append(posInt)
                posInt = ""
                if i == "x":
                    if prev == "" or prev =="+":
                        this.koeff.append("1")

            prev = i

    def FindSum(this):
        this.sum = 0
        for i in this.koeff:
            this.sum += int(i)

    def PushToFile(this):
        inputString = "File sum: " + str(this.sum)
        try:
            f = open("myfileSum.txt", "x")
            f.write(inputString)
            f.close()
        except:
            f = open("myfileSum.txt", "w")
            f.write(inputString)
            f.close()
            print("Файл уже существует") 
            
        # if isinstance(num, int):
        #     print("hello raf")
        #     x = this.strFile1[0]
        #     print(this.strFile1[0])
        # else: print("no")
        # for i in this.strFile1:
        #     print()



