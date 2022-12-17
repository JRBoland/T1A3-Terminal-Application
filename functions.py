import datetime
import tabulate
import pyfiglet
import os
from datetime import datetime
from tinydb import TinyDB, Query

# Constants for graphics/visual compartmentalization
LINEBREAK_GRAPHIC = "__________________________________________________________________________________________________"
STARBREAK_GRAPHIC = "*************************************************"

# Clearscreen function to clear the console when called


def clear():
    os.system("cls" if os.name == "nt" else "clear")


clear()

# Setting the db and search variables using TinyDB module.
db = TinyDB("dogsdb.json")
User = Query()

# Setting the time variables and formats using datetime module.
now = datetime.now()
tz_fmt = "%a %b %d %Y \n%H:%M:%S"
tz_fmt_for_check = "%a %b %d"
time_of_open = datetime.now()

# Function to update all 'fed' results in database to no. To be called if check if new day defaults to else statement


def update_to_no():
    results = db.search(User.Fed == "Yes")
    for res in results:
        res["Fed"] = "No"
    db.update({"Fed": "No"}, Query().Fed.exists())

# If statement to check if date stored in date.txt matches time pulled from datetime module (format inclusive).


def check_if_new_day():
    if ("".join(open("date.txt").read().split("\n"))) == (now.strftime(tz_fmt_for_check)):
        check_today = input(
            "The fed tally has been recovered from last session as it is still the same day as when the dogs were fed.\n\nPress 'enter' to continue.  ")
    else:
        update_to_no()
        get_ok = input(
            "Fed count tally has been reset as it is a new day.\n\nPress 'enter' to continue. ")


# Reads (to check if new day) then writes over the date.txt file to store date when program is ran.
with open("date.txt", mode="r+") as time_file:
    check_if_new_day()
    with open("date.txt", mode="w") as time_file:
        time_file.write(now.strftime(tz_fmt_for_check))
        time_file.close()

# Variables interacting with database so that they can be used in functions throughout the program.
total_dogs_count_main = len(db)
dogs = {}
dogs = db.all()
dog_id = 0

# Reads dog_id_count.txt file to pull unique dog ID.
with open("dog_id_count.txt") as f:
    dog_id = f.read()
    f.close()

fed_dog_count_main = 0

# Alternative of linebreak graphic variable.


def linebreak():
    print("\n")
    print(LINEBREAK_GRAPHIC)

# Alternative of starbreak graphic variable.


def starbreak():
    print("\n")
    print(STARBREAK_GRAPHIC)

# Return to main menu option


def return_to_main():
    print("\n\n\n")
    filler_pass = input("[0] Return to main menu:  \n")
    # Accepts 0 or enter.
    try:
        if filler_pass == "" or "0":
            main_menu()
    except:
        print("Invalid input")

# Pulls fed status from database and updates tally and global variable


def fed_dog_counter():
    results = db.search(User.Fed == "Yes")
    db_fed_dog_tally = len(results)
    global fed_dog_count_main
    fed_dog_count_main = db_fed_dog_tally

# Displays amount of fed dogs. If all dogs are fed then another string is printed.


def fed_dog_count_tally():
    total_dogs_count_main = len(db)
    fed_dog_counter()
    # pyfiglet used to make counter stand out
    print("\nNumber of dogs that have been fed today: \n\n" + (pyfiglet.figlet_format(
        str(fed_dog_count_main) + "  /  " + str(total_dogs_count_main), font="basic",)))

    if str(fed_dog_count_main) == str(total_dogs_count_main):
        print(LINEBREAK_GRAPHIC)
        print("All dogs have been fed for today.")

# Banner for to displaying time and fed tally.


def fed_dog_count_hero_banner():
    clear()
    linebreak()
    print(now.strftime(tz_fmt))
    fed_dog_count_tally()
    print(LINEBREAK_GRAPHIC + "\n")

# Main menu to take input and lead user to page based on input. Includes error handling############need to add more info


def main_menu():

    while True:

        try:
            clear()
            fed_dog_count_hero_banner()
            print("1. View dogs in shelter")
            print("2. Add dog information")
            print("3. Edit dog information")
            print("4. Update fed status")
            print("5. View dogs still to be fed")
            print("6. Delete dog from database")
            print("7. Exit")
            print(LINEBREAK_GRAPHIC)

            selection = input("\n\nEnter menu choice: \n")
            if selection == "1":
                view_dogs()
                print("\nDogs in shelter\n")
                print(LINEBREAK_GRAPHIC)
                return_to_main()
            elif selection == "2":
                new_dog_menu()
                return_to_main()
            elif selection == "3":
                edit_dog_info()
                break
            elif selection == "4":
                mark_dog_as_fed()
                return_to_main()
            elif selection == "5":
                dogs_to_be_fed()
                return_to_main()
            elif selection == "6":
                remove_dog()
            elif selection == "7":
                clear()
                print(pyfiglet.figlet_format("Goodbye!", font="basic"))
                exit_input = input(pyfiglet.figlet_format(
                    "Until\n         Next\n                 Time..."))
                exit()
            else:
                invalid_input_rtm = input(
                    "Invalid input. Please answer with 1-7. \nHit 'enter' to return to main menu.")
                main_menu()

        except (ValueError, IndexError, KeyError) as the_error:
            print(STARBREAK_GRAPHIC)
            value_error_input_rtm = input(
                f"Invalid error {the_error}. Hit 'enter' to return to menu.\n")
            print(STARBREAK_GRAPHIC)
            main_menu()

    exit()

# view dogs


def view_dogs():
    clear()
    fed_dog_count_hero_banner()
    global dogs
    dogs = db.all()

    try:
        header = dogs[0].keys()
        rows = [x.values() for x in dogs]
        print("")
        print(tabulate.tabulate(rows, header,
              tablefmt="grid", maxcolwidths=[None, None]))

    except IndexError:
        print(LINEBREAK_GRAPHIC)
        print("\nNo dogs in here")
        print(LINEBREAK_GRAPHIC)
        return_to_main()

# new dog menu


def new_dog_menu():
    clear()
    print("\n\n")
    print("Add a dog to database.")

    def add_new_dog():
        print("" + LINEBREAK_GRAPHIC)
        print("\nAdd dog information")
        print("To return to main menu at any time type 'exit'\n")

        while True:

            global dogs, dog_id
            new_dog = {}

            file = open("dog_id_count.txt", "r+")
            dog_id = int(dog_id)
            dog_id += 1
            file.write(str(dog_id))
            file.close()
            linebreak()

            name = input("\nWhat is the dogs name?: \n")
            if name.lower() == "exit":
                clear()
                main_menu()
            else:
                name = name
            linebreak()

            breed = input("Breed: \n")
            if breed.lower() == "exit":
                clear()
                main_menu()
            else:
                breed = breed
            linebreak()

            medical_requirements = input(
                "Any medical or dietary requirements? Yes/No: \n")
            if (medical_requirements.lower().startswith("y") and len(medical_requirements) < 5):
                medical_requirements = "Yes"
            elif (medical_requirements.lower().startswith("n") and len(medical_requirements) < 5):
                medical_requirements = "No"
            elif medical_requirements.lower() == "exit":
                main_menu()
            else:
                medical_requirements = medical_requirements
            linebreak()

            if medical_requirements == "Yes":
                requirement_info = input(
                    "Details of medical/dietary Requirement \n")
                linebreak()
                if requirement_info == "exit":
                    main_menu()
                else:
                    requirement_info = requirement_info
            else:
                requirement_info = "N/A"

            has_been_fed = input("Has " + name + " been fed today?: \n")
            if has_been_fed.lower().startswith("y") and len(has_been_fed) < 5:
                has_been_fed = "Yes"
            elif has_been_fed.lower().startswith("n") and len(has_been_fed) < 5:
                has_been_fed = "No"
            else:
                has_been_fed = has_been_fed
            linebreak()

            new_dog["DoggyID"] = dog_id
            new_dog["Name"] = name
            new_dog["Breed"] = breed
            new_dog["Medical/Dietary Requirements?"] = medical_requirements
            new_dog["Details of M/D Requirement"] = requirement_info
            new_dog["Fed"] = has_been_fed

            #if name == True:
            #    dog_id += 1
            #    return dog_id

            db.insert(new_dog)
            #new_dog_count = len(new_dog)
            get_input = input("\nDog added to database: " +
                              name + ".\n\nHit 'enter' to continue.")
            new_dog_menu()

    add_new_dog()

# edit dog menu


def edit_dog_info():
    clear()
    global dogs
    view_dogs()
    print("\n\nEdit Dog information.")
    print(LINEBREAK_GRAPHIC + "\n\n")

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

        selection = input(
            "\nPlease choose from above what you would like to edit: \n")
        if selection == "1":
            linebreak()
            edit_name = input(
                "\nWhat would you like to update the dogs name to?: \n")
            db.update({"Name": edit_name}, User.DoggyID == int(dog_to_edit))
            print("\nUpdated Dog " + str(dog_to_edit) +
                  " name to: \n" + edit_name + "\n")
            edit_dog_info_menu()

        elif selection == "2":
            linebreak()
            edit_breed = input(
                "\nWhat would you like to update the dogs breed to?: \n")
            db.update({"Breed": edit_breed}, User.DoggyID == int(dog_to_edit))
            print("\nUpdated Dog " + str(dog_to_edit) +
                  " breed to: \n" + edit_breed + "\n")
            edit_dog_info_menu()

        elif selection == "3":
            linebreak()
            edit_mdr = input(
                "\nDoes this dog still have any medical requirements?: \n")
            if edit_mdr.lower().startswith("y") and len(edit_mdr) < 5:
                edit_mdr = "Yes"
            elif edit_mdr.lower().startswith("n") and len(edit_mdr) < 5:
                edit_mdr = "No"
            else:
                edit_mdr = edit_mdr
            db.update({"Medical/Dietary Requirements?": edit_mdr},
                      User.DoggyID == int(dog_to_edit))
            print("\nUpdated Dog " + str(dog_to_edit) +
                  " has medical/dietary requirements to: \n" + edit_mdr + "\n")
            edit_dog_info_menu()

        elif selection == "4":
            linebreak()
            edit_dmdr = input(
                "\nUpdate details of medical/dietary requirement: \n")
            db.update({"Details of M/D Requirement": edit_dmdr},
                      User.DoggyID == int(dog_to_edit))
            print("\nUpdated Dog " + str(dog_to_edit) +
                  " medical/dietary requirement details to: \n" + edit_dmdr + "\n")
            edit_dog_info_menu()

        elif selection == "5":
            linebreak()
            edit_fed = input("\nHas dog been fed today?: \n")
            if edit_fed.lower().startswith("y") and len(edit_fed) < 5:
                edit_fed = "Yes"
            elif edit_fed.lower().startswith("n") and len(edit_fed) < 5:
                edit_fed = "No"
            else:
                edit_fed = edit_fed
            db.update({"Fed": edit_fed}, User.DoggyID == int(dog_to_edit))
            print("\n\nUpdated Dog " + str(dog_to_edit) +
                  " fed status to: \n" + edit_fed + "\n")
            edit_dog_info_menu()

        elif selection == "0":
            main_menu()
        else:
            edit_dog_info_menu()

    dog_to_edit = int(input(
        "Type [0] to return to main menu.\n\nEnter the DoggyID of dog to edit: \n"))
    dog_rec_to_edit = db.get(User.DoggyID == int(dog_to_edit))

    if dog_to_edit == 0:
        main_menu()
    if dog_rec_to_edit in db:

        try:
            print(STARBREAK_GRAPHIC)
            print("\nYou have chosen ID: " + str(dog_to_edit) +
                  " - " + (dog_rec_to_edit["Name"]) + ".")
            continue_pass = input(
                "Hit 'enter' if correct. Type 'back' to return to choose a different dog or 'exit' to return to the main menu. \n")
            print(STARBREAK_GRAPHIC)

            if continue_pass == "":
                edit_dog_info_menu()
            elif continue_pass.lower() == "back":
                edit_dog_info()
            elif continue_pass.lower() == "exit":
                main_menu()
            else:
                edit_dog_info()

        except:
            edit_dog_info()

    else:
        edit_dog_info()

# update dog as fed


def mark_dog_as_fed():
    clear()
    global dogs
    view_dogs()

    print("\n\n\n")
    print("Update fed status")
    print(LINEBREAK_GRAPHIC + "\n\n")

    dog_to_edit = int(input(
        "Enter [0] to return to main menu.\n\nEnter the DoggyID of dog to update fed status: \n"))
    dog_rec_to_edit = db.get(User.DoggyID == int(dog_to_edit))
    if dog_to_edit == 0:
        main_menu()
    if dog_rec_to_edit in db:

        try:
            print("\n\n" + STARBREAK_GRAPHIC)
            print("\nYou have chosen ID: " + str(dog_to_edit) +
                  " - " + (dog_rec_to_edit["Name"]) + ".")
            print(LINEBREAK_GRAPHIC + "\n\n")

            is_fed = input("\nType (not case sensitive):\nY/Yes if Yes or N/No if No\n\nHas " +
                           (dog_rec_to_edit["Name"]) + " been fed today?: \n")
            if is_fed.lower().startswith("y") and len(is_fed) < 5:
                is_fed = "Yes"
            elif is_fed.lower().startswith("n") and len(is_fed) < 5:
                is_fed = "No"
            else:
                print("Please try again ")
                return_to_main()

            clear()
            db.update({"Fed": is_fed}, User.DoggyID == int(dog_to_edit))

            print("\nUpdated Dog " + str(dog_to_edit) +
                  " fed status to: \n" + is_fed + "\n")
            print("\n" + STARBREAK_GRAPHIC)
            print("[1] Mark another dog as fed")
            print("[2] Exit to main menu")
            print(STARBREAK_GRAPHIC + "\n")

            next_is_fed = int(input("Choose next action: "))
            if next_is_fed == 1:
                mark_dog_as_fed()
            elif next_is_fed == 2:
                main_menu()
            else:
                print("Please try again")

        except (TypeError, ValueError, KeyError) as error_return_to_main:
            print("\n" + STARBREAK_GRAPHIC)
            print(
                f"Invalid input error '{error_return_to_main}'. Hit 'Enter' to return to main menu.")
            print("\n" + STARBREAK_GRAPHIC)
            return_to_main()

    else:
        mark_dog_as_fed()

# dogs to be fed


def dogs_to_be_fed():
    clear()
    print(STARBREAK_GRAPHIC)
    print("Dogs to be fed")

    def dogs_to_be_fed_view():
        fed_dog_count_hero_banner()
        global dogs
        dogs = db.all()

        try:
            to_be_fed_output = {}
            to_be_fed_output = db.search(User.Fed == "No")
            print(tabulate.tabulate(to_be_fed_output, headers="keys",
                  tablefmt="grid", maxcolwidths=[None, None],))

        except IndexError:
            print("\n" + LINEBREAK_GRAPHIC)
            print("\nNo dogs to be fed")
            print(LINEBREAK_GRAPHIC + "\n\n")
            return_to_main()

    dogs_to_be_fed_view()

    def next_action_update_fed():
        user_to_edit = input("\nEnter your next action: \n")
        if user_to_edit == "1":
            mark_dog_as_fed()
        elif user_to_edit == "0":
            main_menu()
        else:
            dogs_to_be_fed()

    print("\n\nDogs still to be fed")
    print(LINEBREAK_GRAPHIC)
    print("\n\n[1] Go to 'Update fed status of dogs' menu.")
    print("[0] Return to main menu.")

    next_action_update_fed()

# remove dog


def remove_dog():
    clear()
    print("*** Remove dog ***")
    view_dogs()
    print("\nRemove dog from database")
    print(LINEBREAK_GRAPHIC)

    dog_to_dlt = int(input(
        "\n\nType [0] to return to main menu.\n\nEnter the DoggyID of the dog to be removed from database: \n"))
    dog_rec_to_dlt = db.get(User.DoggyID == int(dog_to_dlt))

    if dog_to_dlt == 0:
        main_menu()

    if dog_rec_to_dlt in db:

        try:
            print("\nYou have chosen ID: " + str(dog_to_dlt) +
                  " - " + (dog_rec_to_dlt["Name"]) + ".\n\n")
            continue_pass = input(
                "Hit 'enter' if correct. Type 'back' to return to choose a different dog or 'exit' to return to the main menu. \n")

            if continue_pass == "":
                continue_pass_confirm = input("Continuing with this action will permanently delete " + (
                    dog_rec_to_dlt["Name"] + ". Do you wish to continue? \nY/N: "))
                if (continue_pass_confirm.lower().startswith("y") and len(continue_pass_confirm) < 5):
                    print(STARBREAK_GRAPHIC)
                    db.remove(User.DoggyID == int(dog_to_dlt))
                    print("Dog removed: " + str(dog_to_dlt) +
                          " - " + (dog_rec_to_dlt["Name"]) + ".")
                    print("Goodbye " + (dog_rec_to_dlt["Name"]) + "!!!")
                    return_to_main()
                elif (continue_pass_confirm.lower().startswith("n") and len(continue_pass_confirm) < 5):
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

        except (ValueError, KeyError, NameError, TypeError, IndexError) as type_of_error:
            print(STARBREAK_GRAPHIC)
            value_error_input_rtm = input(
                f"Invalid error {type_of_error}. Hit 'enter' to return to menu.\n")
            print(STARBREAK_GRAPHIC)
            main_menu()
    else:
        inc_input = input("Something went wrong")
