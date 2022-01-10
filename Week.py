class Week:

    def __init__(self, name_of_week):
        self.name_of_week = name_of_week
        self.plates = []

    def __str__(self):
        week_plan = ""
        for plate in self.plates:
            week_plan += str(self.name_of_week) + '|' + str(plate)
        return week_plan

    def add_plate(self, plate):
        if len(self.plates) == 3:
            return

        self.plates.append(plate)

    def get_number_of_plates(self):
        return len(self.plates)

    def all_plates_full(self):
        for plate in self.plates:
            if not plate.full_plate():
                return False
        return True

    def week_complete(self):
        if self.get_number_of_plates() == 3 and self.all_plates_full():
            return 0
        elif (self.get_number_of_plates() == 3 and (not self.all_plates_full())):
            return 1
        elif self.get_number_of_plates() < 3:
            return 2

    def get_week_name(self):
        return self.name_of_week

    def add_plates(self, main_stock):

        proteins_stock = main_stock[0]
        vegetables_stock = main_stock[1]
        spices_stock = main_stock[2]
        dessert_stock = main_stock[3]

        for i in range(0, 3):
            plate = self.plate_order(main_stock)
            if plate is None:
                return
            while True:
                print("\nPlate  " + str(plate))
                print(
                    "\n Which ingredient you want to order? (proteins, vegetables, spices, dessert) \n")
                ingredient_type = input()
                if ingredient_type.lower() not in ['proteins', 'vegetables', 'spices', 'dessert']:
                    print(
                        "Not Available! Please use one of those ingredients with the same syntax: \n (proteins, vegetables, spices, dessert)")
                    continue
                stock = None
                if ingredient_type == "proteins":
                    stock = proteins_stock
                if ingredient_type == "vegetables":
                    stock = vegetables_stock
                if ingredient_type == "spices":
                    stock = spices_stock
                if ingredient_type == "dessert":
                    stock = dessert_stock

                print("The Stock:", stock.products)
                print("\n Which " + ingredient_type + " you want to order?")
                ingr = ""
                for ingredient in stock.products:
                    ingr += ingredient + ", "
                ingr = ingr[:-2]
                ingredient_subtype = input()
                plate.add_ingredient(stock, ingredient_type,
                                     ingredient_subtype.title())
                print("\n Do you want to add another ingredient ? (yes / no)")
                decision_about_ingredient = input()

                while decision_about_ingredient != "yes" and decision_about_ingredient != "no":
                    print("Error! use correct syntax (yes or no)")
                    print("\n Do you want to add another ingredient ? (yes / no)")
                    decision_about_ingredient = input()

                if decision_about_ingredient == "no":
                    break

    def complete_plates(self, main_stock, plate=None):
        proteins_stock = main_stock[0]
        vegetables_stock = main_stock[1]
        spices_stock = main_stock[2]
        dessert_stock = main_stock[3]

        if plate is None:
            plate = self.plate_complete()

        if plate is None:
            return

        if plate.full_plate():
            print("Error! The plate is already full.")
            return
        while True:
            print("\nPlate " + str(plate))
            print(
                "\n Which ingredient you want to add? (proteins, vegetables, spices, dessert) \n")
            ingredient_type = input()
            if ingredient_type.lower() not in ['proteins', 'vegetables', 'spices', 'dessert']:
                print("Not Available! Please use one of those ingredients with the same syntax: \n (proteins, vegetables, spices, dessert)")
                continue
            stock = None
            if ingredient_type == "proteins":
                stock = proteins_stock
            if ingredient_type == "vegetables":
                stock = vegetables_stock
            if ingredient_type == "spices":
                stock = spices_stock
            if ingredient_type == "dessert":
                stock = dessert_stock

            print("The Stock:", stock.products)
            print("\n Which " + ingredient_type + " you want to add?")
            ingr = ""
            for ingredient in stock.products:
                ingr += ingredient + ", "
            ingr = ingr[:-2]
            ingredient_subtype = input()
            plate.add_ingredient(stock, ingredient_type,
                                 ingredient_subtype.title())
            print("\n Do you want to add another ingredient ? (yes / no)")
            decision_about_ingredient = input()

            while decision_about_ingredient != "yes" and decision_about_ingredient != "no":
                print("Error! use correct syntax (yes or no)")
                print("\n Do you want to add another ingredient ? (yes / no)")
                decision_about_ingredient = input()

            if decision_about_ingredient == "no":
                break

    def plate_order(self, stock):
        print("\n Do you want to add a plate ? (yes / no) \n")
        decision_about_plate = input()
        while decision_about_plate != "yes" and decision_about_plate != "no":
            print("Error! use correct syntax (yes or no)")
            print("\n Do you want to add a plate ? (yes / no) \n")
            decision_about_plate = input()
        if decision_about_plate == "no":
            return
        while True:
            print("\n Which plate you want to order ? (p1, p2 or p3) \n")
            plate_name = input()
            if plate_name[0].lower() != 'p':
                print("Error! Use correct syntax  (lower case & number: p1, p2 or p3)\n")
                continue
            if len(plate_name) > 2:
                print("Error! Use correct syntax  (lower case & number: p1, p2 or p3)\n")
                continue
            if not plate_name[1:].isnumeric():
                print("Error! Use correct syntax  (lower case & number: p1, p2 or p3)")
                continue
            plate_number = int(plate_name[1:])
            if plate_number not in range(1, 4):
                print("Error! Max 3 plates \n")
                break
            plate_exists = False
            for p in self.plates:
                if p.get_plate_name() == plate_name:
                    print("The plate " + plate_name +
                          " already exists for this week.")
                    plate_exists = True
                    print("\n Would you like to complete this plate ? (yes / no) \n")
                    decision_about_plate = input()

                    while decision_about_plate != "yes" and decision_about_plate != "no":
                        print("Error! use correct syntax (yes or no)")
                        print(
                            "\n Would you like to complete this plate ? (yes / no) \n")
                        decision_about_plate = input()

                    if decision_about_plate == "no":
                        break
                    if decision_about_plate == "yes":
                        self.complete_plates(stock, p)

            if plate_exists:
                continue
            plate = Plate(plate_name)
            self.add_plate(plate)
            return plate

    def plate_complete(self):
        print("\n Do you want to complete a plate ? (yes / no) \n")
        decision_about_plate = input()

        while decision_about_plate != "yes" and decision_about_plate != "no":
            print("Error! use correct syntax (yes or no)")
            print("\n Do you want to complete a plate ? (yes / no) \n")
            decision_about_plate = input()

        if decision_about_plate == "no":
            return
        while True:
            print("\n Which plate you want to complete ? (p1, p2 or p3) \n")
            plate_name = input()
            if plate_name[0].lower() != 'p':
                print("Error! Use correct syntax  (lower case & number: p1, p2 or p3)\n")
                continue
            if len(plate_name) > 2:
                print("Error! Use correct syntax  (lower case & number: p1, p2 or p3)\n")
                continue
            if not plate_name[1:].isnumeric():
                print("Error! Use correct syntax  (lower case & number: p1, p2 or p3)")
                continue
            plate_number = int(plate_name[1:])
            if plate_number not in range(1, 4):
                print("Error! Max 3 plates \n")
                break
            for p in self.plates:
                if p.get_plate_name() == plate_name:
                    return p

    def plate_exists(self, plate_name):
        if(not any(dict.get_plate_name() == plate_name for dict in self.plates)):
            return False
        else:
            return True
