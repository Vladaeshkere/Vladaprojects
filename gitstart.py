import random
class Pet:
    def __init__(self, name, colorGene, sizeGene, speedGene):
        self.name = name
        self.happines = 50
        self.colorGene = colorGene
        self.sizeGene = sizeGene
        self.speedGene = speedGene

    def change_mood(self, actions):
        if actions == 'play':
            self.happines += 10
        elif actions == 'ignore':
            self.happines -= 10

        if self.happines > 100:
            self.happines = 100
        elif self.happines < 0:
            self.happines = 0

        print(f"{self.name} тепер щасливий на {self.happines}.")

    def show_mood(self):
        if self.happines > 70:
            print(f'{self.name} щасливий')
        elif 40 < self.happines <= 70:
            print(f'{self.name} нормально себе почуває')
        else:
            print(f'{self.name} сумує')
    def show_genes(self):
        print(f"{self.name} Гени: Колір: {self.colorGene}, Розмір: {self.sizeGene}, Швидкість: {self.speedGene}")
    @staticmethod #означає що не відносіться функція до одного об'єкту класу
    def breed_genes(parent1, parent2):
        babyColor = random.choice([parent1.colorGene, parent2.colorGene])
        babySize = random.choice([parent1.sizeGene, parent2.sizeGene])
        babySpeed = random.choice([parent1.speedGene, parent2.speedGene])

        babyName = 'Baby'

        print(f"{babyName} Гени: Колір: {babyColor}, Розмір: {babySize}, Швидкість: {babySpeed}")

Jack = Pet(name='Jack', colorGene='black', speedGene='Max', sizeGene='small')
Lily = Pet(name='Lily', colorGene='gray', speedGene='medium', sizeGene='large')
Jack.show_genes()
Lily.show_genes()
Pet.breed_genes(Jack, Lily)
Jack.change_mood('play')
Jack.show_mood()