import time


def survey():
    question_index = 0
    input = str(input("What is your name? "))
    response = []

    def question_one():
        global question_index
        print("What do you love the most about our food? ")
        print("A. protein  B.Vegetable  C.Dessert  D.Spice")
        ans = str(input())
        response.append(ans)
        question_index += 1

    def question_two():
        global question_index
        print("How do you rate our quality? ")
        print("A.*   B. **  C.***  D.****")
        ans = str(input())
        response.append(ans)
        question_index += 1

    def question_three():
        global question_index
        print("Which segment do you consider worth improving for our service? ")
        print("A. protein  B. vegetable  C.dessert  D.spice")
        ans = str(input())
        response.append(ans)
        question_index += 1

    def question_four():
        global question_index
        print("Was the packaging intact when you did the takeout from the restaurant? ")
        print("A. Yes  B.No")
        ans = str(input())
        response.append(ans)
        question_index += 1

    def question_five():
        global question_index
        print("How likely will you recommend the restaurant to your friends or families? ")
        print("A. Very likely   B. A little likely     C.Unlikely")
        ans = str(input())
        response.append(ans)
        question_index += 1

    def question_six():
        global question_index
        print("What do you like to see on our menu? ")
        print("Please select the segment")
        print("A. Protein  B.Vegetable  C.Dessert   D.Spice")
        answer = str(input())
        print("Please write down the items you would like to have.")
        res = str(input())
        tus = (answer, res)
        response.append(tus)
        question_index += 1

    def question_seven():
        global question_index
        print("Please write down any feedback you may for our food service")
        ans = str(input())
        response.append(ans)
        question_index += 1

    question_one()
    question_two()
    question_three()
    question_four()
    question_five()
    question_six()
    question_seven()
