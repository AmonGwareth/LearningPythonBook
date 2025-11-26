# practice inheritance

class Engine:

    def start(self):
        print("tack tack started")
        pass

    def stop(self):
        pass


class ElectricEngine(Engine):
    pass


class V8Engine(Engine):
    pass


class Car:
    engine_cls = Engine

    def __init__(self):
        self.engine = self.engine_cls()

    def start(self):
        print(f"Starting {self.engine.__class__.__name__} for", f"{self.__class__.__name__} ... Wrooom, wroom!")
        self.engine.start()

    def stop(self):
        self.engine.stop()


class RaceCar(Car):
    engine_cls = V8Engine


class CityCar(Car):
    engine_cls = ElectricEngine


class F1Car(RaceCar):
    pass
