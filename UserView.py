from orders_summary import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from Person import Person
from Week import Week
from Plate import Plate
from Stock import Stock
from functools import reduce


class UserView:
    def __init__(self, frame_user_view, person):
        # GUI for placing the order
        self.person = person
        self.label_heading = Label(frame_user_view, text="Place your order")
        self.label_heading.grid(row=0, column=0, columnspan=6)
        self.label_select_week = Label(
            frame_user_view, text="Select Week", padx=20)
        self.label_select_week.grid(row=1, column=0)
        self.listbox_week = Listbox(frame_user_view, exportselection=False)
        for i in range(0, 52):  # generating 52 weeks w1-w52
            self.listbox_week.insert(i + 1, "w" + str(i + 1))
        self.listbox_week.grid(row=2, column=0)
        self.label_select_plate = Label(
            frame_user_view, text="Select Plate", padx=20)
        self.label_select_plate.grid(row=1, column=1)
        self.listbox_plate = Listbox(frame_user_view, exportselection=False)
        for i in range(0, 3):  # generating 3 plates Plate1-Plate3
            self.listbox_plate.insert(i, "Plate " + str(i + 1))
        self.listbox_plate.grid(row=2, column=1)
        self.label_select_protein = Label(
            frame_user_view, text="Select Protein", padx=20
        )
        self.label_select_protein.grid(row=1, column=2)
        self.listbox_protein = Listbox(frame_user_view, exportselection=False)
        # fetching the proteins from the proteins file
        proteinList = list(proteins_stock.products.keys())
        for i in proteinList:  # adding the proteins' value to the menu
            self.listbox_protein.insert(END, i)
        self.listbox_protein.grid(row=2, column=2)
        self.label_select_vegetable = Label(
            # fetching the vegetables from the vegatbles' stock file
            frame_user_view, text="Select Vegetables", padx=20
        )
        self.label_select_vegetable.grid(row=1, column=3)
        self.listbox_vegetable = Listbox(
            frame_user_view, exportselection=False, selectmode=MULTIPLE
        )
        vegetableList = list(vegetables_stock.products.keys())
        for i in vegetableList:
            self.listbox_vegetable.insert(END, i)
        self.listbox_vegetable.grid(row=2, column=3)
        self.label_select_spice = Label(
            frame_user_view, text="Select Spices", padx=20)
        self.label_select_spice.grid(row=1, column=4)
        self.listbox_spice = Listbox(
            frame_user_view, exportselection=False, selectmode=MULTIPLE
        )
        # fetching the spices from thr spices' stock file
        spiceList = list(spices_stock.products.keys())
        for i in spiceList:
            self.listbox_spice.insert(END, i)
        self.listbox_spice.grid(row=2, column=4)
        self.label_select_dessert = Label(
            frame_user_view, text="Select Dessert", padx=20
        )
        self.label_select_dessert.grid(row=1, column=5)
        # fetching the deserts' from the desert stock file
        self.listbox_dessert = Listbox(frame_user_view, exportselection=False)
        dessertList = list(dessert_stock.products.keys())
        for i in dessertList:
            self.listbox_dessert.insert(END, i)
        self.listbox_dessert.grid(row=2, column=5)
        self.button_submit = Button(  # button for submitting the order
            frame_user_view,
            text="Place Order",
            command=lambda: self.get_order_details(frame_user_view),
        )
        self.button_submit.grid(row=15, column=3, pady=20)
        self.button_clear_selection = Button(  # button for clearing the selection
            frame_user_view,
            text="Clear Selection",
            command=lambda: self.clear_selection(frame_user_view),
        )
        self.button_clear_selection.grid(row=15, column=4, pady=20)

    # getting all the details selected by the user in the listboxes and then validating
    # whether every item is present in the stock
    # even if one item is not available, error message pops up and the existing objects
    # are deleted so that no invalid objects are added

    def get_order_details(self, frame_user_view):
        try:
            week_selected = Week(self.listbox_week.get(  # creating the week object from the value of week selected
                self.listbox_week.curselection()))
            plate_selected = Plate(self.listbox_plate.get(  # creating the plate object from the value of plate selected
                self.listbox_plate.curselection()))
            protein_value = self.convert_index_to_value(  # getting the list of selected value
                self.listbox_protein)
            vegetable_value = self.convert_index_to_value(  # getting the list of selected value
                self.listbox_vegetable)
            dessert_value = self.convert_index_to_value(  # getting the list of selected value
                self.listbox_dessert)
            spice_value = self.convert_index_to_value(  # getting the list of selected value
                self.listbox_spice)
            protein_out_of_stock = self.get_out_of_stock(  # checking if proteins are out of stock or not
                plate_selected, proteins_stock, "proteins", protein_value
            )
            vegetable_out_of_stock = self.get_out_of_stock(  # checking if vegetables are out of stock or not
                plate_selected, vegetables_stock, "vegetables", vegetable_value
            )
            spices_out_of_stock = self.get_out_of_stock(  # checking if spices are out of stock or not
                plate_selected, spices_stock, "spices", spice_value
            )
            dessert_out_of_stock = self.get_out_of_stock(  # checking if desert are out of stock or not
                plate_selected, dessert_stock, "dessert", dessert_value
            )
            if any(  # checking even if one of the things is out of stock
                [  # show error and delete previously created objects
                    protein_out_of_stock,  # as order cannot be successfully added
                    vegetable_out_of_stock,
                    spices_out_of_stock,
                    dessert_out_of_stock,
                ]
            ):
                del week_selected
                del plate_selected
            else:  # if everything is in stock start creating the order
                week_name = week_selected.get_week_name()

                if(self.person.get_week(week_name) == -1):
                    self.person.add_week(week_selected)
                else:
                    week_selected = self.person.get_week(week_name)
                if(week_selected.week_complete() == 0):  # validations added
                    messagebox.showerror(
                        "Error", "You have already added full plates for this week. Please select a different week")
                    return
                elif(week_selected.week_complete() == 1):  # validation for plates added
                    messagebox.showerror(
                        "Error", "You have already added plates for this week. However they are not full.You can add items to your existing plates.")
                    return
                elif(week_selected.plate_exists(plate_selected.get_plate_name()) == True):
                    messagebox.showerror(
                        "Error", "You have already placed an order for this plate for this week. Please select a different plate or go to update plates for changing existing order")
                    return
                elif(len(protein_value) < 1):  # check if one protein has been selected
                    messagebox.showerror(
                        "Error", "Please select a protein for completing your order.")
                    return
                elif(len(vegetable_value) != 2):  # check if two vegetables have been selected
                    messagebox.showerror(
                        "Error", "Please select 2 vegetables for completing your order.")
                    return
                elif(len(spice_value) != 2):  # check if two spices have been selected
                    messagebox.showerror(
                        "Error", "Please select 2 spices for completing your order.")
                    return
                elif(len(dessert_value) < 1):  # check if one desert has been selected
                    messagebox.showerror(
                        "Error", "Please select a desert for completing your order.")
                    return
                week_selected.add_plate(plate_selected)
                orders_summary[self.person.name] = self.person
                pickle.dump(orders_summary, open(FOOD_BOX_FILE, "wb"))
                pickle.dump(proteins_stock, open(  # dumping new values into the files after order has been added
                            PROTEINS_STOCK_FILE, "wb"))
                pickle.dump(vegetables_stock, open(
                            VEGETABLES_STOCK_FILE, "wb"))
                pickle.dump(spices_stock, open(
                            SPICES_STOCK_FILE, "wb"))
                pickle.dump(dessert_stock, open(
                            DESSERT_STOCK_FILE, "wb"))
                print(orders_summary)
                messagebox.showinfo(
                    "Success", "Order Placed successfully")
        except:
            messagebox.showerror(  # error handling if week or plate is not selected
                "Error", "Please select all details before submitting")

    # converting the selected indices from the listbox to a list of actual string values
    def convert_index_to_value(self, obj):
        return [obj.get(idx) for idx in list(obj.curselection())]

    # checking which items are not available in stock and showing error message
    def get_out_of_stock(self, plate, stock, ingredient_type, selected_ingredients):
        ingredients_out_stock = list(
            filter(
                lambda x: plate.add_ingredient(
                    stock, ingredient_type, x) == -1,
                selected_ingredients,
            )
        )
        if len(ingredients_out_stock) >= 1:
            messagebox.showerror(
                "Following items are not in stock ",
                ingredient_type.upper()
                + " , ".join(ingredients_out_stock)
                + " not in stock",
            )
            return TRUE
        return FALSE

    # adding more plates so first checking if any plates have been added
    # then checking if 3 plates have been already added to week or not
    # by default selecting the week which the user had previously selected
    def clear_selection(self, frame_user_view):
        self.listbox_week.select_clear(0, "end")
        self.listbox_plate.selection_clear(0, "end")
        self.listbox_protein.selection_clear(0, "end")
        self.listbox_vegetable.selection_clear(0, "end")
        self.listbox_spice.selection_clear(0, "end")
        self.listbox_dessert.selection_clear(0, "end")
        self.listbox_week.activate(0)
