from django.db import models

class Books(models.Model):
    """Class for representation of a book in the library"""
    book_list=[]
    def __init__(self, id, name, author, publishing_year, type, amount):
        # assign all self object 
        self.__id=id
        self.__name=name
        self.__author=author
        self.__publishing_year=publishing_year
        self.__type=type
        self.__amount=amount

        # add book item to the book list
        Books.book_list.append(self)

   
    """other functions"""

    # magic method for displaying book object
    def __repr__(self):
        return f"""name: {self.__name}, ID: {self.__id}, author: {self.__author}, published in: {self.__publishing_year}, type: {self.__type}, amount of copies in the library: {self.__amount}"""

    # magic method for getting values of object by index key
    def __getitem__(self,key):
        if key!='id' and key!='name' and key!='author' and key!='py' and key!='type' and key!='amount':
            print("Index error!")        
        elif key=='id':
            return self.__id
        elif key=='name':
            return self.__name
        elif key=='author':
            return self.__author
        elif key=='py':
            return self.__publishing_year
        elif key=='type':
            return self.__type
        else:
            return self.__amount






class Customers(models.Model):
    """Class for representation of a customer in the library"""
    customers_list=[]
    def __init__(self, id, name, city, age):
        # assign all self object 
        self.__id=id
        self.__name=name
        self.__city=city
        self.__age=str(age)

        # add customer item to the customers list
        Customers.customers_list.append(self)



    """other functions"""

    # magic method for displaying book object
    def __repr__(self):
        return f"name: {self.__name}, ID: {self.__id}, city: {self.__city}, age: {self.__age}"

    # magic method for getting values of object by index key
    def __getitem__(self,key):
        if key!='id' and key!='name' and key!='city'and key!='age':
            print("Index error!")
        elif key=='id':
            return self.__id
        elif key=='name':
            return self.__name
        elif key=='city':
            return self.__city
        else:
            return self.__age




class Loans(models.Model):
    """Class for representation of a loan in the library"""
    loan_list=[]
    def __init__(self, cust_id, book_id, loan_date, return_date):
        self.__cust_id=cust_id
        self.__book_id=book_id
        self.__loan_date=loan_date
        self.__return_date=return_date

        # add loan item to loans list
        Loans.loan_list.append(self)


    """other functions"""

    # magic method for displaying book object
    def __repr__(self):
        return f'customer ID: {self.__cust_id}, book ID: {self.__book_id}, loan date: {self.__loan_date}, return date: {self.__return_date}'

    # magic method for getting values of object by index key
    def __getitem__(self,key):
        if key!='customer' and key!='book' and key!='loan date' and key!='return date':
            print("Index error!")
        elif key=='customer':
            return self.__cust_id
        elif key=='book':
            return self.__book_id
        elif key=='loan date':
            return self.__loan_date
        else:
            return self.__return_date
