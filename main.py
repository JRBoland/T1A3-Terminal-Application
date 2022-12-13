import functions
import os

def begin():
    while True: 
        functions.clear()
        functions.fed_dog_count_hero_banner()
        start = input("Hit enter to begin: \n")
        if start == "":
            return False

functions.clear()
input("Hello!")
begin()
functions.clear()
functions.main_menu()
functions.clear()

#functions.add_new_dog()
#print("\n\nNew count of dogs is: ", functions.add_new_dog().new_dog_count)
#print("Number of dogs that have been fed today: " + str(functions.add_new_dog.fed_dog_count) + "/" + str(len(functions.add_new_dog.dogs)) + ".\n")
