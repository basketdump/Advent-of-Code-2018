from datetime import datetime

class Event:
    def __init__(self, event_string):
        event = self.__parseEventString(event_string)
        self.occurred_on = event[0]
        self.type = event[1]
        self.action = event[2]


    def __parseEventString(self, event_string):
        event = []
        event_split = event_string.split()
        
        # Add datetime stamp
        event.append(datetime.strptime((event_split[0] + ' ' + event_split[1]), '[%Y-%m-%d %H:%M]'))
        
        if event_split[len(event_split)-1] == 'shift':
            event.append(0)
        elif event_split[len(event_split)-1] == 'asleep':
            event.append(1)
        else:
            event.append(2)
        
        event.append(event_split[2:])
        # event[time stamp, type]
        return event


    def GetGuardID(self):
        if (self.type == 0):
            return int(self.action[1][1:])
        else:
            return -1


    def __lt__(self, other):
        return self.occurred_on < other.occurred_on
    

    def __le__(self, other):
        return self.occurred_on <= other.occurred_on

    
    def __gt__(self, other):
        return self.occurred_on > other.occurred_on
    

    def __ge__(self, other):
        return self.occurred_on >= other.occurred_on
    
    
    def __eq__(self, other):
        return self.occurred_on == other.occurred_on
    

    def __ne__(self, other):
        return self.occurred_on != other.occurred_on
