class User():
    def __init__(self, first_name, last_name,other_name,username, email, phone_number):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.other_name = other_name.title()
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nFirst name: {self.first_name} ")
        print(f"Last name: {self.last_name}")
        print(f"Other name: {self.other_name}")
        print(f"Username: {self.username} ")
        print(f"Email: {self.email}")
        print(f"Phone No.: {self.phone_number}")

    def greet_user(self):
        print(f"\nIs good to have you back {self.username}!!!")

    def increment_login_attempts(self):
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts = 0

Ibrahim = User ('ibrahim', 'Ali', 'Zannah', 'Zamac95', 'ibrahimzannhaali@gmail.com', '+2348032632652',) 
Ibrahim.describe_user()
Ibrahim.greet_user()

print("\nInitiating 5 login attempts...")
Ibrahim.increment_login_attempts()
Ibrahim.increment_login_attempts()
Ibrahim.increment_login_attempts()
Ibrahim.increment_login_attempts()
Ibrahim.increment_login_attempts()
print(f"  Login attempts: {Ibrahim.login_attempts}")

print("Resetting login attempts...")
Ibrahim.reset_login_attempts()
print(f"  Login attempts: {Ibrahim.login_attempts}")


Sadiq = User ('Abubakar', 'Ali', 'Zannah', 'ty2043', 'Abubakarzannhaali@gmail.com', '+2348160015999') 
Sadiq.describe_user()
Sadiq.greet_user()

class Admin(User):
    def __init__(self, first_name, last_name,other_name,username, email, phone_number):
        
        super(). __init__(first_name, last_name, other_name, username, email, phone_number) 
        self.priviledges = []

    def show_priviledges(self):
        print(f"\nPriviledges:")
        for priviledge in self.priviledges:
            print(f"{priviledge}")

ibrahim = Admin('ibrahim', 'Ali', 'Zannah', 'Zamac95', 'ibrahimzannhaali@gmail.com', '+2348032632652')
ibrahim.describe_user()
ibrahim.priviledges = [
    '\n***can reset passphrase***',
    '***can add post***',
        '***can delete post***'
]
ibrahim.show_priviledges()