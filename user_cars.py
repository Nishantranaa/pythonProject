"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    # TODO: Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo = Car(100)
    # TODO: Add 20 more units of fuel to this new car object using the add method
    limo.add_fuel(20)
    # TODO: Attempt to drive the car 115km using the drive method.
    limo.drive(153)
    my_car.drive(30)  # returns distance of 30km
    print("fuel =", my_car.fuel)  # prints 150l
    print("odo =", my_car.odometer)  # prints 30km
    print(my_car)  # prints that my_car is an object
    print(limo)  # prints that limo is an object
    # TODO: Print the amount of fuel in the limo car.
    print("fuel in limo", limo.fuel)

    print("Limo {}, {}".format(limo.fuel, limo.odometer))
    print("Car {}, {}".format(my_car.fuel, my_car.odometer))  # prints 150 and 30km using local object
    print("Car {self.fuel}, {self.odometer}".format(self=limo))  # prints 150l and 30km


main()
