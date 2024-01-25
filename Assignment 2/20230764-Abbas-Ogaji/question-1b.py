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
    
restaurant = Restaurant('Fatima Foods', 'Donots')
restaurant.set_number_served(20)
print(restaurant.number_served)

restaurant.increment_number_served(1)
print(restaurant.number_served)