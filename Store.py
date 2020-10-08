# Author: Clara Watson
# Date: Oct 7, 2020
# Description: this is an online store simulator

class Product: 
    """ represents a product with an ID code, title, description, price and quantity available"""
   
    def __init__(self, ID, title, description, price, quantity_available):  # constructor of class
        """initilizes the 5 private data members"""
        self._ID = ID
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_product_id(self):
        """will return the ID"""
        return self._ID

    def get_title(self):
        """will return the title"""
        return self._title

    def get_description(self): 
        """will return the description"""
        return self._description

    def get_price(self):
        """will return the price"""
        return int(self._price)

    def get_quantity_available(self):
        """will return the quantity available"""
        return int(self._quantity_available)
    
    def decrease_quantity(self):
        num = get_quantity_available()
        new = num - 1
        return new

class Customer:
    """represents a customer with a name and account ID. Customers must be members of the Store to make a purchase. Premium members get free shipping."""
    

    def __init__(self, name, ID, premium_member):  # constructor of class
        """initilizes the 3 private data members"""
        self._name = name
        self._ID = ID
        self._premium_member = None
        self._cart = []
        

    def get_name(self):
        """will return the customer name"""
        return self._name

    def get_customer_id(self):
        """will return the customer id"""
        return self._customer_id

    def is_premium_member(self):
        """will return true or false if the customer is a premuim member"""
        return bool(self._preimum_member)
    
    def add_product_to_cart(self, product_ID):
        """adds product to the cart in a list"""
        for x in product_ID:
            self._cart.append(x)
    
    def empty_cart(self):
        """gets rid of everything in cart"""
        self._cart.clear()

    def get_cart(self):
        """will return the cart in a list form"""
        return self._cart


class Store: 
    """represents a store, which has some number of products in its inventory and some number of customers as members"""
    
    def __init__(self):  # constructor of class
        """initilizes the 2 private data members"""
        self._inventory = []
        self._members = []
        self._cart = []
    
    def add_product(self, product):
        """this adds a product to the inventory"""
        self._inventory.append(product)

    def add_member(self, member):
        """this adds a memeber to the list of memebers"""
        self._members.append(member)

    def get_product_from_id(self, product_ID):
        """finds the product from teh inputed id"""
        try:
            for x in self._inventory:
                ID_from_list = Product.get_product_id(x)
                if ID_from_list == product_ID:
                    return x
        except:
            return None

    def get_member_from_id(self, member_ID):
        """finds the member based on the inputed id"""
        try:
            for x in self._members:
                ID_from_list = Customer.get_customer_id(x)
                if ID_from_list == member_ID:
                    return x
        except:
            return None

    def product_search(self, string):
        """searches if a string is in any of the products in the inventories title or description"""
        newlist = []
        for x in self._inventory:
            title = Product.get_title(x)
            description = Product.get_description(x)
            if string in (title or description):
                newlist.append(Product.get_product_id(x))
        return newlist

    def add_product_to_member_cart(self, product_ID, customer_ID):
        """this adds a product to the members cart"""
        productIsFound = None
        for x in self._inventory:
            ID = Product.get_product_id(x)
            if product_ID == ID: 
                 productIsFound = True
                 product = x
                 break
            else:
                productIsFound = False
        custmerIsFound = ModuleNotFoundError
        if productIsFound:
            for x in self._members:
                ID = Customer.get_customer_id(x)
                if customer_ID == ID: 
                    custmerIsFound = True
                    break
                else:
                    custmerIsFound = False
        else:
            print("product ID not found")
        if custmerIsFound:
            quantity = Product.get_quantity_available(product)
            if quantity == 0: 
                print("product out of stock")
            else: 
                Product.decrease_quantity(product)
                self._cart.append(product)
                print("product added to cart")
        else: 
            print("member ID not found")

    def check_out_member(self,customer_ID):
        """figures out how much money each thing in members cart is worth plus shipping and then clears cart"""
        try: 
            member = get_member_from_id(customer_ID)
        except:
            raise InvalidCheckoutError("no member found")
        for x in self._cart:
            quantity = Product.get_quantity_available(x)
            if quantity > 0: 
                Product.decrease_quantity(x)
                price = Product.get_price(x)
                total = total + price
        if Customer.is_premium_member(member):
            cartCost = total
        else: 
            cartCost = (total * .07) + total
        self._cart.clear()
            
class InvalidCheckoutError(Exception):
    pass

def main(customer_ID):
    try: 
        member = Store.get_member_from_id(customer_ID)
    except:
        raise InvalidCheckoutError("no member found")
    for x in Store._cart:
        quantity = Product.get_quantity_available(x)
        if quantity > 0: 
            Product.decrease_quantity(x)
            price = Product.get_price(x)
            total = total + price
    if Customer.is_premium_member(member):
        cartCost = total
    else: 
        cartCost = (total * .07) + total
    Store._cart.clear()

if __name__ == "__main__":
    main()




    


    

    
        




