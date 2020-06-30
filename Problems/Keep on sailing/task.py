# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self, destination):
        print("The {name_of_the_ship} has sailed for {city}!".format(name_of_the_ship=self.name, city=destination))


black_pearl = Ship("Black Pearl", 800)
city_name = input()
black_pearl.sail(city_name)
