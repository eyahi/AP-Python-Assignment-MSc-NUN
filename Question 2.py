Invitation_list = ["Dad", "Mom", "Brother"]
for x in Invitation_list:
    print("Dear " + x +"," " I would like to invite you to my Graduation cermony")
print(Invitation_list[2])
Invitation_list[2] = "Sister"
for x in Invitation_list:
    print("Dear " + x +"," " I would like to invite you to my Graduation cermony")
Invitation_list.insert(0, "Cousin")
print(Invitation_list)
Invitation_list.insert(2, "Uncle")
print(Invitation_list)
Invitation_list.append("Aunt")
print(Invitation_list)
print("Hello, " + Invitation_list[0] + " Sequel to the Conversation Regarding the number of invitees to my graduation, i wish inform you that i am inviting you to my graduation ceremony at Nile Universy." )
print("Hello, " + Invitation_list[2] + " Sequel to the Conversation Regarding the number of invitees to my graduation, i wish inform you that i am inviting you to my graduation ceremony at Nile Universy." )
print("Hello, " + Invitation_list[5] + " Sequel to the Conversation Regarding the number of invitees to my graduation, i wish inform you that i am inviting you to my graduation ceremony at Nile Universy." )
for x in Invitation_list:
    print("Dear " + x +"," " I would like to invite you to my Graduation cermony")

for x in Invitation_list:
    print("Dear " + x +"," " I regrettably wish to inforn ypu that due to School managemnt decision the number of guest is now Two, sorry for the inconvienience")
newlist_1 = Invitation_list.pop(5)
print("Sorry for not inviting you", newlist_1)
newlist_2 = Invitation_list.pop(4)
print("Sorry for not inviting you", newlist_2)
newlist_3=Invitation_list.pop(3)
print("Sorry for not inviting you", newlist_3)
newlist_4=Invitation_list.pop(2)
print("Sorry for not inviting you", newlist_4)
print(Invitation_list)
Invitation_list.sort()
print(Invitation_list)
Invitation_list.sort(reverse=True)
print(Invitation_list)
del Invitation_list[0:2]
print(Invitation_list)
