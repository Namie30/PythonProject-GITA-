import requests
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"
class BookManager:
    def __init__(self):
        self.books = [
            Book("The Knight in the Panther's Skin", "Shota Rustaveli", 1200),
            Book("To Kill a Mockingbird", "Harper Lee", 1960),
            Book("1984", "George Orwell", 1949),
            Book("Pride and Prejudice", "Jane Austen", 1813)
        ]
    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)
        print("Book added successfully!")
    def show_books(self):
        if not self.books:
            print("No books in the list.")
        else:
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")
    def search_books(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if not found_books:
            print("No books found with that title.")
        else:
            for book in found_books:
                print(book)

         #Email Part
    def notify_admin(self, customer_name, customer_phone, customer_email, book_title):
        url = "https://api.web3forms.com/submit"
        data = {
            "access_key": "",
            "email": customer_email,
            "message": f"Customer {customer_name} has ordered '{book_title}'. Contact them at {customer_phone}.",
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Notification sent successfully!")
        else:
            print(f"Failed to send notification: {response.status_code}")
            print(response.text)

class BookApp:
    def __init__(self):
        self.manager = BookManager()
    def run(self):
        while True:
            print("\nMenu:")
            print("1. Add a new book")
            print("2. Show all books")
            print("3. Search for a book by title")
            print("4. Buy a book")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                year = input("Enter the year of publication: ")
                self.manager.add_book(title, author, year)
            elif choice == "2":
                self.manager.show_books()
            elif choice == "3":
                title = input("Enter the title to search for: ")
                self.manager.search_books(title)
            elif choice == "4":
                title = input("Enter the title of the book you want to buy: ")

                found_books = [book for book in self.manager.books if book.title.lower() == title.lower()]
                if found_books:
                    customer_name = input("Enter your name: ")
                    customer_phone = input("Enter your phone number: ")
                    customer_email = input("Enter your email: ")
                    self.manager.notify_admin(customer_name, customer_phone, customer_email, title)
                    print("Notification has been sent, we will contact you shortly, thanks for the purchase.")
                else:
                    print("Book not found.")
            elif choice == "5":
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = BookApp()
    app.run()
