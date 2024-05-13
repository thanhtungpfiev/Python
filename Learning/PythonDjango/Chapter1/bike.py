# Created by Admin at 5/14/2022
class Bike:
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material

    def brake(self):
        print("Braking!")


red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')

print(red_bike.colour)  # prints: Red
print(red_bike.frame_material)  # prints: Carbon fiber
print(blue_bike.colour)  # prints: Blue
print(blue_bike.frame_material)  # prints: Steel

red_bike.brake()
