class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.reviews = {}  # username -> rating

    def get_avg_rating(self):
        if len(self.reviews) == 0:
            return 0.0
        return sum(self.reviews.values()) / len(self.reviews)


class Store:
    def __init__(self):
        self.catalog = {}  # name -> Product

    def add_product(self, name, price, stock):
        self.catalog[name] = Product(name, price, stock)

    def restock(self, name, quantity):
        self.catalog[name].stock += quantity

    def purchase(self, name, quantity):
        if (self.catalog[name].stock < quantity):
            print ('Insufficient stock')
            return()
        else:
            self.catalog[name].stock -= quantity

    def add_review(self, user, name, rating):
        self.catalog[name].reviews[user] = rating

    def display_inventory(self):
        products = list(self.catalog.values())
        
        # simple bubble sort
        for i in range(len(products)):
            for j in range(i+1, len(products)):
                r1 = products[i].get_avg_rating()
                r2 = products[j].get_avg_rating()
                
                if r1 < r2:  # swap if wrong order
                    products[i], products[j] = products[j], products[i]
                elif r1 == r2:  # tie → sort by price ascending
                    if products[i].price > products[j].price:
                        products[i], products[j] = products[j], products[i]
        
        for p in products:
            print(p.name, p.stock, p.get_avg_rating())
            
        # Format: {name} {stock} {avg-rating}


amazon = Store()

n = int(input())
for i in range(n):
    name, price, stock = input().split()
    amazon.add_product(name, int(price), int(stock))

k = int(input())
for i in range(k):
    query = input().split()
    if query[0] == "PURCHASE":
        amazon.purchase(query[1], int(query[2]))
    elif query[0] == "RESTOCK":
        amazon.restock(query[1], int(query[2]))
    elif query[0] == "REVIEW":
        amazon.add_review(query[1], query[2], int(query[3]))

print("--- Final Inventory ---")
amazon.display_inventory()
