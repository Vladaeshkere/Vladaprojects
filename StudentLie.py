import random


class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 1
        self.gladness = 20
        self.alive = True
        self.energy = 50

    def to_study(self):
        print("Я навчаюсь")
        self.progress += 0.1
        self.gladness -= 5
        self.energy -= 10

    def to_sleep(self):
        print("Я пішов спати")
        self.progress += 0.02
        self.gladness += 3
        self.energy += 15

    def to_chill(self):
        print("Я відпочиваю")
        self.gladness += 5
        self.progress -= 0.1
        self.energy += 2

    def play(self):
        print("Я граю в роблокс")
        self.gladness += 10
        self.progress -= 0.4
        self.energy -= 15

    def extra_study(self):
        print("Я дуже сильно навчаюсь")
        self.progress += 0.4
        self.gladness -= 20
        self.energy -= 30

    def hamster_combat(self):
        print("Я тапаю хом'ячка")
        self.progress += 1
        self.gladness += 20
        self.energy += 30

    def info(self):
        print(f"Рівень навчання {round(self.progress, 2)}")
        if self.gladness >= 100:
            self.gladness = 100
        print(f"Задоволення     {self.gladness}")
        if self.energy >= 150:
            self.energy = 150
        print(f"Енергії     {self.energy}")
        print()

    def is_alive(self):
        if self.progress > 5:
            print("Ми все вивчили, і закінчили МКА ШАГ")
            self.alive = False
        if self.progress < -0.5:
            print("Ми втратили інтерес до навчання ....")
            self.alive = False
        if self.gladness <= 0:
            print("У мене дипресія")
            self.alive = False
        if self.energy <= -10:
            print("Ми померли від знесилення")
            self.alive = False

    def live(self, day):
        print(f"День {day} з життя {self.name}")
        print("====================================")
        choice1 = random.randint(1, 3)
        choice2 = random.randint(1, 80)
        choice3 = random.randint(1, 120)
        if choice3 == 1:
            self.hamster_combat()
        else:
            if choice2 == 1:
                self.play()
            elif choice2 == 2:
                self.extra_study()
            else:
                if choice1 == 1:
                    self.to_study()
                elif choice1 == 2:
                    self.to_sleep()
                elif choice1 == 3:
                    self.to_chill()
        self.info()
        self.is_alive()



student = Student("C2121")
for day in range(366):
    if student.alive == False:
        break
    student.live(day)