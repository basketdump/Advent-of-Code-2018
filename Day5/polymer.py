class Polymer:
    def __init__(self, polymer_string):
        self.units = list(polymer_string)

    def react(self):
        current = 1
        while (current < len(self.units)):
            if self.is_polar(self.units[current], self.units[current-1]):
                self.units.pop(current)
                self.units.pop(current-1)
                if (current > 1):
                    current -= 1
            else:
                current += 1

    def remove_type(self, unit_type):
        unit_type = unit_type.lower()
        current = 0
        while current < self.length():
            if self.units[current].lower() == unit_type:
                self.units.pop(current)
                if current > 0:
                    current -= 1
            else:
                current += 1

    def is_polar(self, u1, u2):
        # Polarity is defined by the same letter type but differing case
        # ASCII difference of a lower and capital version of the same letter is 32
        # This returns true if the difference of unit 1 and unit 2 is 32 (same letter type, different case)
        return abs(ord(u1) - ord(u2)) == 32

    def length(self):
        return len(self.units)

    def __str__(self):
        result = ''
        for unit in self.units:
            result += unit
        
        return result
