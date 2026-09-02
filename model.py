class Book:
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDREN = 2

    def __init__(self, title, price_code):
        self.title = title
        self.price_code = price_code

    def get_charge(self, days_rented: int) -> float:
        amount = 0
        if self.price_code == Book.REGULAR:
            amount += 2
            if days_rented > 2:
                amount += (days_rented - 2) * 1.5
        elif self.price_code == Book.NEW_RELEASE:
            amount += days_rented * 3
        elif self.price_code == Book.CHILDREN:
            amount += 1.5
            if days_rented > 3:
                amount += (days_rented - 3) * 1.5
        return amount

    def get_frequent_renter_points(self, days_rented: int) -> int:
        points = 1
        if self.price_code == Book.NEW_RELEASE and days_rented > 1:
            points += 1
        return points


class Rental:
    def __init__(self, book, days_rented):
        self.book = book
        self.days_rented = days_rented

    def get_charge(self) -> float:
        return self.book.get_charge(self.days_rented)

    def get_frequent_renter_points(self) -> int:
        return self.book.get_frequent_renter_points(self.days_rented)


class Client:
    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        self.rentals.append(rental)

    def statement(self) -> str:
        total_amount = 0
        frequent_renter_points = 0
        result = f"Rental summary for {self.name}\n"

        for rental in self.rentals:
            amount = rental.get_charge()

            # add frequent renter points
            frequent_renter_points += rental.get_frequent_renter_points()

            # show each rental result
            result += f"- {rental.book.title}: {amount}\n"
            total_amount += amount

        # show total result
        result += f"Total: {total_amount}\n"
        result += f"Points: {frequent_renter_points}"
        return result

    
class Client:
    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        self.rentals.append(rental)

    def statement(self) -> str:
        total_amount = 0
        frequent_renter_points = 0
        result = f"Rental summary for {self.name}\n"

        for rental in self.rentals:
            amount = rental.get_charge()

            # add frequent renter points
            frequent_renter_points += rental.get_frequent_renter_points()

            # show each rental result
            result += f"- {rental.book.title}: {amount}\n"
            total_amount += amount

        # show total result
        result += f"Total: {total_amount}\n"
        result += f"Points: {frequent_renter_points}"
        return result

class Client:
    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        self.rentals.append(rental)

    def statement(self) -> str:
        total_amount = 0
        frequent_renter_points = 0
        result = f"Rental summary for {self.name}\n"

        for rental in self.rentals:
            amount = rental.get_charge()

            # add frequent renter points
            frequent_renter_points += rental.get_frequent_renter_points()

            # show each rental result
            result += f"- {rental.book.title}: {amount}\n"
            total_amount += amount

        # show total result
        result += f"Total: {total_amount}\n"
        result += f"Points: {frequent_renter_points}"
        return result