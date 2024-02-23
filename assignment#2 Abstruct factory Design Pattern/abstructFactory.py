from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_car(self, model):
        pass

class FactoryProducer:
    def get_factory(self, company):
        if company == 'BMW':
            from company import BMWFactory
            return BMWFactory()
        if company == 'Toyota':
            from company import ToyotaFactory
            return ToyotaFactory()