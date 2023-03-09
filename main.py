import sys

class TicketBooking:
    def __init__(self, max_seats):
        self.max_seats = max_seats
        self.available_seats = max_seats
        self.booked_seats = {}

    def display_seats(self):
        print(f"\nTotal seats available: {self.available_seats}")
        for seat, name in self.booked_seats.items():
            print(f"Seat {seat} booked by {name}")

    def book_ticket(self, name, num_seats):
        if num_seats <= self.available_seats:
            seats = self._get_seats(num_seats)
            self.booked_seats.update(seats)
            self.available_seats -= num_seats
            print(f"\n{name}, your booking is confirmed for seats {', '.join(seats)}.")
        else:
            print("Sorry, there are not enough seats available.")

    def cancel_ticket(self, name):
        seats = [seat for seat, booked_name in self.booked_seats.items() if booked_name == name]
        if seats:
            for seat in seats:
                del self.booked_seats[seat]
            self.available_seats += len(seats)
            print(f"\n{name}, your booking for seats {', '.join(seats)} has been cancelled.")
        else:
            print("Sorry, there are no bookings under that name.")

    def _get_seats(self, num_seats):
        seats = []
        for i in range(num_seats):
            seat = input(f"Enter seat number {i+1}: ")
            if seat not in self.booked_seats:
                seats.append(seat)
            else:
                print("That seat is already booked. Please try again.")
                return self._get_seats(num_seats)
        return {seat: input("Enter your name: ") for seat in seats}

def main():
    tb = TicketBooking(50)

    while True:
        print("\nWelcome to the ticket booking system!")
        tb.display_seats()

        print("\n1. Book a ticket")
        print("2. Cancel a ticket")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            name = input("Enter your name: ")
            num_seats = int(input("Enter the number of seats you want to book: "))
            tb.book_ticket(name, num_seats)
        elif choice == "2":
            name = input("Enter your name: ")
            tb.cancel_ticket(name)
        elif choice == "3":
            print("\nThank you for using the ticket booking system!")
            sys.exit()
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
