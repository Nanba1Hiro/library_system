# Goal: Design a system to manage books, members, and library staff.
# Implement a mechanism to issue and return books, ensuring proper checks for availability.

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        pass

    def display_info(self):
        print(f"{self.name} took out a book")
        pass


class Member(Person):
    def __init__(self, name, email, membership_id):
        super().__init__(name, email)
        self.membership_id = membership_id
        pass

    def borrow_book(self, start_date):
        self.start_date = start_date
        pass

    def return_book(self, return_date):
        self.return_date = return_date
        pass


class Staff(Person):
    def __init__(self, name, email, staff_id):
        super().__init__(name, email)
        self.staff_id = staff_id
        pass

    def manage_book(self):
        pass


class Book:
    def __init__(self, title, author, is_available):
        self.title = title
        self.author = author
        self.is_available = is_available
        pass


Member1 = Member("Simon", "simon@gmail.com", 4242)
Staff1 = Staff("Layla", "Layla@yahoo.com", 9090)
Book1 = Book("Warzone: Undeafted", "Michael J", False)
# Member1.display_info()