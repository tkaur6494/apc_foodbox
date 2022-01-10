# to have the functionalities properly tested we need to have an external database, which save in a local file using pickles libary to write and read (due to the structure of the objects {person, with weeks, plates, ingredients.} would be very length to implement wihtout pickles)
import pickle
import os.path  # to avoid issues also we used the os.path library to check that the pickles file exists or not

from Stock import Stock
orders_summary = {}
feedback_complete = {}

# variable created just in case we need to change the file and avoid typos
FOOD_BOX_FILE = "food_box_orders.p"
PROTEINS_STOCK_FILE = "food_box_proteins_stock.p"
VEGETABLES_STOCK_FILE = "food_box_vegetables_stock.p"
SPICES_STOCK_FILE = "food_box_spices_stock.p"
DESSERT_STOCK_FILE = "food_box_dessert_stock.p"
FEEDBACK_USER_FILE = "food_box_feedback_list.p"


# since we do not have a database this list will store the orders for admin functionalities test
orders_summary = {}

# separate files for orders, proteins, vegetables, spices, deserts and feedback

if os.path.isfile(FOOD_BOX_FILE):
    orders_summary = pickle.load(open(FOOD_BOX_FILE, "rb"))

if os.path.isfile(PROTEINS_STOCK_FILE):
    proteins_stock = pickle.load(open(PROTEINS_STOCK_FILE, "rb"))


if os.path.isfile(VEGETABLES_STOCK_FILE):
    vegetables_stock = pickle.load(open(VEGETABLES_STOCK_FILE, "rb"))

if os.path.isfile(SPICES_STOCK_FILE):
    spices_stock = pickle.load(open(SPICES_STOCK_FILE, "rb"))

if os.path.isfile(DESSERT_STOCK_FILE):
    dessert_stock = pickle.load(open(DESSERT_STOCK_FILE, "rb"))

if os.path.isfile(FEEDBACK_USER_FILE):
    feedback_complete = pickle.load(open(FEEDBACK_USER_FILE, "rb"))
