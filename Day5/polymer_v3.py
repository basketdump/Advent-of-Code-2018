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
        """ Removes a unit type, regardless of polarity, from the polymer """
        new_polymer = []
        unit_type = unit_type.lower()
        for unit in self.units:
            if unit.lower() == unit_type:
                continue
            else:
                new_polymer.append(unit)
        
        self.units = new_polymer

    def is_polar(self, u1, u2):
        """ Checks to see if unit 1 and unit 2 are polar opposites of same type """
        # Polarity is defined by the same letter type but differing case
        return u1.lower() == u2.lower() and (u1 != u2)

    def length(self):
        """ Small wrapper for getting current length of polymer """
        return len(self.units)

    def __str__(self):
        """ Used for debugging purposes """
        result = ''
        for unit in self.units:
            result += unit
        
        return result
