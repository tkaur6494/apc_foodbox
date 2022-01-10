from tkinter import *
from tkinter import ttk
from orders_summary import *


class ViewOrder:
    # generating a table view for viewing orders
    def __init__(self, frame_view_order, person=None, admin=None):
        self.frame_view_order = frame_view_order
        if(person != 'None'):
            self.person = person
        self.treeView = ttk.Treeview(self.frame_view_order)
        style = ttk.Style()
        style.theme_use("clam")
        self.treeView["columns"] = ["Name", "Week", "Plate",
                                    "Protein", "Vegetables", "Spices", "Dessert"]
        self.treeView.column("#0", width=0, stretch=NO)
        if(admin == None):
            self.treeView.column("Name", minwidth=0, width=0,
                                 stretch=NO, anchor=CENTER)  # hiding name column if user has logged in
        else:
            self.treeView.column("Name", minwidth=0, width=80,
                                 stretch=NO, anchor=CENTER)
        self.treeView.column("Week", minwidth=0, width=80,
                             stretch=NO, anchor=CENTER)
        self.treeView.column("Plate", minwidth=0, width=80,
                             stretch=NO, anchor=CENTER)
        self.treeView.column("Protein", minwidth=0,
                             width=80, stretch=NO, anchor=CENTER)
        self.treeView.column("Vegetables", minwidth=0,
                             width=120, stretch=NO, anchor=CENTER)
        self.treeView.column("Spices", minwidth=0,
                             width=120, stretch=NO, anchor=CENTER)
        self.treeView.column("Dessert", minwidth=0,
                             width=120, stretch=NO, anchor=CENTER)
        self.treeView.heading("Name", text="Name")
        self.treeView.heading("Week", text="Week")
        self.treeView.heading("Plate", text="Plate")
        self.treeView.heading("Protein", text="Protein")
        self.treeView.heading("Vegetables", text="Vegetables")
        self.treeView.heading("Spices", text="Spices")
        self.treeView.heading("Dessert", text="Dessert")
        self.treeView.grid(row=0, column=0, sticky="we")

    def updateText(self):
        for i in self.treeView.get_children():
            self.treeView.delete(i)
        if(self.person != None):
            _personOrders = str(
                orders_summary[self.person.get_name()]).split("\n")
            for i in _personOrders:
                final_str = self.person.get_name()+"|"+i
                self.treeView.insert(
                    '', 'end', values=tuple(final_str.split("|")))
        else:
            for i in orders_summary.keys():
                order_list_per_user = str(orders_summary[i]).split("\n")
                filterdList = list(
                    filter(lambda x: x != '', order_list_per_user))  # removing any null orders

                for j in filterdList:
                    final_str = i+"|"+str(j)
                    self.treeView.insert(
                        '', 'end', values=tuple(final_str.split("|")))
