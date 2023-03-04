model_cost = []
colour_cost = []
accessory_cost = []
model = ""
colour = ""
colour_type = ""
accessory = ""
total = 0
option = "0"

def carModel():
    model_info = []
    choose_model = "yes"

    while choose_model == "yes":

        choice = input(('''\nPlease select a car model: 
        1. Mustang - £27,000
        2. Chevrolet - £50,000
        3. Ferrari - £200,000
        4. McLaren - £300,000
        
        '''))

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

        else:
            print("\nYou have not selected valid option. Please try again")
    
    return model_info

def carColour():
    colour_info = []
    colour_price = 0
    choose_colour = "yes"

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

        if choice == "1":
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

        else:
            print("\nYou have not selected valid option. Please try again")
    
    return colour_info

def carAccessories():
    accessory_info = []
    choose_accessory = "yes"

    while choose_accessory == "yes":

        choice = input(('''\nPlease select an accessory: 
        1. Tinted Windows - £75
        2. Custom Rims - £125
        3. Heated Seats - £200
        4. Enhanced Infotainment System - £500
        
        '''))

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
    
    return accessory_info

while option != "5":

    print("\nWelcome to the car configurator! Let's get started")
    option = input('''What would you like to choose first?: 
        1. Select Car Model
        2. Select Car Colour
        3. Add Accessories
        4. See current selection and total
        5. Quit
        : ''')
    
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

    elif option == "4":
        print(f"\nYou have selected: ")
        print(f"\nModel: {model}")
        print(f"Colour: {colour}")
        print(f"Paint Type: {colour_type}")
        print(f"Accessory: {accessory}")
        print(f"\nYour current total is: £{total}")

    elif option == "5":
        quit
    
    else:
        print("\nYou have selected an invalid option")

