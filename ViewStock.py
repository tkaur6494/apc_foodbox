from tkinter import *
from tkinter import ttk
#from config_stock import *
from orders_summary import *


class ViewStock:
    def __init__(self, frame_stock_view, stock, person):
        self.stock = stock
        self.frame_stock_view = frame_stock_view
        self.labels = []
        self.labelValues = []
        self.person = person
        self.appendLabelText()

    def updateText(self, stock):
        # destroying text after new text has been updated
        for i in self.labelValues:
            i.destroy()
        for i in self.labels:
            i.destroy()
        self.labels.clear()
        self.labelValues.clear()
        self.appendLabelText()

    def appendLabelText(self):
        # adding labels and their corresponding values so multiplied by two
        for i in range(0, len(self.stock)*2, 2):
            stock_item = self.stock[int(i/2)]
            label_category_header = Label(self.frame_stock_view,
                                          text=stock_item.get_stock_name().upper())
            label_category_header.grid(row=i, column=0)
            if(self.person.get_name() == 'admin'):  # if admin has logged in adding refill button
                button_refill = Button(self.frame_stock_view, text="Refill All",
                                       command=lambda stock_item=stock_item: self.updateStock(stock_item))
                button_refill.grid(row=i, column=1)
            products_list = self.stock[int(i/2)].get_products()
            product_list_keys = list(products_list.keys())
            row_value = i+1
            # generating the proper format of the ui using for loop
            for j in range(0, len(product_list_keys)*3, 3):
                label_sub_header = Label(self.frame_stock_view,
                                         text=product_list_keys[int(j/3)])
                label_value = Label(self.frame_stock_view,
                                    text=products_list[product_list_keys[int(j/3)]])
                label_sub_header.grid(row=i+1, column=j)
                label_value.grid(row=i+1, column=j+1)

            self.labels.append(label_category_header)

    def updateStock(self, stock_item):
        # refilling stock by calling method of stock class
        new_list = stock_item.refill_stock()
        for i in self.stock:
            stock_name = i.get_stock_name()
            if(stock_name == stock_item.get_stock_name()):
                i.products = new_list
                if(stock_name == "proteins"):  # dumping new values in their corresponding files
                    pickle.dump(proteins_stock, open(
                        PROTEINS_STOCK_FILE, "wb"))
                elif(stock_name == "vegetables"):
                    pickle.dump(vegetables_stock, open(
                        VEGETABLES_STOCK_FILE, "wb"))
                elif(stock_name == "spices"):
                    pickle.dump(spices_stock, open(
                        SPICES_STOCK_FILE, "wb"))
                else:
                    pickle.dump(dessert_stock, open(
                        DESSERT_STOCK_FILE, "wb"))
        self.updateText(self.stock)
