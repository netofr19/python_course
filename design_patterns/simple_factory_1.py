"""
Na POO, o termo factory refere-se a uma classe ou método que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema um sistema com baixo acoplamento entre classes porque ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache ou criação de "singletons" porque a factory pode retornar um objeto já criado para, ao invés de criar novos objetos sempre que o cliente precisar

Desvantagens:
    Podem introduzir muitas classes no código.
"""

from abc import ABC, abstractmethod
from random import choice

class Vehicle(ABC):
    @abstractmethod
    def search_client(self) -> None:
        pass

class LuxuryCar(Vehicle):
    def search_client(self) -> None:
        print("Luxury car is searching the client...")

class SimpleCar(Vehicle):
    def search_client(self) -> None:
        print("Simple car is searching the client...")

class Motorcycle(Vehicle):
    def search_client(self) -> None:
        print("Motorcycle is searching the client...")

class VehicleFactory:
    @staticmethod
    def get_car(type: str) -> Vehicle:
        if type == 'luxury':
            return LuxuryCar()
        if type == 'simple':
            return SimpleCar()
        if type == 'motorcycle':
            return Motorcycle()
        assert 0, "Vehicle doesn't exist."

if __name__ == "__main__":
    disponible_cars = ['luxury', 'simple', 'motorcycle']

    for i in range(10):
        car = VehicleFactory.get_car(choice(disponible_cars))
        car.search_client()