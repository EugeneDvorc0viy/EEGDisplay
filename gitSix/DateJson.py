import json
import os
from datetime import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

class JsonForDate:

    def __init__(self, nameFile):
        self.nameFile = nameFile
        self.idTest = []
        try:
            with open(f"json/{nameFile}.json") as file:
                data = json.load(file)
                file.close()
            for elem in data:
                self.idTest.append(elem)
        except Exception:
            data = {
            }
            with open(f"json/{nameFile}.json", 'w') as file:
                json.dump(data, file)
                file.close()

    def opening(self):
        with open(f"json/{self.nameFile}.json") as file:
            fileRead = json.load(file)
            return fileRead

    def newTest(self, fileName, title, colvoIndicators):
        time = f"{dt.now().year}/{dt.now().month}/{dt.now().day} {dt.now().hour}:{dt.now().minute}:{dt.now().second}"
        data = {"nameTest": title, "dateTime": time, "description": "", "indicators": colvoIndicators,
                "test": [], "status": "Not done"
                }
        with open(f"json/{fileName}.json", "w") as file:
            json.dump(data, file)
            file.close()

    def addInfo(self, context, fileName):
        with open(f"json/{fileName}.json") as file:
            data = json.load(file)
            file.close()

        # num = len(data["test"])
        textIn = {}
        for i in range(data["indicators"]):
            textIn[str(i + 1)] = context[i]
        data["test"].append(textIn)
        with open(f"json/{fileName}.json", "w") as file:
            json.dump(data, file)
            file.close()

    # def helpFileJson(self, someName, nameTest, colvoIndicators):
    #     pass
    #     if not os.path.exists(f"json/{someName}"):
    #         text = {
    #             nameTest: {
    #             }
    #         }
    #         for i in range(colvoIndicators):
    #             text[nameTest][i] = 0
    #         with open(f"json/{someName}", "w") as file:
    #             json.dump(text, file)
    #             file.close()
    #         context = "Файл для запасного копирования создан"
    #     else:
    #         context = "Нельзя использовать такое имя"
    #     return context


    # help func
    def readHelpFileJson(self, name):
        with open(f"json/{name}.json") as file:
            fileRead = json.load(file)
            return fileRead

    def fileDone(self, nameFile, nameTest):
        with open(f"json/{nameFile}.json") as file:
            data = json.load(file)
            file.close()
        with open(f"json/{self.nameFile}.json") as bigFile:
            bigData = json.load(bigFile)
            bigFile.close()
        data["status"] = "Done"
        bigData[nameTest] = data
        with open(f"json/{self.nameFile}.json", 'w') as file:
            json.dump(bigData, file)
            file.close()

    def showTestResult(self, namePart):
        with open(f"json/{self.nameFile}.json") as file:
            data = json.load(file)
            file.close()

        colvoDatch = data[namePart]["indicators"]



        numElem = 0
        time = [(i + 1) for i in range(len(data[namePart]["test"]))]
        titleLine = []
        for indicator in range(1, data[namePart]["indicators"] + 1):
            result = []
            titleLine.append(f"Датчик {indicator}")
            for elem in data[namePart]["test"]:

                result.append(int(elem[str(indicator)]))
            plt.plot(time, result)

        plt.title(f"Эксперимент: {namePart}"),
        plt.xlabel("Time")
        plt.ylabel("Result")
        plt.grid()
        plt.legend(titleLine)
        plt.show()

        # plt.show()
        # x = np.linspace(1, 10, 50)
        # y = x
        # plt.title("CheckOne")
        # plt.xlabel("Time")
        # plt.ylabel("Result")
        # plt.grid()
        # plt.plot(x, y)
        # plt.show()



#


# # print(a.helpFileJson("check.json", "CheckOne", 5))
# a.addElem([1, 2, 3, 4, 5], "check.json", "CheckOne", 5)
# print(a.readHelpFileJson("check.json"))

# print(dt.now())
#
# a.addInfo([35, 21, 12], "Some", True)
