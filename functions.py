
def add_new_dog():
    dogs = {}
    fed_dog_count = 0
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
   
        new_dog_count = len(dogs) + 1
        dogs[new_dog_count] = new_dog

        #for been_fed_prompt in dogs:
        #    been_fed_prompt = Has_been_fed
        #    if been_fed_prompt == "Yes":
        #        fed_dog_count += 1

        #menu_options()
        #break
        new_dog_menu_option = input("\n\n_______________________________________\nNew dog #" + str(new_dog_count) + " entered: " + name + "\n_______________________________________\n\nPlease select next action. \n\n1. Add another dog.\n2. View list of newly added dogs.\n3. View total list of dogs\n4. Exit to main menu.\n\nChoose your answer by typing the appropriate number and hitting enter:  ")
        if new_dog_menu_option.startswith("1") and len(new_dog_menu_option) < 3:
            pass
        elif new_dog_menu_option.startswith("2") and len(new_dog_menu_option) < 3:
            for dog_id, dog_info in dogs.items():
                print("\nDog", dog_id,":\n_______________________________________")
                for key in dog_info:
                    print(key + ":\n", dog_info[key], "\n_______________________________________")
                print("\n\n *        *        *        *        *")
                
        elif new_dog_menu_option == "3":
            print("option 3 not implemented yet")
            pass
        elif new_dog_menu_option == "4":
            print("you have chosen option 4")
            break
        else:
            print("exiting to main menu")
            break
        
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

