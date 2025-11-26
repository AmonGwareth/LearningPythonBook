from dataclasses import dataclass


@dataclass # reduces a bit of effort in writing the class
class Body:
    """Class to represent a physical body"""
    name: str
    mass: float = 0.0  # kg
    speed: float = 1.0  # m/s
    # likely not the correct place to add the units here --> think it could be better to write a print method ?
    mass_unit: str = "kg"
    speed_unit: str = "m/s"
    kinetic_energy_unit: str = "J"
    momentum_unit: str = "kg * m/s"

    def kinetic_energy(self) -> float:
        return (self.mass * self.speed**2) / 2

    def momentum(self) -> float:
        return self.mass * self.speed
