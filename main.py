''' Things I' going to want in this, so like a checklist I guess
[ ] A menu
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

from Diary import Print_Menu
special_message = "Ello der Chuck"
print("\nWelcome to Nikki's Diary\n")
#insert big cool text art thingy saying "Nikki's Diary," "

Print_Menu()
choice = input("Select: ")