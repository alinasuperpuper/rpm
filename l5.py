from abc import ABC, abstractmethod


class Engine(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class GasolineEngine(Engine):
    def start(self):
        print('бензиновый двигатель запущен')

    def stop(self):
        print('бензиновый двигатель остановлен')


class ElectricEngine(Engine):
    def start(self):
        print('электрический двигатель запущен')

    def stop(self):
        print('электрический двигатель остановлен')


class HybridEngine(Engine):
    def start(self):
        print('гибридный двигатель запущен')

    def stop(self):
        print('гибридный двигатель остановлен')


class Vehicle(ABC):
    def __init__(self, engine: Engine):
        self.engine = engine

    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):

        print('машина начинает движение')
        self.engine.start()

        print('машина движется..')
        self.engine.stop()


class Bike(Vehicle):
    def drive(self):
        print('велосипед начинает движение')
        self.engine.start()

        print('велосипед движется..')
        self.engine.stop()


gasoline_car = Car(GasolineEngine())
gasoline_car.drive()
print()

electric_bike = Bike(ElectricEngine())
electric_bike.drive()
print()


hybrid_car = Car(HybridEngine())
hybrid_car.drive()
