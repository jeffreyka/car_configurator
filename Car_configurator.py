# The model_cost list is where all the infomation from the carModel function is returned to.
# The colour_cost list is where all the infomation from the carColour function is returned to.
# The accessory_cost list is where all the infomation from the carAccessories function is returned to.
# The model string variable is where the model name is stored.
# The colour string variable is where the colour name is stored.
# The colour string variable is where the color type is stored.
# The accessory string variable is where the accessory name is stored.
# The total variable is where the total cost is stored and updated as the user makes selections.
# The option variable is used for the main menu where the user will make a selection.
model_cost = []
colour_cost = []
accessory_cost = []
model = ""
colour = ""
colour_type = ""
accessory = ""
total = 0
option = "0"

# This function gets the user to select the car model they would like and returns the price and the name of the model 
# they have chosen.
def carModel():

    # The model_info list will store the users choice and price.
    # The choose_model string is used for the while loop below.
    model_info = []
    choose_model = "yes"

    # This loop ensures that the user will be repeatedly asked to select an option until they select a valid option.
    while choose_model == "yes":

        choice = input(('''\nPlease select a car model: 
        1. Mustang - £27,000
        2. Chevrolet - £50,000
        3. Ferrari - £200,000
        4. McLaren - £300,000
        
        '''))

        # If the user selects one of the options from the list above, then the corresponding price and name will be added to the list.
        # The choose_model variable is then set to "no" in order to exit the loop.
        if choice == "1":
            model_info.append(2700)
            model_info.append("Mustang")
            choose_model = "no"
        
        elif choice == "2":
            model_info.append(50000)
            model_info.append("Chevrolet") 
            choose_model = "no"
        
        elif choice == "3":
            model_info.append(200000)
            model_info.append("Ferrari") 
            choose_model = "no"
        
        elif choice == "4":
            model_info.append(300000)
            model_info.append("McLaren")
            choose_model = "no"

        # If the user does not select a valid option then they are shown this error message and taken to the start of the loop.
        else:
            print("\nYou have not selected valid option. Please try again")
    
    # This return statement will return the list containing the price and the name of the chosen model.
    return model_info

def carColour():
    # The colour_info list will store the users choice.
    # The colour_price variable is used to keep track of the price.
    # The choose_colour string is used for the while loop below.
    colour_info = []
    colour_price = 0
    choose_colour = "yes"

    # This loop ensures that the user will be repeatedly asked to select an option until they select a valid option.
    while choose_colour == "yes":

        choice = input((
        '''\nPlease select a car model: 
        1. Red - £500
        2. Blue - £500
        3. Green - £500
        4. Yellow - £500
        5. White - £500
        6. Black - £500
        7. Silver - £500
        :'''))

        # If the user selects one of the options from the list above, then the price variable is update.
        if choice == "1":
            colour_price = 500

            # Once the user selects a colour then they are prompted to select the type of paint from the list.
            colour_type = (input(
            '''\nWould you like the colour as: 
            1. Regular - £50
            2. Matte - £100
            3. Chrome - £150
            :'''))

            # Once the user selects one fo the type of paint they want, then the price is updated and appended to the list
            # along with the name of the colour and the type of paint.
            # The choose_colour variable is also set to "no" to ensure that program exists the loop
            if colour_type == "1":
                colour_price += 50
                colour_info.append(colour_price)
                colour_info.append("Red")
                colour_info.append("Regular")
                choose_colour = "no"
            
            elif colour_type == "2":
                colour_price += 100
                colour_info.append(colour_price)
                colour_info.append("Red")
                colour_info.append("Matte")
                choose_colour = "no"
            
            elif colour_type == "3":
                colour_price += 150
                colour_info.append(colour_price)
                colour_info.append("Red")
                colour_info.append("Chrome")
                choose_colour = "no"
            
            else:
                print("\nYou have selected an invalid option")
        
        elif choice == "2":
            colour_price = 500

            colour_type = (input(
            '''\nWould you like the colour as: 
            1. Regular - £50
            2. Matte - £100
            3. Chrome - £150
            :'''))

            if colour_type == "1":
                colour_price += 50
                colour_info.append(colour_price)
                colour_info.append("Blue")
                colour_info.append("Regular")
                choose_colour = "no"
            
            elif colour_type == "2":
                colour_price += 100
                colour_info.append(colour_price)
                colour_info.append("Blue")
                colour_info.append("Matte")
                choose_colour = "no"
            
            elif colour_type == "3":
                colour_price += 150
                colour_info.append(colour_price)
                colour_info.append("Blue")
                colour_info.append("Chrome")
                choose_colour = "no"
            
            else:
                print("\nYou have selected an invalid option")
        
        elif choice == "3":
            colour_price = 500

            colour_type = (input(
            '''\nWould you like the colour as: 
            1. Regular - £50
            2. Matte - £100
            3. Chrome - £150
            :'''))

            if colour_type == "1":
                colour_price += 50
                colour_info.append(colour_price)
                colour_info.append("Green")
                colour_info.append("Regular")
                choose_colour = "no"
            
            elif colour_type == "2":
                colour_price += 100
                colour_info.append(colour_price)
                colour_info.append("Green")
                colour_info.append("Matte")
                choose_colour = "no"
            
            elif colour_type == "3":
                colour_price += 150
                colour_info.append(colour_price)
                colour_info.append("Green")
                colour_info.append("Chrome")
                choose_colour = "no"
            
            else:
                print("\nYou have selected an invalid option")
        
        elif choice == "4":
            colour_price = 500

            colour_type = (input(
            '''\nWould you like the colour as: 
            1. Regular - £50
            2. Matte - £100
            3. Chrome - £150
            :'''))

            if colour_type == "1":
                colour_price += 50
                colour_info.append(colour_price)
                colour_info.append("Yellow")
                colour_info.append("Regular")
                choose_colour = "no"
            
            elif colour_type == "2":
                colour_price += 100
                colour_info.append(colour_price)
                colour_info.append("Yellow")
                colour_info.append("Matte")
                choose_colour = "no"
            
            elif colour_type == "3":
                colour_price += 150
                colour_info.append(colour_price)
                colour_info.append("Yellow")
                colour_info.append("Chrome")
                choose_colour = "no"
            
            else:
                print("\nYou have selected an invalid option")

        elif choice == "5":
            colour_price = 500

            colour_type = (input(
            '''\nWould you like the colour as: 
            1. Regular - £50
            2. Matte - £100
            3. Chrome - £150
            :'''))

            if colour_type == "1":
                colour_price += 50
                colour_info.append(colour_price)
                colour_info.append("White")
                colour_info.append("Regular")
                choose_colour = "no"
            
            elif colour_type == "2":
                colour_price += 100
                colour_info.append(colour_price)
                colour_info.append("White")
                colour_info.append("Matte")
                choose_colour = "no"
            
            elif colour_type == "3":
                colour_price += 150
                colour_info.append(colour_price)
                colour_info.append("White")
                colour_info.append("Chrome")
                choose_colour = "no"
            
            else:
                print("\nYou have selected an invalid option")
        
        elif choice == "6":
            colour_price = 500

            colour_type = (input(
            '''\nWould you like the colour as: 
            1. Regular - £50
            2. Matte - £100
            3. Chrome - £150
            :'''))

            if colour_type == "1":
                colour_price += 50
                colour_info.append(colour_price)
                colour_info.append("Black")
                colour_info.append("Regular")
                choose_colour = "no"
            
            elif colour_type == "2":
                colour_price += 100
                colour_info.append(colour_price)
                colour_info.append("Black")
                colour_info.append("Matte")
                choose_colour = "no"
            
            elif colour_type == "3":
                colour_price += 150
                colour_info.append(colour_price)
                colour_info.append("Black")
                colour_info.append("Chrome")
                choose_colour = "no"
            
            else:
                print("\nYou have selected an invalid option")

        elif choice == "7":
            colour_price = 500

            colour_type = (input(
            '''\nWould you like the colour as: 
            1. Regular - £50
            2. Matte - £100
            3. Chrome - £150
            :'''))

            if colour_type == "1":
                colour_price += 50
                colour_info.append(colour_price)
                colour_info.append("Silver")
                colour_info.append("Regular")
                choose_colour = "no"
            
            elif colour_type == "2":
                colour_price += 100
                colour_info.append(colour_price)
                colour_info.append("Silver")
                colour_info.append("Matte")
                choose_colour = "no"
            
            elif colour_type == "3":
                colour_price += 150
                colour_info.append(colour_price)
                colour_info.append("Silver")
                colour_info.append("Chrome")
                choose_colour = "no"
            
            else:
                print("\nYou have selected an invalid option")

        # If the user does not select a valid option they are shown this error message and the loop restarts.
        else:
            print("\nYou have not selected valid option. Please try again")
    
    # This return statement will return the list containing the price, the chosen colour and the type of paint.
    return colour_info

# This function allows the user to select which accessory they would like to add to their car.
def carAccessories():

    # The accessory_info list will store the users choice and price.
    # The choose_accessory string is used for the while loop below.
    accessory_info = []
    choose_accessory = "yes"

    # This loop ensures that the user will be repeatedly asked to select an option until they select a valid option.
    while choose_accessory == "yes":

        choice = input(('''\nPlease select an accessory: 
        1. Tinted Windows - £75
        2. Custom Rims - £125
        3. Heated Seats - £200
        4. Enhanced Infotainment System - £500
        
        '''))

        # If the user selects one of the options from the list above, then the corresponding price and accessory name will be 
        # added to the list.
        # The choose_accessory variable is then set to "no" in order to exit the loop.
        if choice == "1":
            accessory_info.append(75)
            accessory_info.append("Tinted Windows")
            choose_accessory = "no"
        
        elif choice == "2":
            accessory_info.append(125)
            accessory_info.append("Custom Rims")
            choose_accessory = "no"
        
        elif choice == "3":
            accessory_info.append(200)
            accessory_info.append("Heated Seats")
            choose_accessory = "no"
        
        elif choice == "4":
            accessory_info.append(500)
            accessory_info.append("Enhanced Infotainment System")
            choose_accessory = "no"

        else:
            print("\nYou have not selected valid option. Please try again")
    
    # This return statement will return the list containing the price and the name of the accessory.
    return accessory_info

# This loop ensures that the user will be repeatedly asked to select an option until they select a valid option.
while option != "5":

    print("\nWelcome to the car configurator! Let's get started")
    option = input('''What would you like to choose first?: 
        1. Select Car Model
        2. Select Car Colour
        3. Add Accessories
        4. See current selection and total
        5. Quit
        : ''')
    
    # Depending on the option selected by the user, the corresponding function is called and the total price is updated 
    # and the relevant info is assigned into variables that can be used later to print to the user.
    if option == "1":
        model_cost = carModel()
        total = model_cost[0]
        model = model_cost[1]

    elif option == "2":
        colour_cost = carColour()
        total += colour_cost[0]
        colour = colour_cost[1]
        colour_type = colour_cost[2]
    
    elif option == "3":
        accessories_cost = carAccessories()
        total += accessories_cost[0]
        accessory = accessories_cost[1]

    # When the user selects to display the total cost and their selections, they are displayed to the user before the main menu
    # is displayed again where the user can make changes to the selections.
    elif option == "4":
        print(f"\nYou have selected: ")
        print(f"\nModel: {model}")
        print(f"Colour: {colour}")
        print(f"Paint Type: {colour_type}")
        print(f"Accessory: {accessory}")
        print(f"\nYour current total is: £{total}")

    # If the user selects option five they can then exit the program.
    elif option == "5":
        quit
    
    # If the user select an invalid option then they are shown a message and the main menu loop returns to the beginning.
    else:
        print("\nYou have selected an invalid option")

