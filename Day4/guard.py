from shift import Shift

class Guard:
    def __init__(self, id):
        self.id = id
        self.shifts = []
        self.minutes_asleep = []
        for i in range(60):
            self.minutes_asleep.append(0)
    

    def add_shift(self, shift):
        self.shifts.append(shift)
        self.minutes_asleep = [sum(pair) for pair in zip(self.minutes_asleep, shift.minutes_asleep())]


    def __eq__(self, other):
        return self.id == other.id
    

    def __ne__(self, other):
        return self.id != other.id
    

    def __lt__(self, other):
        return self.id < other.id
    

    def __le__(self, other):
        return self.id <= other.id
    

    def __gt__(self, other):
        return self.id > other.id
    

    def __ge__(self, other):
        return self.id >= other.id
