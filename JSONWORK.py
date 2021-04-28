import json

class WorkJSON:

    def openning(self, name):
        with open(name) as file:
            fileRead = json.load(file)
            return fileRead

    def adding(self, name, title):
        with open("json/file.json") as file:
            data = json.load(file)
        if title not in data:
            data[title] = {
                "colvo": 0,
                "task": [

                ],
            }
            with open(name, "w") as file:
                json.dump(data, file)
        else:
            print("Ce element est deja existe.")

    def killing(self, name, element):
        with open(name) as file:
            fileRead = json.load(file)
        fileRead.pop(element)
        with open(name, "w") as file:
            json.dump(fileRead, file)

    def changingTask(self, name, element, part=None, new=None):
        func, title, elem = element.split('/')
        elem = int(elem)
        if func == "del":
            self.deleteTask(name, title, elem)
        if func == "add":
            self.addTask(name, title, new)
        if func == "change":
            self.changeTask(name, title, elem, part, new)

    def deleteTask(self, name, title, elem):
        with open(name) as file:
            data = json.load(file)
        data[title]["task"].pop(elem)
        data[title]["colvo"] -= 1
        with open(name, "w") as file:
            json.dump(data, file)

    def addTask(self, name, title, new):
        with open(name) as file:
            data = json.load(file)
        context = {
            "nameTask": new,
            "disTask": '',
            "time": '',
        }
        data[title]["task"].append(context)
        data[title]["colvo"] += 1
        with open(name, "w") as file:
            json.dump(data, file)

    def changeTask(self, name, title, elem, part, new):
        with open(name) as file:
            data = json.load(file)
        data[title]["task"][elem][part] = new
        with open(name, "w") as file:
            json.dump(data, file)

    def forDisplay(self, name, title):
        with open("json/file.json") as file:
            data = json.load(file)
        if title in data:
            try:
                text = title + '\n'
                for i in range(data[title]["colvo"]):
                    context = data[title]["task"][i]
                    text += f"--{context['nameTask']}\n  {context['time']}\n  {context['disTask']}\n\n"
            except Exception:
                text = "Что-то пошло не так.\nВозможно Вы неправильно заполнили форму"
        else:
            text = "Такой программы не существует."
        return text

    
# testing

a = WorkJSON()

print(a.openning("json/file.json"))
# a.changingTask("json/file.json", "add/One/1", new="PressFeet")
# a.changingTask("json/file.json", "add/One/4", new="Press")
# print('\n')
# print(a.openning("json/file.json"))
print(a.forDisplay("json/file.json", "One"))

# a.adding('json/file.json', "Two")
# print("\n")
# print(a.openning("json/file.json"))
# a.killing("json/file.json", "Two")


# with open("json/file.json", "w") as file:
#     json.dump(tasks, file)
