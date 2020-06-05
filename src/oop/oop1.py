# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# Vehicle is the base class - everything else builds off of this one.
class Vehicle:
    def __init__(self):
        """ I believe __init__ is auto-added under the hood if you dont define this. But I added it for a more complete understanding."""
        pass

# starting on the ground vehicle path


class GroundVehicle(Vehicle):
    def __init__(self):
        pass


class Car(GroundVehicle):
    def __init__(self):
        pass


class Motorcycle(GroundVehicle):
    def __init__(self):
        pass

# starting on the air vehicle path


class FlightVehicle(Vehicle):
    def __init__(self):
        pass


class Airplane(FlightVehicle):
    def __init__(self):
        pass


class Starship(FlightVehicle):
    def __init__(self):
        pass
