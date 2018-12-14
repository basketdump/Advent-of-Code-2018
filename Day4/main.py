import sys
from event import Event
from shift import Shift
from guard import Guard
from algorithms import binary_insert, binary_search, index_of_max


def main(input_file):
    # Load input as events in sorted order (Event timestamp)
    events = []
    with open(input_file) as file:
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
            tmp_guard = Guard(e.GetGuardID())
            if len(guards) > 0:
                guards[current_guard_id].add_shift(current_shift)
                current_shift = Shift()
                
                index = binary_search(guards, tmp_guard)
                if index == -1:
                    current_guard_id = binary_insert(guards, tmp_guard)
                else:
                    current_guard_id = index
            else:
                guards.append(tmp_guard)
        current_shift.add_event(e)
    
    # Find guard who slept most
    result_index = index_of_max([sum(g.minutes_asleep) for g in guards])

    # Most slept minute
    msm = guards[result_index].get_most_slept_minute()

    # Part 1 Answer
    print("Guard #", guards[result_index].id, sep='')
    print("Slept most at minute", msm)
    print("Part 1 Answer:", guards[result_index].id * msm)

    print()

    # Part 2 Answer
    msm_count = [g.minutes_asleep[g.get_most_slept_minute()] for g in guards]
    result_index = index_of_max(msm_count)
    msm = guards[result_index].get_most_slept_minute()
    
    print("Guard #", guards[result_index].id, sep='')
    print("Slept most at minute ", msm, ', ', msm_count[result_index], ' times', sep='')
    print("Part 2 Answer:", guards[result_index].id * msm)


main(sys.argv[1])
