"""Write a Class Train which has methods to
book a ticket,
get status (no of seats)
and get fare
information of train running under Indian Railways."""

from random import randint


class Train:

    def __init__(self, trainNo):
        self.t = trainNo

    def booking(self, t_from, t_to):
        print(f"Ticket is booking in Train No:{self.t} from {t_from} to {t_to}")

    def get_status(self):
        print(f"Train No:{self.t} is running on time.")

    def get_fare(self, t_from, t_to):
        print(
            f"Ticket fare in Train no:{self.t} from {t_from} to {t_to} is {randint(50, 141)}km "
        )


t = Train(1205)
t.booking("navaron", "Khulna")
t.get_status()
t.get_fare("navaron", "Khulna")
