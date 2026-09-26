#University tech fest participant management

#initial list
students=["Aarav","Isha","Rohan","Sneha","Kabir"]

#third student
print("third student:",students[2])

#change rohan to rohan patil
students[2]="Rohan Patil"
print("Updated list 1:",students)

#new students
students.append("Ananya")
students.append("Vihaan")
print("updated list 2:",students)

#remove kabir
students.remove("Kabir")
print("updated list 3:",students)

#total no of registered students
print("total no of registered students:",len(students))

#check for Isha
print("Is Isha registered?","Isha" in students)

#aphabetical order
students.sort()
print("alphabetical order:",students)

#backup
backup_students=students.copy()
print("backup list:",backup_students)

#AI hackathon
hackathon=["Meera","Arjun","Isha"]
print("AI hackathon participants:",hackathon)

#combine both lists
all_participants=students+hackathon
print("all participants:",all_participants)

#display
print("Final list of participants:",all_participants)
print("backup list of participants:",backup_students)
print("combined participants list:",all_participants)