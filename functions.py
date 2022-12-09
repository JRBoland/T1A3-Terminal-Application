#make sure you use pep8 styling!
fed_dog_count_main = 0
total_dogs_count_main = 0
dogs = {}

def fed_dog_count_tally():
    print("\n\n_______________________________________")
    print("Number of dogs that have been fed today: " + str(fed_dog_count_main) + "/" + str(total_dogs_count_main) + ".\n")
#\nXX total meals to be prepared.\nx meals to contain special dietary requirements.\n_______________________________________\n")
    print("_______________________________________\n\n")

def main_menu():
    fed_dog_count_tally()
    print("1. View dogs in shelter")
    print("2. Add dog information")
    print("3. Edit dog information")
    print("4. Mark a dog as fed")
    print("5. View dogs still to be fed")
    print("6. Delete dog from database")
    print("7. Exit")
    while True:
        try:
            selection = int(input("\n\nEnter menu choice: "))
            if selection == 1:
                view_dogs()
                break
            elif selection == 2:
                add_new_dog()
                break
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
            print("Invalid choice. Please enter 1-7.")
    exit()

def view_dogs():
    print("*** View Dogs ***")
    for dog_id, dog_info in dogs.items():
        print("\nDog", dog_id + 1,":\n_______________________________________")
        for key in dog_info:
            print(key + ":\n", dog_info[key],)
            print("_______________________________________")
    filler_pass = input("\n\nPress any key & hit enter to return to main menu: ")
    main_menu()


def add_new_dog():
    
    fed_dog_count = 0
    print("\n*** Add dog information ***")
    while True:
        new_dog = {}
        name = input("\nWhat is the dogs name?: ")
        breed = input("Breed: ")
        medical_requirements = input("Any medical or dietary requirements? Y/N: ")
        #print(yes_or_no(medical_requirements))
        
        if medical_requirements.lower().startswith("y") and len(medical_requirements) < 5:
            medical_requirements = "Yes"
        elif medical_requirements.lower().startswith("n") and len(medical_requirements) < 5:
            medical_requirements = "No"
        else:
            medical_requirements = medical_requirements
        
        if medical_requirements == "Yes":
            requirement_info = input("Details of medical/dietary requirement: ")
        else:
            requirement_info = "N/A"
            
            #new_dog["Requirement information"] = requirement_info

        has_been_fed = input("Has this dog been fed today?: ")
        if has_been_fed.lower().startswith("y") and len(has_been_fed) < 5:
            has_been_fed = "Yes"
        elif has_been_fed.lower().startswith("n") and len(has_been_fed) < 5:
            has_been_fed = "No"
        else:
            has_been_fed = has_been_fed
        
        if has_been_fed == "Yes":
            fed_dog_count += 1
        
        new_dog["Name"] = name
        new_dog["Breed"] = breed
        new_dog["Medical/dietary requirements"] = medical_requirements
        new_dog["Details of medical/dietary requirement"] = requirement_info
        new_dog["Has " + name + " been fed today?"] = has_been_fed
   
        new_dog_count = len(dogs)
        dogs[new_dog_count] = new_dog
        
        global fed_dog_count_main, total_dogs_count_main
        fed_dog_count_main += fed_dog_count
        total_dogs_count_main += new_dog_count
        #for been_fed_prompt in dogs:
        #    been_fed_prompt = Has_been_fed
        #    if been_fed_prompt == "Yes":
        #        fed_dog_count += 1

        #menu_options()
        #break
        
        def new_dog_menu():
            print("\n***********************************")
            print("1. Add a dog to database")
            print("2. View list of recently added dogs")
            print("3. View total list of dogs")
            print("4. Exit to main menu")
            print("***********************************\n")

            new_dog_menu_selection = int(input("Please enter your selection: "))
            try:
                if new_dog_menu_selection == 1:
                    add_new_dog()
                elif new_dog_menu_selection == 2:
                    for dog_id, dog_info in dogs.items():
                        print("\nDog", dog_id + 1,":\n_______________________________________")
                        for key in dog_info:
                            print(key + ":\n", dog_info[key], "\n_______________________________________")
                        print("\n\n *        *        *        *        *")
                    #print("\n\nNew count of dogs is: ", add_new_dog().new_dog_count)
                    new_dog_menu()
                elif new_dog_menu_selection == 3:
                    print("View total list of dogs")
                    new_dog_menu()
                elif new_dog_menu_selection == 4:
                    print("Exiting to main menu...")
                    main_menu()
                else:
                    print("Invalid choice. Enter 1-4")
                    new_dog_menu()
            except ValueError:
                print("Invalid choice. Enter 1-4")
        new_dog_menu()
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

def edit_dog_info():
    print("*** Edit Dog info ***")
    filler_pass = input("Enter anything to return to main menu: ")
    main_menu()

def mark_dog_as_fed():
    print("*** Mark Dog as fed ***")
    filler_pass = input("Enter anything to return to main menu: ")
    main_menu()

def dogs_to_be_fed():
    print("*** Dogs to be fed ***")
    filler_pass = input("Enter anything to return to main menu: ")
    main_menu()

def remove_dog():
    print("*** Remove dog ***")
    filler_pass = input("Enter anything to return to main menu: ")
    main_menu()
