from Stock import Stock

proteins_stock = Stock(
    "proteins", {"chicken": 0, "beef": 10, "Lamb": 10, "Fish": 10})

vegetables_stock = Stock(
    "vegetables",
    {"Salad": 10, "Carot": 0, "Onion": 10, "Corn": 10, "Celery": 10, "Potato": 10},
)

spices_stock = Stock(
    "spices",
    {"Salt": 10, "Peper": 10, "Curry": 10, "Basil": 10, "Cumin": 10, "Paprika": 10},
)

dessert_stock = Stock(
    "desert", {"Ice Cream": 10, "Chocolate": 10, "Cake": 10, "Fruit": 10}
)
