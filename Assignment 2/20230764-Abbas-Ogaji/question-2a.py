class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        print('Users names are {} {}, and a {} years old {}'.format(self.first_name, self.last_name, self.age, self.gender))

    def greet_user(self):
        print('Good day, {} {}'.format(self.first_name, self.last_name))

    
user_one = User('Abbas', 'Ogaji', 25, 'male')
user_one.describe_user()
user_one.greet_user()

user_two = User('John', 'doe', 33, 'male')
user_two.describe_user()
user_two.greet_user()

user_three = User('Mary', 'Sikh', 19, 'female')
user_three.describe_user()
user_three.greet_user()