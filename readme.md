## Link to Github Repo

[View the repo on GitHub](https://github.com/JRBoland/T1A3-Terminal-Application)

### Styling

[PEP8](https://peps.python.org/pep-0008/) Styling was used. 
    -- how was it used? small para

### Referenced sources

- Ed
- Documentation
- Youtube
- Classes



# Dog Shelter Feeding Helper

- Application to manage a dog shelter’s daily feeding schedule - keeping track of the feeding & the dietary information of dogs that come in.
- *The ‘fed’ status of the dog will reset each day*. The dogs name & information will be assigned a ‘DoggyID’ and remain in the database until it has been deleted (adopted).
    
    ## List of features
    
    **Continuity message to indicate to user if fed count has been reset.**
        
        ![Untitled](T1A3%20TERMINAL%20a6d3f23e6e7046539137cd6cb93503d2/Untitled.png)
        
    - On opening the application, a message will indicate if the fed count has been reset (new day) or carried on from last session (same day)

    **Display of count of dogs in shelter, count of dogs that have been fed**
    *(eg. 15/20 dogs have been fed today). Count of dogs that have been fed will reset on a new day*.
        
        ![Untitled](T1A3%20TERMINAL%20a6d3f23e6e7046539137cd6cb93503d2/Untitled%201.png)
        
        ![Untitled](T1A3%20TERMINAL%20a6d3f23e6e7046539137cd6cb93503d2/Untitled%202.png)
        
    - Using a separate file `date.txt`, a date in `%a %b %d` fmt (seen below) will be checked and compared with the systems date. If it’s the same day, the fed counter remains the same from the last session. If it is a different day, the fed counter will reset to 0, done by changing all of the ‘Fed’ key values to ‘No’ in the json file `dogsdb.json` on recognition of it being a different date. In both situations, `date.txt` is written over and replaced with the current date at time of use. 
    - If all dogs are fed, the user gets a message on the display indicating that all dogs have been fed today.

    **Menu to view which actions the user wishes to take. Entering an input takes the user to that menu option.**

    - Includes some error handling to catch index or value errors, accounting for the user inputting an invalid option.

    **Menu options include:**

    1. **View dogs & information (including dietary requirements/ in readable format)**
        
        ![Untitled](T1A3%20TERMINAL%20a6d3f23e6e7046539137cd6cb93503d2/Untitled%203.png)
        
        ![Untitled](T1A3%20TERMINAL%20a6d3f23e6e7046539137cd6cb93503d2/Untitled%204.png)
        
        - Uses `tabulate` to show the dogs in an easily viewable format, looping through and pulling the key value pairs stored in the `dogsdb.json` file.
    
    2. **Add a dog & its information to the database** 
        
        ![Untitled](T1A3%20TERMINAL%20a6d3f23e6e7046539137cd6cb93503d2/Untitled%205.png)
        
        - User can add a new dog to the shelter, entering its ‘name’, ‘breed’, ‘medical and dietary requirements’ (yes/no), ‘details of medical & dietary requirement’ and whether or not the dog has been ‘fed’. This information is stored in the dictionary format (in the case of the add dog menu; ‘prompt’: ‘answer’) and is stored in a separate json file `dogsdb.json` and used in conjunction with the python package `tinydb`. 
        - User can exit back to main menu at any time by typing exit.
        - Little error handling as user has freedom to answer how they would prefer. User can type ‘exit’’ at any time to exit back to main menu. ‘0’ option to return to menu does not work on the add dog page. Should be adjusted that the ‘0’ to return to menu option is implemented when user is at the name/breed fields.
        - Next addition *Nice to have* would be to have empty answers return “N/A” or something to that effect. Additionally, a user can input a new record which is all empty. This issue needs to be fixed.
        
    3. **Edit dog information in database**
        
        ![Untitled](T1A3%20TERMINAL%20a6d3f23e6e7046539137cd6cb93503d2/Untitled%206.png)
        
        - Using view dogs from above, the user can enter in an identifier ‘DoggyID’ to select a dog from the database and change their information. 
        - Using tinydb, a record is matched.
        - User gets a secondary menu with prompts of which key value they would like to change. Users new response overrides previous value for the selected key (menu option), which is then updated in the database.
    
    4. **Update the fed status of a dog**
        
        ![Untitled](T1A3%20TERMINAL%20a6d3f23e6e7046539137cd6cb93503d2/Untitled%207.png)

        - Very similar process to menu option 3, however streamlined to update fed status. As with all other ways to update the fed status of the dogs, changing ‘fed’ value will update the fed count display.
        - User gets yes/no option to update a dogs fed status.
        - New page appears confirming change of value.
    
    5. **View dogs still to be fed**
        
        ![Untitled](T1A3%20TERMINAL%20a6d3f23e6e7046539137cd6cb93503d2/Untitled%208.png)
        
        ![Untitled](T1A3%20TERMINAL%20a6d3f23e6e7046539137cd6cb93503d2/Untitled%209.png)
        
        - Returns the dogs that need to be fed, and gives the user the option to go to the ‘mark dog as fed’ menu option or return to main menu.
        - Uses same functionality as view dogs menu option, however filters out to only show dogs with the ‘Fed’ key value of ‘No’. 
    
    6. **Remove a dog from the shelter**
    
    ###########
    
    7. **Exit the application**
    
    #########

### Implementation 

Implementation plan 
- Outlines how each feature will be implemented and a checklist of tasks for each feature 
    - Trello board checklist
- Trello board prioritisation
- Trello deadline/duration

Tracked this plan

- other things that i came across

Trello screenshots

![flowchart](./t1a3_flowchart.pdf)

### Help documentation

- Describe how to use and install the application
    - steps to install the application
    - any dependencies required by the application to operate
    - any system/hardware requirements
    - how to use any command line arguments made for the application 

### SLIDE DECK

Slides must include:
1. An overview of terminal application
    - Must explain: Main features and overall structure

2. An overview of code:
    - Must explain: Explanation of important parts of code, including any crucial application logic 