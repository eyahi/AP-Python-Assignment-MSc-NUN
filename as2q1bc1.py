class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

h_continental = Restaurant('Hcontinental', 'rice')
h_continental.describe_restaurant()

ibro_fish = Restaurant("ibro fish", 'grilled fish')
ibro_fish.describe_restaurant()

chicken_republic = Restaurant('chicken republic', 'chickwizz')
chicken_republic.describe_restaurant()

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    

najeeb = User('najeeb', 'musa', 'najeeb-ktg', 'najeebmusa77@mail.com', 'abuja')
najeeb.describe_user()
najeeb.greet_user()

ibrahim = User('ibrahim', 'zannah', 'zannahi', 'zannahI@mail.com', 'gwarinpa')
ibrahim.describe_user()
ibrahim.greet_user()
