#make sure you use pep8 styling
import json
import time
import datetime
from datetime import datetime
import tabulate
import schedule
#from prettytable import PrettyTable
linebreak_graphic = "_________________________________________________"
starbreak_graphic = "************************************************"
#from pytz import timezone
#from tzlocal import get_localzone
import os
from tinydb import TinyDB, Query

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

clear()
db = TinyDB('dogsdb.json')

User = Query()

#local_tz = tzlocal
#tz = local_tz
#now = datetime.now(tz)
#now = datetime.datetime(2022, 12, 12, 0, 0, 0, 500)
now = datetime.now()
tz_fmt = '%a %b %d %Y \n%H:%M:%S'
tz_fmt_for_check = '%a %b %d'
#print(now())

def update_to_no():
    results = db.search(User.Fed == 'Yes')
    for res in results: 
        res['Fed'] = 'No'
    db.update({'Fed': 'No'}, Query().Fed.exists())
#    db.update(results)

time_of_open = datetime.now()

def check_if_new_day():
    if time_file != now.strftime(tz_fmt_for_check):
        update_to_no() == True
        if update_to_no() is True:
            get_ok = input("Fed count tally has been reset as it is a new day.")

with open('date.txt', mode='r+') as time_file:
    check_if_new_day()
    time_file.write(now.strftime(tz_fmt_for_check) + "\n")
    time_file.close()


print(time_file)


#if (now.hour == 0 and now.minute == 0 and now.second == 0): 
#    update_to_no()



total_dogs_count_main = len(db)

dogs = {}
dogs = db.all()
dog_id = 0
with open('dog_id_count.txt') as f:
    dog_id = f.read()
    f.close()





#dog_id = int()
    
#dog_id = int()

fed_dog_count_main = 0
#current_id = int()
#dog_id = current_id



#dog_id = 0
#dog_id = str()



def linebreak():
    print("\n\n")
    print(linebreak_graphic)

def return_to_main():
    filler_pass = int(input("\n\n[0] - Return to main menu:  \n"))
    try:
        if filler_pass == 0:
            main_menu()
    except:
        print("Invalid input")

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
#fed_dog_counter()

def fed_dog_count_tally():
    total_dogs_count_main = len(db)
    fed_dog_counter()
    print("Number of dogs that have been fed today: " + str(fed_dog_count_main) + "/" + str(total_dogs_count_main) + ".")
#\nXX total meals to be prepared.\nx meals to contain special dietary requirements.\n_______________________________________\n")

def fed_dog_count_hero_banner():
    clear()
    print("\n\n" + linebreak_graphic)
    print(now.strftime(tz_fmt) + "\n")
    fed_dog_count_tally()
    print(linebreak_graphic + "\n\n")


def main_menu():
    clear()
    #print("\n\n" + linebreak_graphic)
    #print(now.strftime(tz_fmt) + "\n")
    #fed_dog_count_tally()
    #print(linebreak_graphic + "\n\n")
    fed_dog_count_hero_banner()
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
                main_menu()
        except ValueError:
            filler_continue = input("Invalid choice. Please enter a valid numerical option.")
            main_menu()
    exit()

def view_dogs():
    clear()
    fed_dog_count_hero_banner()
    global dogs
    dogs = db.all()
    try:
        #print(starbreak_graphic + "***********" + starbreak_graphic)
        #print(linebreak_graphic + "View Dogs" + linebreak_graphic)
        #print(starbreak_graphic + "***********" + starbreak_graphic)
        header = dogs[0].keys()
        rows = [x.values() for x in dogs]
        print("")
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
    clear()
    fed_dog_count_hero_banner()
    print("\n" + starbreak_graphic)
    print("[1] Add a dog to database")
    print("[0] Exit to main menu")
    print(starbreak_graphic + "\n")
    def add_new_dog():
        clear()
        print("\n" + starbreak_graphic)
        print("\nAdd dog information")
        print("To return to main menu at any time type 'exit'\n")
        print(starbreak_graphic + "\n")
        while True:
            global dogs, dog_id
            new_dog = {}
            
            #file = open('dog_id_count.txt', 'r')
            #dog_id = file.readlines()
            #file.close()
            #dog_id = file
            #file.close()
            
            #file.close()            

            #

            file = open('dog_id_count.txt', 'r+')
            dog_id = int(dog_id)
            #for i in range(dog_id):
            #    i = 1
            dog_id += 1
            file.write(str(dog_id))
            file.close()
            
            #for i in dogs:
            #    print(i)
            #print(dogs)
            #print(db)
            #dog_id = len(db) + 1
            linebreak()

            name = input("\nWhat is the dogs name?: \n")
            if name.lower() == 'exit':
                clear()
                main_menu()
            else:
                name = name
            linebreak()

            breed = input("Breed: \n")
            if breed.lower() == 'exit':
                clear()
                main_menu()
            else:
                breed = breed
            linebreak()

            medical_requirements = input("Any medical or dietary requirements? Yes/No: \n")
            if medical_requirements.lower().startswith("y") and len(medical_requirements) < 5:
                medical_requirements = "Yes"
            elif medical_requirements.lower().startswith("n") and len(medical_requirements) < 5:
                medical_requirements = "No"
            elif medical_requirements.lower() == 'exit':
                main_menu()
            else:
                medical_requirements = medical_requirements
            linebreak()
            
            if medical_requirements == "Yes":
                requirement_info = input("Details of medical/dietary Requirement \n")
                linebreak()
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
            linebreak()
            
            #if has_been_fed == "Yes":
            #    fed_dog_count += 1
            if name == True:
                dog_id += 1
                return dog_id
                

            
            new_dog["EntryID"] = dog_id
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
        elif new_dog_menu_selection == 0:
            print("Exiting to main menu...")
            main_menu()
        else:
            print("Invalid choice. Enter 1-2")
            new_dog_menu()
    except ValueError:
        again =input("Invalid choice. Enter 1-2")
        new_dog_menu()


def edit_dog_info():
    clear()
    global dogs
    #print("Dogs on file: "+ str(dogs))
    view_dogs()
    
    #print("\nDogs on file: \n")
    #names = [sub['Name'] for sub in dogs]
    #dog_id = [sub['EntryID'] for sub in dogs]
##  
    #for dog_id, name in enumerate(names, start=1):
    #   print("ID: ",dog_id," - ",(name))
        #name += 1
    #print("\n\n")
    #print("[0]  -  Return to main menu")

    #dog_to_dlt = int(input("\nEnter the EntryID of the dog to be removed from database: \n"))
    #dog_rec_to_dlt = db.get(User.EntryID == int(dog_to_dlt))
    #if dog_to_dlt in db.get(User.EntryID == str(dog_to_dlt)):
        #print(db.get(User.EntryID == str(dog_to_dlt)))
    #print("\nYou have chosen ID: " + str(dog_to_dlt) + " - " + (dog_rec_to_dlt['Name']) + ".\n\n")
    #dog_to_dlt = int(input("\nEnter the EntryID of the dog to be removed from database: \n"))
    #dog_rec_to_dlt = db.get(User.EntryID == int(dog_to_dlt))
    #if dog_to_dlt in db.get(User.EntryID == str(dog_to_dlt)):
        #print(db.get(User.EntryID == str(dog_to_dlt)))
    #print("\nYou have chosen ID: " + str(dog_to_dlt) + " - " + (dog_rec_to_dlt['Name']) + ".\n\n")
    #print("\nYou have chosen ID: " + str(dog_to_dlt) + " - " + (dogs[dog_to_dlt - 1]['Name']) + ".\n\n")
    #continue_pass = input("Hit 'enter' if correct. Type 'back' to return to choose a different dog or 'exit' to return to the main menu. \n")



    dog_to_edit = int(input("\nType the ID of dog to edit: \n"))
    dog_rec_to_edit = db.get(User.EntryID == int(dog_to_edit))
    if dog_to_edit == 0:
        main_menu()
    else:
        print(starbreak_graphic)
        print("\nYou have chosen ID: " + str(dog_to_edit) + " - " + (dog_rec_to_edit['Name']) + ".")
        continue_pass = input("Hit 'enter' if correct. Type 'back' to return to choose a different dog or 'exit' to return to the main menu. \n")
        print(starbreak_graphic)
        if continue_pass.lower() == 'back':
            edit_dog_info()
        elif continue_pass.lower() == 'exit':
            main_menu()
        else: 
            pass

    def edit_dog_info_menu():
        clear()
        view_dogs()
        print("\n")
        print("[1] Name")
        print("[2] Breed")
        print("[3] Medical/Dietary requirements")
        print("[4] Details of medical/dietary requirement")
        print("[5] Has been fed today")
        print("\n[0] Return to main menu")
        selection = int(input("\nPlease choose from above what you would like to edit: \n"))
        if selection == 1:
            linebreak()
            edit_name = input("\nWhat would you like to update the dogs name to?: \n")
            db.update({'Name': edit_name}, User.EntryID == int(dog_to_edit))
            print("\nUpdated Dog " + str(dog_to_edit) + " name to: \n" + edit_name + "\n")
            edit_dog_info_menu()
        elif selection == 2:
            linebreak()
            edit_breed = input("\nWhat would you like to update the dogs breed to?: \n")
            db.update({'Breed': edit_breed}, User.EntryID == int(dog_to_edit))
            print("\nUpdated Dog " + str(dog_to_edit) + " breed to: \n" + edit_breed + "\n")           
            edit_dog_info_menu()
        elif selection == 3:
            linebreak()
            edit_mdr = input("\nDoes this dog still have any medical requirements?: \n")
            if edit_mdr.lower().startswith("y") and len(edit_mdr) < 5:
                edit_mdr = "Yes"
            elif edit_mdr.lower().startswith("n") and len(edit_mdr) < 5:
                edit_mdr = "No"
            else:
                edit_mdr = edit_mdr
            db.update({'Medical/Dietary Requirements?': edit_mdr}, User.EntryID == int(dog_to_edit))
            print("\nUpdated Dog " + str(dog_to_edit) + " has medical/dietary requirements to: \n" + edit_mdr + "\n")           
            edit_dog_info_menu()
        elif selection == 4:
            linebreak()
            edit_dmdr = input("\nUpdate details of medical/dietary requirement: \n")
            db.update({'Details of M/D Requirement': edit_dmdr}, User.EntryID == int(dog_to_edit))
            print("\nUpdated Dog " + str(dog_to_edit) + " medical/dietary requirement details to: \n" + edit_dmdr + "\n")                      
            edit_dog_info_menu()
        elif selection == 5:
            linebreak()
            edit_fed = input("\nHas dog been fed today?: \n")
            if edit_fed.lower().startswith("y") and len(edit_fed) < 5:
                edit_fed = "Yes"
            elif edit_fed.lower().startswith("n") and len(edit_fed) < 5:
                edit_fed = "No"
            else:
                edit_fed = edit_fed
            db.update({'Fed': edit_fed}, User.EntryID == int(dog_to_edit))
            print("\n\nUpdated Dog " + str(dog_to_edit) + " fed status to: \n" + edit_fed + "\n")                                 
            edit_dog_info_menu()

        #db.update({'Name': }), User.name == dog_to_edit
        ##pull list of dog names and enumerate
        elif selection == 0:
            main_menu()
    edit_dog_info_menu()

def mark_dog_as_fed():
    
    clear()
    global dogs
    #print("Dogs on file: "+ str(dogs))
    view_dogs()
    print(starbreak_graphic)
    print("Mark Dog as fed")
    #print("\nDogs on file: \n")
    #names = [sub['Name'] for sub in dogs]
    #dog_id = [sub['EntryID'] for sub in dogs]
##  #
    #for dog_id, name in enumerate(names, start=1):
    #   print("ID: ",dog_id," - ",(name))
    #    #name += 1
#
    #print("\n\nID:  0  -  Return to main menu")
    print(starbreak_graphic)

    
    
    dog_to_edit = int(input("\nType the ID of dog to mark as fed: \n"))
    
    if dog_to_edit == 0:
        main_menu()
    if dog_to_edit <= int(dog_id):
        clear()
        print(starbreak_graphic)
        print("\nYou have chosen ID: " + str(dog_to_edit) + " - " + (dogs[dog_to_edit - 1]['Name']) + ".")
        print(starbreak_graphic)
    is_fed = input("\nType Y/Yes if " + (dogs[dog_to_edit - 1]['Name']) + " has been fed today.\nType N/No if " + (dogs[dog_to_edit - 1]['Name']) + " has not been fed today: \n")
    if is_fed.lower().startswith("y") and len(is_fed) < 5:
        is_fed = "Yes"
    elif is_fed.lower().startswith("n") and len(is_fed) < 5:
        is_fed = "No"
    else: 
        print("Please try again ")
        return_to_main()
    #is_fed = input("\nHas dog been fed today?: \n")
    ##if is_fed.lower().startswith("y") and len(is_fed) < 5:
    #    is_fed = "Yes"
    #elif is_fed.lower().startswith("n") and len(is_fed) < 5:
    #    is_fed = "No"
    #else:
    #    is_fed = is_fed
    clear()
    db.update({'Fed': is_fed}, User.EntryID == int(dog_to_edit))
    print("\nUpdated Dog " + str(dog_to_edit) + " fed status to: \n" + is_fed + "\n")  
    print("\n" + starbreak_graphic)
    print("[1] Mark another dog as fed")
    #print("[2] View list of recently added dogs")
    #print("[3] View total list of dogs")
    print("[2] Exit to main menu")
    print(starbreak_graphic + "\n")                               
    next_is_fed = int(input("Choose next action: "))
    if next_is_fed == 1:
        mark_dog_as_fed()
    elif next_is_fed == 2:
        main_menu()
    else:
        print("Please try again")

    
    return_to_main()

def dogs_to_be_fed():
    clear()
    print(starbreak_graphic)
    print("Dogs to be fed")
    def dogs_to_be_fed_view():
        
        fed_dog_count_hero_banner()
        global dogs
        dogs = db.all()
        try:
        #print(starbreak_graphic + "***********" + starbreak_graphic)
        #print(linebreak_graphic + "View Dogs" + linebreak_graphic)
        #print(starbreak_graphic + "***********" + starbreak_graphic)
            to_be_fed_output = {}
            to_be_fed_output = db.search(User.Fed == 'No')
            print(tabulate.tabulate(to_be_fed_output,headers="keys", tablefmt='grid', maxcolwidths=[None,None])) #maxcolwidths=[None, None]))
            #header = dogs[0].keys()
            #rows = [x.values() for x in dogs]#change
            #print(to_be_fed_output)
        
            #print(tabulate.tabulate(rows,header, tablefmt='grid', maxcolwidths=[None, None]))
        
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
    print(starbreak_graphic)
    dogs_to_be_fed_view()
    return_to_main()

def remove_dog():
    clear()
    print("*** Remove dog ***")
    view_dogs()
    #names = [sub['Name'] for sub in dogs]
    #dog_id = [sub['EntryID'] for sub in dogs]
    
    dog_to_dlt = int(input("\nEnter the EntryID of the dog to be removed from database: \n"))
    dog_rec_to_dlt = db.get(User.EntryID == int(dog_to_dlt))
    #if dog_to_dlt in db.get(User.EntryID == str(dog_to_dlt)):
        #print(db.get(User.EntryID == str(dog_to_dlt)))
    print("\nYou have chosen ID: " + str(dog_to_dlt) + " - " + (dog_rec_to_dlt['Name']) + ".\n\n")
    #print("\nYou have chosen ID: " + str(dog_to_dlt) + " - " + (dogs[dog_to_dlt - 1]['Name']) + ".\n\n")
    continue_pass = input("Hit 'enter' if correct. Type 'back' to return to choose a different dog or 'exit' to return to the main menu. \n")
    if continue_pass == "":
        continue_pass_confirm = input("Continuing with this action will permanently delete " + (dog_rec_to_dlt['Name'] + ". Do you wish to continue? \nY/N: "))
        if continue_pass_confirm.lower().startswith("y") and len(continue_pass_confirm) < 5:
            print(starbreak_graphic)
        #dog_to_dlt = input("\nEnter the EntryID of the dog to be removed from database: \n")
            db.remove(User.EntryID == int(dog_to_dlt))
            print("Dog removed: " + str(dog_to_dlt) + " - " + (dog_rec_to_dlt['Name']) + ".")  
            print("Goodbye " + (dog_rec_to_dlt['Name']) + "!!!")  
            print(starbreak_graphic)
        elif continue_pass_confirm.lower().startswith("n") and len(continue_pass_confirm) < 5:
            remove_dog()
        else: 
            remove_dog()             
    elif continue_pass == "back":
        remove_dog()
    elif continue_pass == "exit":
        main_menu()
    else:
        dummy = input("Invalid option, press enter to continue: ")
        remove_dog()
    return_to_main()
