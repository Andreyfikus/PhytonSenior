class Human:
    def __init__(self,name):
        self.name = name
    

class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passengers = []


    def add_passenger(self,human):
        self.passengers.append(human)

    def print_passengers(self):
        if self.passengers != []:
            print(f"Name of {self.brand} passengers:")
            for i in self.passengers:
                print(i.name)
        else:
            print(f"There are no passenger in {self.brand}")


nick = Human("Nick")
kate = Human("Kate")

car = Auto("Mersedes")

car.add_passenger(nick)
car.add_passenger(kate)
car.print_passengers()     












import random

class Human:
    def __init__(self,name = "Human", job = None, home = None, car = None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.setiety = 50
        self.job = job
        self.home = home 
        self.car = car

    def get_home(self):
        pass

    def get_car(self):

        pass
    def get_job(self):
        pass

    def eat(self):

        pass
    def work(self):

        pass
    def shopping(self,manage):

        pass
    def chil(self):

        pass
    def clean_home(self):

        pass
    def days_infdex(self,day):
        pass

    def is_alive(self):
        pass

    def live(self,day):
        pass

