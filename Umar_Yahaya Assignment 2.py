#!/usr/bin/env python
# coding: utf-8

# In[47]:


# Name: UMAR YAHAYA
# ID 20222993
# ASSIGNMENT 2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Creating instances of the Restaurant class
restaurant = Restaurant("Foodie Haven", "International")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Creating three different instances of the Restaurant class
restaurant1 = Restaurant("Burger Palace", "Fast Food")
restaurant2 = Restaurant("Pasta Paradise", "Italian")
restaurant3 = Restaurant("Sushi Delight", "Japanese")

# Calling describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# Adding attributes to the Restaurant class and testing methods
restaurant.number_served = 50
print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(100)
print(f"Updated number of customers served: {restaurant.number_served}")

restaurant.increment_number_served(30)
print(f"After incrementing, number of customers served: {restaurant.number_served}")

# Creating an instance of the IceCreamStand class
ice_cream_stand = IceCreamStand("Sweet Treats", "Dessert", ["Vanilla", "Chocolate", "Strawberry"])

# Calling methods for the IceCreamStand instance
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()


# In[39]:


class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"User Information:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")


user1 = User("John", "Doe", 25, "john.doe@example.com")
user2 = User("Jane", "Smith", 30, "jane.smith@example.com")
user3 = User("Bob", "Johnson", 28, "bob.johnson@example.com")

# Calling methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()


# In[41]:


class User:
    def __init__(self, username):
        self.username = username
        self.login_attempts = 0


    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


        user_instance = User("example_user")


user_instance.increment_login_attempts()
user_instance.increment_login_attempts()
user_instance.increment_login_attempts()


        print(f"Login Attempts: {user_instance.login_attempts}")


        user_instance.reset_login_attempts()


        print(f"Login Attempts after reset: {user_instance.login_attempts}")


# In[38]:


class User:
    def __init__(self, username):
        self.username = username

class Privileges:
    def __init__(self):
        self.privileges_list = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges_list:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, username):
        super().__init__(username)
        self.privileges = Privileges()

admin_user = Admin("admin_user")
admin_user.privileges.show_privileges()


# In[ ]:




