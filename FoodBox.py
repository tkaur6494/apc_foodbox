# FOOD BOX

# Variable names
# name = user name
# name_dictionary = the dictionary of the users names and related ordering
# week = list of weeks
# plate = list of plates


# ORDERING PROCESS

# What can be done for ordering
# New users start order from w1
# Existing users will continue order for the week after its last ordered week
# User can order up to 3 plates per week
# Each plat contain 1 protein, 2 veggies, 2 spices, 1 dessert
# System in will form what is available in stock
# If order does not match what is in stock a info to order what is in stock will be displayed


# Login process (sinple login wihtout passowrd, system will check if name exist or not)

from orders_summary import *
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from Person import Person
from Week import Week
from Plate import Plate
from Stock import Stock
from UserView import UserView
from ViewOrder import ViewOrder
from FeedbackView import FeedbackView
from ViewStock import ViewStock
from ViewAdminFeedback import ViewAdminFeedback


class FoodBox:
    def __init__(self):
        self.root = Tk()
        self.root.title("Food Box")
        self.frame_login = None
        self.notebook_view = ttk.Notebook(self.root)
        self.person = None
        self.loginView()
        self.root.mainloop()

    def loginView(self):
        self.frame_login = LabelFrame(self.root, pady=80)                   
        self.frame_login.pack(side=RIGHT, fill=Y)
        label_username = Label(
            self.frame_login, text="Username", padx=10, font=("Helvetica", 10, "bold"))
        entry_username = Entry(
            self.frame_login, width=35, relief=SUNKEN, bd=2)
        button_login = Button(
            self.frame_login, text="Login", command=lambda: self.getUserName(entry_username.get()))
        label_username.grid(row=0, column=0, sticky=W)
        entry_username.grid(row=1, column=0, padx=10, pady=5)
        button_login.grid(row=2, column=0)

    def getUserName(self, person_name):
        self.frame_login.destroy()
        person_name = person_name
        if person_name in orders_summary:           #checking if the person already exists
            print("\nWelcome Back")
            self.person = orders_summary[person_name]
        else:
            self.person = Person(person_name)       #if not create a new object
        # the view order view will also be same but different parameters
        frame_view_order = LabelFrame(self.root, pady=5)

        if(person_name != 'admin'):                  #checking if the logged in person is the admin or not
            self.userView()
            orderView = ViewOrder(frame_view_order, self.person)
        else:
            orderView = ViewOrder(frame_view_order, None, 'admin')
            frame_feedback_complete = LabelFrame(self.root, pady=5)
            feedbackCompleteView = ViewAdminFeedback(frame_feedback_complete)
            self.notebook_view.add(
                frame_feedback_complete, text="View feedbacks")

        self.commonView()                            #common view method for handling the same views - view order and stock
        self.notebook_view.bind(
            '<<NotebookTabChanged>>', lambda event: orderView.updateText() if event.widget.tab('current')['text'].lower() == "view orders" else (stockView.updateText() if event.widget.tab('current')['text'].lower() == "view stock" else None))
        self.notebook_view.add(frame_view_order, text="View orders")
        self.notebook_view.pack()

    # adding user view and feedback view
    def userView(self):
        frame_user_view = LabelFrame(self.root, pady=5)
        userView = UserView(frame_user_view, self.person)
        self.notebook_view.add(frame_user_view, text="New order")
        frame_feedback_user_view = LabelFrame(self.root, pady=5)
        feedbackView = FeedbackView(frame_feedback_user_view, self.person)
        self.notebook_view.add(
            frame_feedback_user_view, text="Give Feedback")

    # the stock view will be visible to both user and admin

    def commonView(self):

        frame_stock_view = LabelFrame(self.root, pady=5)
        stockView = ViewStock(
            frame_stock_view, [proteins_stock, vegetables_stock, spices_stock, dessert_stock], self.person)
        self.notebook_view.add(
            frame_stock_view, text="View Current Stock")


fb = FoodBox()
