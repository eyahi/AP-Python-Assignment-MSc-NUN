#a)
class User():
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('John', 'Doe', '25', 'john.doe@email.com')
user2 = User("Jane", "Smith", 30, "jane.smith@email.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

#b)
user = User("Alice", "Johnson", 28, "alice.j@email.com")
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")

#c)
class Admin(User):
    def init(self, first_name, last_name, age, email):
        super().init(first_name, last_name, age, email)
        self.privileges = []
 
    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

najib = Admin("Admin", "User", 35, "admin.user@email.com")
najib.describe_user()
najib.privileges = ['\ncan reset password','can add post','can review post']
najib.show_privileges()