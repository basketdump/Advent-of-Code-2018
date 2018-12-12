from event import Event

class Shift:
    def __init__(self):
        self.events = []


    def add_event(self, event):
        self.events.append(event)


    def minutes_asleep(self):
        minutes_asleep = []
        for i in range(60):
            minutes_asleep.append(0)
        
        for i in range(len(self.events)):
            if self.events[i].type == 1:
                for time in range(self.events[i].occurred_on.minute, self.events[i+1].occurred_on.minute):
                    minutes_asleep[time] += 1
            else:
                continue
        
        return minutes_asleep
