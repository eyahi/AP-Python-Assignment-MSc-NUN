#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Name:-           Ibrahim Nuhu Aliyu
Exam No.:-       20223023
Department:-     Computer Engineering
Course Tittle:-  Advanced Programming
Course Code:-    CPE 802
Course Tutor:-   Dr. Emmanuel Ali 


# In[25]:


# Q1a
# Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and 
# a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and 
# a method called open_restaurant() that prints a message indicating that the restaurant is open. 
# Make an instance called restaurant from your class. Print the two attributes individually, and
# then call both methods. Create three different instances from the class, and 
# call describe_restaurant() for each instance.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        # the printing method is added just to make the output of the program readable 
        print(" ")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
        # the printing method is added just to make the output of the program readable 
        print(" ")

# Creating an instance called 'restaurant'
restaurant = Restaurant("Ocean Basket", "Pounded Yam")

# Printing individual attributes
print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")

# invoking methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Creating three different instances and calling describe_restaurant() for each
restaurant1 = Restaurant("Metisse Restaurant", "Jollof Rice")
restaurant2 = Restaurant(" Nkoyo Restaurant", "Fried Plantain")
restaurant3 = Restaurant(" Jevinik Restaurant", "Ogbono Soup")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


# In[28]:


# Q1b
# Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of customers that have been served. 
# Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
# Call this method with any number you like that could represent how many customers were served in, say, a day of business.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Number of Customers Served: {self.number_served}")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

# Creating an instance called 'restaurant'
restaurant = Restaurant("Ocean Basket", "Pounded Yam")

# Printing the initial number of customers served
print(f"Number of Customers Served: {restaurant.number_served}")

# Changing the number of customers served and printing again
restaurant.number_served = 50
print(f"Number of Customers Served: {restaurant.number_served}")

# Using the set_number_served() method
restaurant.set_number_served(100)
print(f"Number of Customers Served: {restaurant.number_served}")

# Using the increment_number_served() method
restaurant.increment_number_served(20)
print(f"Number of Customers Served: {restaurant.number_served}")


# In[30]:


# Q1c 
# An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from 
# the Restaurant class. Add an attribute called flavors that stores a list of ice cream flavors. 
# Write a method that displays these flavors. Create an instance of IceCreamStand, 
# and call this method.
 
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        # Call the __init__ method of the base class (Restaurant)
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Ice Cream Flavors are listed below:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Creating an instance of IceCreamStand
ice_cream_stand = IceCreamStand("Scoops & Smiles", "Ice Cream", ["Coffee", "Rasberry Ripple", "Strawberry", "Coconut"])

# Calling the display_flavors() method
ice_cream_stand.display_flavors()


# In[32]:


# Q2a
# Make a class called User. Create two attributes called first_name and last_name, 
# and then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user’s information.
# Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"\nPersonnel Information for {self.first_name} {self.last_name}:")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"\nHello, {self.first_name}! Do Have A Nice Day.")

# Creating instances of the User class
user1 = User("Dr Emmanuel ", "Ali", 34, "emmanuelali@nileuniversity.edu.ng", "Abuja, Nigeria.")
user2 = User("Ibrahim Nuhu", "Aliyu", 29, "20223023@nileuniversity.edu.ng", "Niger State, Borgu")
user3 = User("Jibril", "Halima", 27, "jibrilhalimat@email.com", "Yobe Stae Damaturu")

# Calling methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()


# In[40]:


# Q2b
# Add an attribute called login_attempts to your User class. Write a method called increment_login_attempts() 
# that increments the value of login_attempts by 1. Write another method called reset_login_attempts() 
# that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times. 
# Print the value	of	login_attempts	to	make	sure	it	was	incremented	properly,	
# and	then	call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0  # New attribute for login attempts

    def describe_user(self):
        print(f"\nUser Information for {self.first_name} {self.last_name}:")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"\nHello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Creating an instance of the User class
user1 = User("Dr. Emmanuel", "Ali", 25, "emmanuelali@nileuniversity.edu.ng", "Abuja, Nigeria")

# Calling increment_login_attempts several times
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Printing the value of login_attempts
print(f"Login Attempts: {user1.login_attempts}")

# Calling reset_login_attempts
user1.reset_login_attempts()

# Printing the value of login_attempts after reset
print(f"Login Attempts after reset: {user1.login_attempts}")


# In[41]:


# Q2c
# An administrator is a special kind of user. Write a class called Admin that inherits from the User class. 
# Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", 
# and so on.Write a method called show_privileges() that lists the administrator’s set of privileges. 
# Create an instance of Admin, and call your method. Write a separate Privileges class.
# The class should have one attribute, privileges, that stores a list of strings as described above.
# Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges.

class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nAdmin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, email, location, privileges=[]):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges(privileges)

# Creating an instance of Admin
admin_user = Admin("Admin", "User", 35, "admin.user@email.com", "AdminCity", ["Can Add Post", "Can Delete Post", "Can Ban User"])

# Using the show_privileges method from the Privileges class
admin_user.privileges.show_privileges()


# In[ ]:




