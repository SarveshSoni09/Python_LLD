from abc import ABC, abstractmethod


class CoffeeDecorator(ABC):
    pass


class ExtraSugarDecorator(CoffeeDecorator):
    pass


class CaramelSyrumDecorator(CoffeeDecorator):
    pass
