#A
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0


    def describe_restaurant(self): 
        message = f"{self.restaurant_name} serves wonderful {self.cuisine_type}."
        print(f"\n{message}")

    def open_restaurant(self):
        message = f"{self.restaurant_name} is open"
        print(f"\n{message}")

    def set_number_served(self, number_served):
        self.number_served = number_served 
    

    def increment_number_served(self, More_served):
        self.number_served += More_served
        

restaurant = Restaurant('eatwell', 'kilishi')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()


restaurant1 = Restaurant('Maman Aisha', 'Tuwon shinkafa')
restaurant2 = Restaurant('enjoy', 'Egusi')
restaurant3 = Restaurant('Najib\'s Eatery', 'Dan Wake')


restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
print(f"\n")


#B

restaurant = Restaurant("Fine Dining", "French")
print(restaurant.restaurant_name)
print(f"\n")
message=f"Number of Customers served: {restaurant.number_served}"
print(f"{message}")

restaurant.set_number_served(50)
message=f"Updated number of customers served: {restaurant.number_served}"
print(f"{message}")

restaurant.increment_number_served(50)
message=f"Updated number of customers served: {restaurant.number_served}"
print(f"{message}")

#C
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


Cravins = IceCreamStand('Cravins')
Cravins.flavors = ['vanilla', 'chocolate', 'black cherry']

Cravins.describe_restaurant()
Cravins.show_flavors()