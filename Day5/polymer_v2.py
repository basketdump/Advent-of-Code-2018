class Polymer:
    def __init__(self, polymer_string):
        self.units = list(polymer_string)

    def react(self):
        """ Reacts all units in the polymer until no reactions are left """
        reacted_polymer = []
        for unit in self.units:
            if reacted_polymer and self.is_polar(unit, reacted_polymer[-1]):
                reacted_polymer.pop()
            else:
                reacted_polymer.append(unit)
        
        self.units = reacted_polymer

    def remove_type(self, unit_type):
        """ Removes a unit type, regarldess of polarity, from the polymer """
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
        """ Checks to see if unit 1 and unit 2 are polar opposites of same type """
        # Polarity is defined by the same letter type but differing case
        # ASCII difference of a lower and capital version of the same letter is 32
        # This returns true if the difference of unit 1 and unit 2 is 32 (same letter type, different case)
        return abs(ord(u1) - ord(u2)) == 32

    def length(self):
        """ Small wrapper for getting current length of polymer """
        return len(self.units)

    def __str__(self):
        """ Used for debugging purposes """
        result = ''
        for unit in self.units:
            result += unit
        
        return result
