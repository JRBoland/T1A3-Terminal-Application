#make sure you use pep8 styling
import json
import time
import datetime
from datetime import datetime
import tabulate
#from prettytable import PrettyTable
linebreak_graphic = "_________________________________________________"
starbreak_graphic = "************************************************"
#from pytz import timezone
#from tzlocal import get_localzone

from tinydb import TinyDB, Query
db = TinyDB('dogsdb.json')

User = Query()

#local_tz = tzlocal
#tz = local_tz
#now = datetime.now(tz)
#now = datetime.datetime(2022, 12, 12, 0, 0, 0, 500)
now = datetime.now()
tz_fmt = '%a %b %d %Y \n%H:%M:%S'

#print(now())

def update_to_no():
    results = db.search(User.Fed == 'Yes')
    for res in results: 
        res['Fed'] = 'No'
    db.update({'Fed': 'No'}, Query().Fed.exists())
#    db.update(results)

if (now.hour == 0 and now.minute == 0 and now.second == 0): 
    update_to_no()


total_dogs_count_main = len(db)

dogs = {}
dogs = db.all()

fed_dog_count_main = 0
current_id = int()
dog_id = current_id

def return_to_main():
    filler_pass = input("\n\nHit 'enter' to return to main menu. \n")
    main_menu()

def return_to_main_option():
    while True:
        filler_pass = input("\n\nHit 'enter' to return to main menu or type 'cont' to continue. \n")
        if filler_pass == 'cont':
            break
        else:
            main_menu()


def fed_dog_counter():
    results = db.search(User.Fed == 'Yes')
    db_fed_dog_tally = len(results)
    global fed_dog_count_main
    fed_dog_count_main = db_fed_dog_tally
fed_dog_counter()

def fed_dog_count_tally():
    total_dogs_count_main = len(db)
    fed_dog_counter()
    print("Number of dogs that have been fed today: " + str(fed_dog_count_main) + "/" + str(total_dogs_count_main) + ".")
#\nXX total meals to be prepared.\nx meals to contain special dietary requirements.\n_______________________________________\n")
    

def main_menu():
    print("\n\n" + linebreak_graphic)
    print(now.strftime(tz_fmt) + "\n")
    fed_dog_count_tally()
    print(linebreak_graphic + "\n\n")
    print("1. View dogs in shelter")
    print("2. Add dog information")
    print("3. Edit dog information")
    print("4. Mark a dog as fed")
    print("5. View dogs still to be fed")
    print("6. Delete dog from database")
    print("7. Exit")
    while True:
        try:
            selection = int(input("\n\nEnter menu choice: \n"))
            if selection == 1:
                view_dogs()
                return_to_main()
            elif selection == 2:
                new_dog_menu()
                return_to_main()
            elif selection == 3:
                edit_dog_info()
                break
            elif selection == 4:
                mark_dog_as_fed()
                break
            elif selection == 5:
                dogs_to_be_fed()
                break
            elif selection == 6:
                remove_dog()
                break
            elif selection == 7:
                break
            else:
                print("\n*** INVALID CHOICE ***\n*** Enter 1-7 ***")
                main_menu()
        except ValueError:
            print("Invalid choice. Please enter a valid numerical option.")
    exit()

def view_dogs():
    global dogs
    dogs = db.all()
    try:
        #print(starbreak_graphic + "***********" + starbreak_graphic)
        #print(linebreak_graphic + "View Dogs" + linebreak_graphic)
        #print(starbreak_graphic + "***********" + starbreak_graphic)
        header = dogs[0].keys()
        rows = [x.values() for x in dogs]
        print("\n\n")
        print(tabulate.tabulate(rows,header, tablefmt='grid', maxcolwidths=[None, None]))
        
        #for index in range(len(dogs)):
        #    print("\nDog", key +1, ":\n")
        #    for key,value in dogs[index]:
        #        print(dogs[index][key][value])
        #for dog_id, dog_info in dogs.items():
        #    print("\nDog", dog_id + 1,":\n_______________________________________")
        #    for key in dog_info:
        #        print(key + ":\n", dog_info[key],)
        #        print("_______________________________________")
    except IndexError:
        print(linebreak_graphic)
        print("\nNo dogs currently in shelter")
        print(linebreak_graphic)
        return_to_main()
    

def new_dog_menu():
    print("\n" + starbreak_graphic)
    print("[1] Add a dog to database")
    #print("[2] View list of recently added dogs")
    #print("[3] View total list of dogs")
    print("[2] Exit to main menu")
    print(starbreak_graphic + "\n")
    def add_new_dog():
        print("\n" + starbreak_graphic)
        print("\nAdd dog information")
        print("To return to main menu at any time type 'exit'\n")
        print(starbreak_graphic + "\n")
        while True:
            global dogs, dog_id
            new_dog = {}
            dog_id = len(db) + 1
            name = input("\nWhat is the dogs name?: \n")
            if name.lower() == 'exit':
                main_menu()
            else:
                name = name
            breed = input("Breed: \n")
            if breed.lower() == 'exit':
                main_menu()
            else:
                breed = breed
            medical_requirements = input("Any medical or dietary requirements? Yes/No: \n")
            #print(yes_or_no(medical_requirements))
            
            if medical_requirements.lower().startswith("y") and len(medical_requirements) < 5:
                medical_requirements = "Yes"
            elif medical_requirements.lower().startswith("n") and len(medical_requirements) < 5:
                medical_requirements = "No"
            elif medical_requirements.lower() == 'exit':
                main_menu()
            else:
                medical_requirements = medical_requirements
            
            if medical_requirements == "Yes":
                requirement_info = input("Details of medical/dietary Requirement \n")
                if requirement_info =='exit':
                    main_menu()
                else:
                    requirement_info = requirement_info
            else:
                requirement_info = "N/A"
                
                #new_dog["Requirement information"] = requirement_info
    
            has_been_fed = input("Has " + name + " been fed today?: \n")
            if has_been_fed.lower().startswith("y") and len(has_been_fed) < 5:
                has_been_fed = "Yes"
            elif has_been_fed.lower().startswith("n") and len(has_been_fed) < 5:
                has_been_fed = "No"
            else:
                has_been_fed = has_been_fed
            
            #if has_been_fed == "Yes":
            #    fed_dog_count += 1
            if name == True:
                dog_id += 1

            new_dog["Identifier"] = dog_id
            new_dog["Name"] = name
            new_dog["Breed"] = breed
            new_dog["Medical/Dietary Requirements?"] = medical_requirements
            new_dog["Details of M/D Requirement"] = requirement_info
            new_dog["Fed"] = has_been_fed
            
            
            
            #file.write("Name: ")
            #file.write(name + ", ")
            #file.write("Breed: ")
            #file.write(breed +", ")
            #file.write("Medical/dietary requirements :")
            #file.write(medical_requirements + ", ")
            #file.write("Details of medical/dietary requirement :")
            #file.write(requirement_info + ", ")
            #file.write("Has " + name + " been fed today? :")
            #file.write(has_been_fed + ".\n")
            db.insert(new_dog)
    
            new_dog_count = len(new_dog)
            #dogs[new_dog_count] = new_dog
            #dogs.update(new_dog)
            
            
            #global fed_dog_count_main
             #, has_been_fed_main
            #fed_dog_count += fed_dog_count_main
            #fed_dog_count = fed_dog_count_main
            #has_been_fed_main += has_been_fed
            #for been_fed_prompt in dogs:
            #    been_fed_prompt = Has_been_fed
            #    if been_fed_prompt == "Yes":
            #        fed_dog_count += 1
            print("\nDog added to database: ", name, "\n")
            new_dog_menu()
            #menu_options()
            #break
            
            #______________________
            #new_dog_menu_option = input("\n\n_______________________________________\nNew dog #" + str(new_dog_count) + " entered: " + name + "\n_______________________________________\n\nPlease select next action. \n\n1. Add another dog.\n2. View list of newly added dogs.\n3. View total list of dogs\n4. Exit to main menu.\n\nChoose your answer by typing the appropriate number and hitting enter:  ")
            #if new_dog_menu_option.startswith("1") and len(new_dog_menu_option) < 3:
            #    pass
            #elif new_dog_menu_option.startswith("2") and len(new_dog_menu_option) < 3:
            #    for dog_id, dog_info in dogs.items():
            #        print("\nDog", dog_id,":\n_______________________________________")
            #        for key in dog_info:
            #            print(key + ":\n", dog_info[key], "\n_______________________________________")
            #        print("\n\n *        *        *        *        *")
            #        
            #elif new_dog_menu_option == "3":
            #    print("option 3 not implemented yet")
            #    pass
            #elif new_dog_menu_option == "4":
            #    print("Exiting to main menu...")
            #    main_menu()
            #    break
            #else:
            #    print("exiting to main menu")
            #    break
            #_____________________
            
            #add_another_dog = input("\nWould you like to add another dog? Y/N: ")
            #if not add_another_dog.lower().startswith("y") and len(add_another_dog) < 5:
            #    break
            #need to add an error fix for this, this is error prone^
    
        
        #dict2class
    
        #print("\n\nNew count of dogs is: ", new_dog_count)
        #print("Number of dogs that have been fed today: " + str(fed_dog_count) + "/" + str(len(dogs)) + ".\n")
    
    #add_new_dog()
    #delete a doggy
    #new_dog_count -= 1
    new_dog_menu_selection = int(input("Please enter your selection: \n"))
    try:
        if new_dog_menu_selection == 1:
            add_new_dog()
        #elif new_dog_menu_selection == 2:
        #    for dog_id, dog_info in dogs.items():
        #        print("\nDog", dog_id + 1,":\n_______________________________________")
        #        for key in dog_info:
        #            print(key + ":\n", dog_info[key], "\n_______________________________________")
        #        print("\n\n *        *        *        *        *")
        #    #print("\n\nNew count of dogs is: ", add_new_dog().new_dog_count)
        #    new_dog_menu()
        #elif new_dog_menu_selection == 3:
        #    print("View total list of dogs")
        #    new_dog_menu()
        elif new_dog_menu_selection == 2:
            print("Exiting to main menu...")
            main_menu()
        else:
            print("Invalid choice. Enter 1-2")
            new_dog_menu()
    except ValueError:
        print("Invalid choice. Enter 1-2")
    new_dog_menu()


def edit_dog_info():
    global dogs
    #print("Dogs on file: "+ str(dogs))
    view_dogs()
    
    print("\nDogs on file: \n")
    names = [sub['Name'] for sub in dogs]
    dog_id = [sub['Identifier'] for sub in dogs]
##  
    for dog_id, name in enumerate(names, start=1):
       print("ID: ",dog_id," - ",(name))
        #name += 1

    print("\n\nID:  0  -  Return to main menu")
    
    dog_to_edit = int(input("\nType the ID of dog to edit: \n"))
    if dog_to_edit == 0:
        main_menu()
    if dog_to_edit <= int(dog_id):
        print(starbreak_graphic)
        print("\nYou have chosen ID: " + str(dog_to_edit) + " - " + (dogs[dog_to_edit - 1]['Name']) + ".")
        continue_pass = input("Hit 'enter' if correct. Type 'back' to return to choose a different dog or 'exit' to return to the main menu. \n")
        print(starbreak_graphic)
        if continue_pass.lower() == 'back':
            edit_dog_info()
        elif continue_pass.lower() == 'exit':
            main_menu()
        else: 
            pass

    def edit_dog_info_menu():
        print("\n")
        print("[1] Name")
        print("[2] Breed")
        print("[3] Medical/Dietary requirements")
        print("[4] Details of medical/dietary requirement")
        print("[5] Has been fed today")
        print("[6] Return to main menu")
        selection = int(input("\nPlease choose from above what you would like to edit: \n"))
        if selection == 1:
            edit_name = input("\nWhat would you like to update the dogs name to?: \n")
            db.update({'Name': edit_name}, User.Identifier == int(dog_to_edit))
            print("\nUpdated Dog " + str(dog_to_edit) + " name to: \n" + edit_name + "\n")
            edit_dog_info_menu()
        elif selection == 2:
            edit_breed = input("\nWhat would you like to update the dogs breed to?: \n")
            db.update({'Breed': edit_breed}, User.Identifier == int(dog_to_edit))
            print("\nUpdated Dog " + str(dog_to_edit) + " breed to: \n" + edit_breed + "\n")           
            edit_dog_info_menu()
        elif selection == 3:
            edit_mdr = input("\nDoes this dog still have any medical requirements?: \n")
            if edit_mdr.lower().startswith("y") and len(edit_mdr) < 5:
                edit_mdr = "Yes"
            elif edit_mdr.lower().startswith("n") and len(edit_mdr) < 5:
                edit_mdr = "No"
            else:
                edit_mdr = edit_mdr
            db.update({'\nMedical/Dietary Requirements?': edit_mdr}, User.Identifier == int(dog_to_edit))
            print("\nUpdated Dog " + str(dog_to_edit) + " has medical/dietary requirements to: \n" + edit_mdr + "\n")           
            edit_dog_info_menu()
        elif selection == 4:
            edit_dmdr = input("\nUpdate details of medical/dietary requirement: \n")
            db.update({'Details of M/D Requirement': edit_dmdr}, User.identifier == int(dog_to_edit))
            print("\nUpdated Dog " + str(dog_to_edit) + " medical/dietary requirement details to: \n" + edit_dmdr + "\n")                      
            edit_dog_info_menu()
        elif selection == 5:
            edit_fed = input("\nHas dog been fed today?: \n")
            if edit_fed.lower().startswith("y") and len(edit_fed) < 5:
                edit_fed = "Yes"
            elif edit_fed.lower().startswith("n") and len(edit_fed) < 5:
                edit_fed = "No"
            else:
                edit_fed = edit_fed
            db.update({'Fed': edit_fed}, User.Identifier == int(dog_to_edit))
            print("\nUpdated Dog " + str(dog_to_edit) + " fed status to: \n" + edit_fed + "\n")                                 
            edit_dog_info_menu()

        #db.update({'Name': }), User.name == dog_to_edit
        ##pull list of dog names and enumerate
        elif selection == 6:
            main_menu()
    edit_dog_info_menu()

def mark_dog_as_fed():
    print("*** Mark Dog as fed ***")
    return_to_main()

def dogs_to_be_fed():
    print("*** Dogs to be fed ***")
    return_to_main()

def remove_dog():
    print("*** Remove dog ***")
    return_to_main()
