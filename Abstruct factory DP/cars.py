from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def info(self):
        pass

class BMWSedan(Car):
    def info(self):
        return f"This is a BMW Sedan."

class BMWSUV(Car):
    def info(self):
        return f"This is a BMW SUV."

class ToyotaSedan(Car):
    def info(self):
        return f"This is a Toyota Sedan."

class ToyotaSUV(Car):
    def info(self):
        return f"This is a Toyota SUV."