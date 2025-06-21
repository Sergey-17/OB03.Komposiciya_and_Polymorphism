# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
#     и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
#     Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и
#     вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
#     Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
#     (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#Дополнительно:
#Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и
#возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

import pickle
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):

    def make_sound(self):
        print(f"{self.name} поёт")

class Mammal(Animal):       # Млекопитающее
    def make_sound(self):
        print(f"{self.name} Мычит")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} Молчит ;)")

class Human:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Human):        # Сотрудник зоопарка
    def feed_animal(self, animal):
        print(f"{self.name} кормлю {animal.name}")

class Veterinarian(Human):        # Сотрудник зоопарка
    def heal_animal(self, animal):
        print(f"{self.name} лечу {animal.name}")

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.sotrudniki = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное {animal.name} \nсписок животных стал таким:")
        for animal in self.animals:
            print(f"{animal.name}")

    def add_staff(self, sotrudnik):
        self.sotrudniki.append(sotrudnik)
        print(f"Добавлен сотрудник {sotrudnik.name} \nсписок сотрудников стал таким:")
        for s in self.sotrudniki:
            print(f"{s.name}")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


zoo = Zoo("ZooBlag")
bird = Bird("птица", 3)
korova = Mammal("корова", 4)
python = Reptile("питон", 7)
sotrudnik_pertovich = ZooKeeper("Петрович")
veterinar_nikiforovna = Veterinarian("Никифоровна")
zoo.add_animal(bird)
zoo.add_animal(korova)
zoo.add_animal(python)
zoo.add_staff(sotrudnik_pertovich)
zoo.add_staff(veterinar_nikiforovna)
animal_sound(zoo.animals)
veterinar_nikiforovna.heal_animal(korova)
sotrudnik_pertovich.feed_animal(bird)

# Сохраняем в список
zoo_obj = [zoo, bird, korova, python,sotrudnik_pertovich, veterinar_nikiforovna]

# Записываем в файл
with open("zoo_obj.pkl", "wb") as file:
    pickle.dump(zoo_obj, file)

# Загружаем из файла
with open("zoo_obj.pkl", "rb") as file:
    loaded_zoo_obj = pickle.load(file)
# Проверяем правильность загрузки
print("Восстановленные из файла объекты")
for ob in loaded_zoo_obj:
    print(f"Объект {ob.name} класса: {type(ob)}")
