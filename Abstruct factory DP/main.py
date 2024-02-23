from abstructFactory import FactoryProducer

producer = FactoryProducer()

bmw_factory = producer.get_factory('BMW')
toyota_factory = producer.get_factory('Toyota')

sedan_car = bmw_factory.create_car('Sedan')
suv_car = toyota_factory.create_car('SUV')

print(sedan_car.info())
print(suv_car.info())