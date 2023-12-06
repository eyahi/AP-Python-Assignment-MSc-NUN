guest_list = ['Alamin', 'Tiamiu', 'David']
for guest in guest_list:
    print(f"Dear {guest}, \n\tYou have been invited to my grauation ceremony. I would be happy if you could attend.\n")
    
unavailable_guest = guest_list.pop(1)
print(f"Unfortunately, {unavailable_guest} can't make it to the graduation.\n")

new_guest = "Ronaldo"
guest_list.insert(1, new_guest)

for guest in guest_list:
    print(f"Dear {guest}, \n\tYou have been invited to attend my graduation ceremony.\n")
    
print("Awesome news! I am now allowed to invite more guests to the graduation.")

guest_list.insert(0, 'Joel Embiid')
guest_list.insert(3, 'Micheal Jordan')
guest_list.append('Paris Jackson')

for guest in guest_list:
    print(f"\nDear {guest},\n\tYou are formally invited to my graduation ceremony.\n")
    
print("Due to organizational issues, I can now only invite two people to my graduation.\n")

while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry, {removed_guest}, Unfortunately i can't invite you to the graduation.\n")
    
for guest in guest_list:
    print(f"Dear {guest}, \n\tYou are still invited to my graduation ceremony.\n")
    
guest_list.sort()
print("Guest list sorted alphabetically:", guest_list)

guest_list.reverse()
print("\nGuest list reversed:", guest_list)

del guest_list[-2:]

print("\nThe final guest list:", guest_list)