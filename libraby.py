class Library :

    def __init__(self,lists, name):

        self.booklist = lists
        self.name = name
        self.lendDict = {}

   # Display the Available books in the library

    def displayBooks(self) :

        print(f"We have following books in our library: {self.name}")

        for book in self.booklist :

            print(book)

    # If someones requested for a book, it displays whether book is available to lend or not
    
    def lendBook(self, user, book) :

        if book not in self.lendDict.keys() :

            self.lendDict.update({book:user})
            print('Lender book database has been updated. You can take the book now')

        else :

            print(f"Book is already being used by {self.lendDict[book]}")
            
    # Adding a book to the list of books in the library
    
    def addbook(self, book) :

        self.booklist.append(book)
        print("Book has been added to the book list")
        
    # Returning the lending books

    def returnBook(self, book) :
        
        self.lendDict.pop(book)


if __name__ == '__main__' :

    siddhu = Library(['Python','Rich Daddy Poor daddy','Harry Potter','C++','Web developer'], 'CodeWithSiddhu')

    while(True) :

        print(f"Welcome to the {siddhu.name} library. Enter Your choice to Continue")

        print("1. Display Books")
        print("2. Lend Books")
        print("3. Add Books")
        print("4. Remove Books")

        user_choice = input()

        if user_choice not in ['1','2','3','4'] :

            print('Please Enter a valid option :')
            
            continue

        else :

            user_choice = int(user_choice)

        if user_choice == 1 :

            siddhu.displayBooks()

        elif user_choice == 2 :

            book = input("Enter the name of the book you want to lend : ")

            user = input("Enter your name : ")

            siddhu.lendBook(user,book)

        elif user_choice == 3 :

            book = input("Enter the name o the book you want to add :")
            siddhu.addbook(book)
            
        elif user_choice == 4 :

            book = input("Enter the name o the book you want to return :")

            siddhu.returnBook(book)


        else :

            print("Not a valid option")

        print("Press q to quit and c to continue")

        user_choice2 =""

        while(user_choice2 != "c" and user_choice2 != "q") :

            user_choice2 = input()

            if user_choice2 == "q" :

                exit()

            elif user_choice2 == "c" :

                continue

        
