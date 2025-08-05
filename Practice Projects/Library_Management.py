class Library:
    def __init__(self):
        self.books = []
        self.no_of_Books = 0

    def addBook(self, book):
        self.books.append(book)
        self.no_of_Books = len(self.books)
    
    def showBooks(self):
        for book in self.books:
            print(f"-> {book}")

        print(f"Total Books: {self.no_of_Books}")
    
    def check(self):
        if(len(self.books) != self.no_of_Books):
            print("There is some problem in your program!")
        else:
            print("Don't Worry, Everything looks good")
    

lib1 = Library()

lib1.addBook("Atmoic Habit")
lib1.addBook("Sapiens")
lib1.addBook("Too Good to be True")
lib1.addBook("Ikigai")
lib1.addBook("Think Python")

lib1.showBooks()

lib1.check()