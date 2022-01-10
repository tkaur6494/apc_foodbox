from Week import Week


class Person:  # the Person object is the customer where the orders will be stored under his name

    def __init__(self, name):
        self.name = name
        # weeks will be a list (w1, w2, ..)  which will be populated with plates (p1, p2..) and ingredients (1 protein, 2 veggies, 2 spices, 1 dessert)
        self.weeks = []
        self.response = []  # response of feedback stored from users

    # used later on to support "in' argument to check if customer already exists
    def __contains__(self, substring):
        if substring in self.name:
            return True
        else:
            return False

    def __str__(self):  # function for printing the order (week, plate and content) when customer ends the program: print (person) (combine the String Week and Plate)
        #personal_plan = str(self.name) + '\n'
        personal_plan = ''
        for week in self.weeks:
            personal_plan += str(week) + '\n'
        return personal_plan

    def add_week(self, week):  # function to append weeks to this person
        self.weeks.append(week)

    # function to check if ALL weeks order have been completed(that is used when a week is fully completed, otherwise week_complete is used)
    def all_weeks_complete(self):
        for w in self.weeks:
            if not w.week_complete():
                return False
        return True

    # function to customer add new week and check if this week already exists or not
    def week_order(self, stock):
        print("\n Do you want to place an order for a week? (yes / no) \n")
        decision_about_week = input()
        while decision_about_week != "yes":  # input check for correct syntax "yes or no"
            if decision_about_week == "no":
                print("\nHave a nice day ")
                return
            print("Error! use correct syntax (yes or no)")
            print("\n Do you want to place an order for a week? (yes / no) \n")
            decision_about_week = input()
        while decision_about_week == "yes":
            # input check for correct syntax "w1.."
            print("\n For which week do you want to order? (w1, w2, w3,..w52) \n")
            week_name = input()
            if week_name[0].lower() != 'w':
                print(
                    "Error! Use correct syntax  (lower case & number: w1, w2,...w52)\n")
                continue
            if len(week_name) > 3 or len(week_name) < 2:
                print(
                    "Error! Use correct syntax  (lower case & number: w1, w2,...w52)\n")
                continue
            if not week_name[1:].isnumeric():
                print("Error! Use correct syntax  (lower case & number: w1, w2,...w52)")
                continue
            # input check for max number of weeks (52)
            week_number = int(week_name[1:])
            if week_number not in range(1, 53):
                print("Error! Use max 52 weeks \n")
                continue

            week_exists = False
            for w in self.weeks:  # check if the week already exists
                if w.get_week_name() == week_name:
                    print("The week " + week_name +
                          " already exists for this person.")
                    week_exists = True
                    print("\n Would you like to complete this week ?\n")
                    decision_about_week = input()

                    # input check for correct syntax "yes" or "no"
                    while decision_about_week != "yes" and decision_about_week != "no":
                        print("Error! use correct syntax (yes or no)")
                        print("\n Would you like to complete this week ?\n")
                        decision_about_week = input()

                    if decision_about_week == "no":
                        break
                    if decision_about_week == "yes":  # if week already exist and customer wants to complete it calls the function to complete the plates of that week
                        self.complete_week(stock, w)
            if week_exists:
                continue

            week = Week(week_name)
            self.add_week(week)
            return week

    def week_complete(self):  # function to check if the week the person wants to complete, exists (used when a week is created but not all plates or ingredients have been ordered)
        while True:
            print("\n Which week do you want to complete? (w1, w2, w3,..w52) \n")
            week_name = input()
            if week_name[0].lower() != 'w':
                print(
                    "Error! Use correct syntax  (lower case & number: w1, w2,...w52)\n")
                continue
            if len(week_name) > 3 or len(week_name) < 2:
                print(
                    "Error! Use correct syntax  (lower case & number: w1, w2,...w52)\n")
                continue
            if not week_name[1:].isnumeric():
                print("Error! Use correct syntax  (lower case & number: w1, w2,...w52)")
                continue
            week_number = int(week_name[1:])
            if week_number not in range(1, 53):
                print("Error! Use max 52 weeks \n")
                continue
            for w in self.weeks:
                if w.get_week_name() == week_name:
                    return w

    # function to check if the week has all the 3 plates ordered (completed) and if not to append it
    def complete_week(self, list_of_stock, week=None):

        if week is None:
            week = self.week_complete()

        if week is None:  # call the function week_complete to check if the week already has 3 plates or not
            return

        if week.get_number_of_plates() == 3:  # check number of plates in the object
            print("Error! That week already has 3 plates")
            return

        week.add_plates([proteins_stock, vegetables_stock,
                         spices_stock, dessert_stock])

    # get the value of the week
    def get_week(self, week):
        for i in self.weeks:
            if(i.get_week_name() == week):
                return i
        return -1

    # get the name of the person
    def get_name(self):
        return self.name

    # set the response submitted by the user
    def set_response(self, response):
        self.response = response
        print(self.response)
