''' Things I' going to want in this, so like a checklist I guess
[X] A menu
[ ] A password system perhaps?
[ ] A way to make entries
    [ ] Make Entry as an object or class
    [ ] Manage how to add details like time and day, perhaps a title for the entry
    [ ] A mood tracker perhaps with images?
    [ ] A way to save the entries to be able to load them and resave them
            **** probably the most important really
              **Cause otherwise every time you close the program and reload it it would 
                prolly all be wiped
              **Gonna be a lot of io filestream type things
'''              
          
from DiaryModule import *
import os
os.system('cls')
special_message = "Ello der Chuck"
print("\nWelcome to Nikki's Diary\n")
#insert big cool text art thingy saying "Nikki's Diary," " instead of plain text

#testing entry stuff, it worked
#testing = DiaryEntry()
#print(testing.date,testing.time,testing.title)


#Menu Area
Print_Menu()
choice = input("Select: ")

while choice != 'Q':
  if choice == 'N':
    print("Nothing for now")
  elif choice == 'R':
    print("Nothing for now")
  elif choice == 'V':
    print("Nothing for now")
  os.system('cls')
  print("\nWelcome to Nikki's Diary\n")
  if choice == 'C':
        print(special_message,"\n")
  Print_Menu()
  choice = input("Select: ")
print("\nAdios\n")