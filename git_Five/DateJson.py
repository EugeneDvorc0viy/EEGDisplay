import json
import os
from datetime import datetime as dt

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
            data = {"all": [

            ]}
            with open(f"json/{nameFile}.json", 'w') as file:
                json.dump(data, file)
                file.close()

    def opening(self):
        with open(self.nameFile) as file:
            fileRead = json.load(file)
            return fileRead

    def newTest(self, fileName, title, colvoIndicators):
        time = f"{dt.now().year}/{dt.now().month}/{dt.now().day} {dt.now().hour}:{dt.now().minute}:{dt.now().second}"
        data = {"nameTest": title, "dateTime": time, "description": "", "indicators": colvoIndicators,
                "test": [{"second": "0"}], "status": "Not done"
                }
        with open(f"json/{fileName}.json", "w") as file:
            json.dump(data, file)
            file.close()

    def addInfo(self, context, fileName, status):
        with open(f"json/{fileName}.json") as file:
            data = json.load(file)
            file.close()

        num = len(data["test"])
        textIn = {"second": num}
        for i in range(data["indicators"]):
            textIn[str(i + 1)] = context[i]
        textIn["status"] = status
        data["test"].append(textIn)
        print(num)
        with open(f"json/{fileName}.json", "w") as file:
            json.dump(data, file)

    def helpFileJson(self, someName, nameTest, colvoIndicators):
        if not os.path.exists(f"json/{someName}"):
            text = {
                nameTest: {
                }
            }
            for i in range(colvoIndicators):
                text[nameTest][i] = 0
            with open(f"json/{someName}", "w") as file:
                json.dump(text, file)
                file.close()
            context = "Файл для запасного копирования создан"
        else:
            context = "Нельзя использовать такое имя"
        return context


    def readHelpFileJson(self, name):
        with open(f"json/{name}") as file:
            fileRead = json.load(file)
            return fileRead

    def fileDone(self, nameFile):
        with open(f"json/{nameFile}.json") as file:
            data = json.load(file)
            file.close()
        with open(f"json/{self.nameFile}.json") as bigFile:
            bigData = json.load(bigFile)
            bigFile.close()
        data["status"] = "Done"
        bigData["all"].append(data)
        with open(f"json/{self.nameFile}.json", 'w') as file:
            json.dump(bigData, file)
            file.close()



#
a = JsonForDate("")
# # print(a.helpFileJson("check.json", "CheckOne", 5))
# a.addElem([1, 2, 3, 4, 5], "check.json", "CheckOne", 5)
# print(a.readHelpFileJson("check.json"))

# print(dt.now())
#
# a.addInfo([35, 21, 12], "Some", True)
