class Plate:

    def __init__(self, plate_name):
        self.plate_name = plate_name
        self.dessert = None
        self.vegetables = []
        self.protein = None
        self.spicy = []

    def get_plate_name(self):
        return self.plate_name

    def add_dessert(self, dessert):
        if self.dessert is None:
            self.dessert = dessert
        else:
            print("You already have a dessert")

    def add_protein(self, protein):
        if self.protein is None:
            self.protein = protein
        else:
            print("You already have a protein")

    def add_vegetable(self, vegetable):
        if len(self.vegetables) < 2:
            self.vegetables.append(vegetable)
        else:
            print("You already have two vegetables")

    def add_spice(self, spice):
        if len(self.spicy) < 2:
            self.spicy.append(spice)
        else:
            print("You already have two spices")

    def add_ingredient(self, stock, ingredient_type, ingredient):
        if stock.is_in_this_stock(ingredient):
            if stock.take_from_stock(ingredient):
                if ingredient_type == "proteins":
                    self.add_protein(ingredient)
                if ingredient_type == "vegetables":
                    self.add_vegetable(ingredient)
                if ingredient_type == "spices":
                    self.add_spice(ingredient)
                if ingredient_type == "dessert":
                    self.add_dessert(ingredient)
            else:
                print("Choose another, there is not enough " +
                      ingredient + " on stock")
        else:
            print("Sorry, " + ingredient + " is not on stock")
            return -1

    def full_plate(self):
        has_dessert = self.dessert is not None
        has_protein = self.protein is not None
        has_two_veg = len(self.vegetables) == 2
        has_two_spices = len(self.spicy) == 2
        return has_protein and has_dessert and has_two_veg and has_two_spices

    def __str__(self):
        return self.plate_name + "|" + str(self.protein) + "|" + str(self.vegetables) + "|" + str(self.spicy) + "|" + str(self.dessert)+"\n"
