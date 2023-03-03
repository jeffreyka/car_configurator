model_cost = 0
total = 0
option = "0"

def carModel():
    base_price = 0
    choose_model = "yes"

    while choose_model == "yes":

        choice = input(('''Please select a car model: 
        1. Mustang - £27,000
        2. Chevrolet - £50,000
        3. Ferrari - £200,000
        4. McLaren - £300,000
        
        '''))

        if choice == "1":
            base_price = 27000
            choose_model = "no"
        
        elif choice == "2":
            base_price = 50000
            choose_model = "no"
        
        elif choice == "3":
            base_price = 200000
            choose_model = "no"
        
        elif choice == "4":
            base_price = 300000
            choose_model = "no"

        else:
            print("You have not selected valid option. Please try again")
    
    return base_price

def carColour():
    colour_price = 0
    choose_colour = "yes"

    while choose_colour == "yes":

        choice = input((
        '''Please select a car model: 
        1. Red - £500
        2. Blue - £500
        2. Green - £500
        3. Yellow - £500
        4. White - £500
        5. Black - £500
        6. Silver - £500
        :'''))

        if choice == "1":
            colour_price = 500

            colour_type = (input(
            '''Would you like the colour as: 
            1. Regular - £50
            2. Matte - £100
            3. Chrome - £150
            :'''))

            if colour_type == "1":
                colour_price += 50
                choose_colour = "no"
            
            elif colour_type == "2":
                colour_price += 100
                choose_colour = "no"
            
            elif colour_type == "3":
                colour_price += 150
                choose_colour = "no"
            
            else:
                print("You have selected an invalid option")
        
        elif choice == "2":
            colour_price = 500

            colour_type = (input(
            '''Would you like the colour as: 
            1. Regular - £50
            2. Matte - £100
            3. Chrome - £150
            :'''))

            if colour_type == "1":
                colour_price += 50
                choose_colour = "no"
            
            elif colour_type == "2":
                colour_price += 100
                choose_colour = "no"
            
            elif colour_type == "3":
                colour_price += 150
                choose_colour = "no"
            
            else:
                print("You have selected an invalid option")
        
        elif choice == "3":
            colour_price = 500

            colour_type = (input(
            '''Would you like the colour as: 
            1. Regular - £50
            2. Matte - £100
            3. Chrome - £150
            :'''))

            if colour_type == "1":
                colour_price += 50
                choose_colour = "no"
            
            elif colour_type == "2":
                colour_price += 100
                choose_colour = "no"
            
            elif colour_type == "3":
                colour_price += 150
                choose_colour = "no"
            
            else:
                print("You have selected an invalid option")
        
        elif choice == "4":
            colour_price = 500

            colour_type = (input(
            '''Would you like the colour as: 
            1. Regular - £50
            2. Matte - £100
            3. Chrome - £150
            :'''))

            if colour_type == "1":
                colour_price += 50
                choose_colour = "no"
            
            elif colour_type == "2":
                colour_price += 100
                choose_colour = "no"
            
            elif colour_type == "3":
                colour_price += 150
                choose_colour = "no"
            
            else:
                print("You have selected an invalid option")

        elif choice == "5":
            colour_price = 500

            colour_type = (input(
            '''Would you like the colour as: 
            1. Regular - £50
            2. Matte - £100
            3. Chrome - £150
            :'''))

            if colour_type == "1":
                colour_price += 50
                choose_colour = "no"
            
            elif colour_type == "2":
                colour_price += 100
                choose_colour = "no"
            
            elif colour_type == "3":
                colour_price += 150
                choose_colour = "no"
            
            else:
                print("You have selected an invalid option")
        
        elif choice == "6":
            colour_price = 500

            colour_type = (input(
            '''Would you like the colour as: 
            1. Regular - £50
            2. Matte - £100
            3. Chrome - £150
            :'''))

            if colour_type == "1":
                colour_price += 50
                choose_colour = "no"
            
            elif colour_type == "2":
                colour_price += 100
                choose_colour = "no"
            
            elif colour_type == "3":
                colour_price += 150
                choose_colour = "no"
            
            else:
                print("You have selected an invalid option")

        else:
            print("You have not selected valid option. Please try again")
    
    return colour_price

def carAccessories():
    pass

while option != "5":

    print("Welcome to the car configurator! Let's get started")
    option = input('''What would you like to choose first?: 
        1. Select Car Model
        2. Select Car Colour
        3. Add Accessories
        4. See current overall cost
        5. Quit
        : ''')
    
    if option == "1":
        model_cost = carModel()
        total += model_cost

    elif option == "2":
        colour_cost = carColour()
        total += colour_cost
    
    elif option == "3":
        accessories_cost = carAccessories()
        total += accessories_cost

    elif option == "4":
        print(f"Your current total is: £{total}")

    elif option == "5":
        quit
    
    else:
        print("You have selected an invalid option")

