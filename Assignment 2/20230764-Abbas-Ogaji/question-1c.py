class Restaurant:
    number_served = 0

    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
    
    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, increment):
        self.number_served += increment

    def describe_restaurant(self):
        print('{}: {}'.format(self.resturant_name, self.cuisine_type))

    def open_restaurant(self):
        print('{} is now opened'.format(self.resturant_name))

class IceCreamStand(Restaurant):
    def __init__(self, resturant_name, cuisine_type, flavors):
        super().__init__(resturant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        [print(fl) for fl in self.flavors]


ice_scream_stand = IceCreamStand('Hauwa Taste', 'Ice creams', ['vanilla', 'chocolate', 'strawberry', 'oreos'])
ice_scream_stand.display_flavors()