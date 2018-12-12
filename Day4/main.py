from event import Event
from shift import Shift
from guard import Guard


def binary_search(array, element):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if element == array[mid]:
            return mid
        elif element < array[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def binary_insert(array, element):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if element == array[mid]:
            array.insert(mid, element)
            return mid
        elif element < array[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if element > array[mid]:
        mid += 1

    array.insert(mid, element)
    return mid


def main():
    # Load input as events in sorted order (Event timestamp)
    events = []
    with open('input.txt') as file:
        for line in file:
            # TODO: Binary insert based off datetime instead of append
            e = Event(line)
            if (len(events) > 0):
                binary_insert(events, e)
            else:
                events.append(e)

    # Setup guards with shifts, and those shifts with events, in sorted order (Guard ID)
    guards = []
    current_guard_id = 0
    current_shift = Shift()
    for e in events:
        if e.type == 0:
            tmp_guard = Guard(int(e.action[1][1:]))
            if len(guards) > 0:
                guards[current_guard_id].add_shift(current_shift)
                current_shift = Shift()
                
                # TODO: Clean up nasty ass split
                index = binary_search(guards, tmp_guard)
                if index == -1:
                    current_guard_id = binary_insert(guards, tmp_guard)
                else:
                    current_guard_id = index
            else:
                guards.append(tmp_guard)
        current_shift.add_event(e)
    
    # Find guard who slept most
    highest = 0
    for g in guards:
        slept = sum(g.minutes_asleep)
        if  slept > highest:
            highest = slept
            result_guard = g

    # Find most slept minute
    highest = 0
    most_slept_minute = 0
    
    for i in range(len(result_guard.minutes_asleep)):
        if result_guard.minutes_asleep[i] > highest:
            highest = result_guard.minutes_asleep[i]
            most_slept_minute = i

    # Part 1 Answer
    print("Guard #", result_guard.id, sep='')
    print("Slept most at minute", most_slept_minute)
    print("Part 1 Answer:", result_guard.id * most_slept_minute)

    # Part 2 Answer
    
main()
