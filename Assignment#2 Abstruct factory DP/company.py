from abstructFactory import AbstractFactory

class ToyotaFactory(AbstractFactory):
    def create_car(self, model):
        from cars import ToyotaSedan, ToyotaSUV
        if model == 'Sedan':
            return ToyotaSedan()
        if model == 'SUV':
            return ToyotaSUV()

class BMWFactory(AbstractFactory):
    def create_car(self, model):
        from cars import BMWSedan, BMWSUV
        if model == 'Sedan':
            return BMWSedan()
        if model == 'SUV':
            return BMWSUV()