# Author: Clara Watson
# Date: Oct 7, 2020
# Description: this is an unit test for my store simulator program

import unittest
from Store import Customer,Store,Product

class TestMyCode(unittest.TestCase):
    """Contains unit tests for my Store.py"""
    
    def test_1(self):
        """test to see if you get the correct price from the product"""
        product = Product("1", "potato", "tis a potato", 12, 8)
        result = Product.get_price(product)
        self.assertEqual(result, 12)

    def test_2(self):
        """test to see if member is a  premium member""" 
        customer = Customer("Clara","11",True)
        result = Customer.is_premium_member(customer)
        self.assertTrue(result)

    def test_3(self):
        """test to see if the search function can find a string within the list of products"""
        product1 = Product("1", "potato", "tis a potato", 12, 8)
        product2 = Product("2", "rice", "tis some rice", 13, 9)
        product3 = Product("3", "cheese", "tis some cheese", 14, 10)
        myStore = Store()
        myStore.add_product(product1)
        myStore.add_product(product2)
        myStore.add_product(product3)
        result = myStore.product_search("cheese")
        self.assertEqual("3",result)

    def test_4(self):
        """test to see if it returns none when the id doesnt match"""
        product1 = Product("4", "potato", "tis a potato", 12, 8)
        myStore = Store()
        myStore.add_product(product1)
        result = myStore.get_product_from_id("3")
        self.assertEqual(None, result)

    def test_5(self):
        """test to see if the member will be found using the member id"""
        customer = Customer("Clara","11",True)
        myStore = Store()
        myStore.add_member(customer)
        result = myStore.get_member_from_id("11")
        self.assertIs(customer, result)
  
if __name__ == '__main__':    
    unittest.main()

   
        