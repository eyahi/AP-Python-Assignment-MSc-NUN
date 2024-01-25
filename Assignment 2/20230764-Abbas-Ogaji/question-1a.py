class Restaurant:
    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('{}: {}'.format(self.resturant_name, self.cuisine_type))

    def open_restaurant(self):
        print('{} is now opened'.format(self.resturant_name))
    
restaurant = Restaurant('Fatima Foods', 'Donots')
print(restaurant.resturant_name)
print(restaurant.cuisine_type)

restaurant.open_restaurant()
restaurant.describe_restaurant()


restaurant_one = Restaurant('Zahsa lace', 'Soups')
restaurant_one.describe_restaurant()

restaurant_two = Restaurant('Zahsa lace', 'Soups')
restaurant_two.describe_restaurant()

restaurant_three = Restaurant('Trayblaze lunch', 'Rice')
restaurant_three.describe_restaurant()