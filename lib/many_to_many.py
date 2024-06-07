class Author:
    def __init__(self, name):
        self.name = name
        
    def contracts(self):
        result = []
        for contract in Contract.all:
            if contract.author == self:
                result.append(contract)
        return result
    
    def books(self):
        result = []
        for contract in Contract.all:
            if contract.author == self:
                result.append(contract.book)
        return result
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        result = 0
        for contract in self.contracts():
            result += contract.royalties
        return result
        


class Book:
    def __init__(self, title):
        self.title = title
        
    def contracts(self):
        result = []
        for contract in Contract.all:
            if contract.book == self:
                result.append(contract)
        return result
    
    def authors(self):
        result = []
        for contract in Contract.all:
            result.append(contract.author)
        return result

class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise ValueError('value must be an Author instance')
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if isinstance(value, Book):
            self._book = value
        else:
            raise ValueError('value must be a Book instance')
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if isinstance(value, str):
            self._date = value
        else:
            raise ValueError('value must be a string')
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if isinstance(value, (int, float)):
            self._royalties = value
        else:
            raise ValueError('value must be an int or float')
        
    @classmethod
    def contracts_by_date(cls, date):
        result = []
        for contract in cls.all:
            if contract.date == date:
                result.append(contract)
        return result