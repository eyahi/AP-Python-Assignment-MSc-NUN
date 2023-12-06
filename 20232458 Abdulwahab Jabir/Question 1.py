my_name = 'Jabir Abdulwahab'
print(f"Hello {my_name}, I am taking some python classes?\n")

print(f"Lowercase: {my_name.lower()}")
print(f"Uppercase: {my_name.upper()}")
print(f"Titlecase: {my_name.title()}")

print(f"\nRepeated Lowercase: {my_name.lower()} {my_name.lower()}")
print(f"Reapeted Uppercase: {my_name.upper()} {my_name.upper()}")
print(f"Reapeted Titlecase:  {my_name.title()}  {my_name.title()}")

fame_person = '\nJ. Robert Oppenheimer'
quote = "Now I am become Death, the destroyer of worlds."

message = f'{fame_person} once said, "{quote}" '
print(message)

names = ["Najeeb", "Abbas", "Ibrahim"]
for name in names:
    print(f"\nHello {name}, What did you learn in today's class!")