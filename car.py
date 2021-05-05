"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.fuel = fuel  # 180l
        self.odometer = 0  # 0
        self.name = name

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel: # 30km > 180l = false
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance  # 180l - 30 = 150 so self.fuel is now 150l
        self.odometer += distance # 0 + 30  so self.odometer is now 30km
        return distance # returns 30km

# TODO:
# Now add the `__str__` method to the Car class in car.py.
# Using {} string formatting, have it return a string in the following
#    format:
#    `Car, fuel=42, odometer=277`
#   Remember that you can run this method by **print**ing your car
#    object, or passing the car object to the **str()** function.
#    **Do NOT** call the method explicitly like `my_car.__str__()`

    def __str__(self):
        """Return a string representation of a Car object."""
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel, self.odometer)