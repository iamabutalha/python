class Flight:

    def __init__(self, capicity):
        self.capicity = capicity
        self.passenger = []

    def add_passenger(self, name):
        if not self.open_seat() :
            return False
        self.passenger.append(name)
        return True
           

    def open_seat(self):
        return self.capicity - len(self.passenger)

fligth = Flight(capicity=3)

names = ["Hagrid", "Harry", "Hermonie", "Darco","Ron"]
 
for f in names:
    if fligth.add_passenger(f):
        print(f"Added {f} to fligth")
    else:
        print(f"No avilabele seat for {f}") 