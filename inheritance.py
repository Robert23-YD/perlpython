# library management system


class book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year

    def displayinfo(self):
        return f"Title:{self.title},Author:{self.author},Year:{self.year}"

# child class/derived class

class librarybook(book):
    def __init__(self,title,author,year,isbn,copies_available):
        super().__init__(title,author,year)
        self.copies_available=copies_available
        self.isbn=isbn
    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -=1
            return f"{self.title} borrowed. Copies left {self.copies_available}"
        else:
            return f"no. of title{self.title} is available"

    def return_book(self):
        self.copies_available+=1
        return f"{self.title} returned. Copies left {self.copies_available}"

#usage example
book1=librarybook("Blossoms","Maina Kanani","2007",199,3000)
print(book1.displayinfo())

print(book1.borrow_book())
print(book1.return_book())

print(book1.borrow_book())
print(book1.borrow_book())
print(book1.return_book())
