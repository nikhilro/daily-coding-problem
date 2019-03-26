import bisect


def itinerary_naive(routes, start):  # not tested, O(n) space, runtime? pre bad but standard backtrack
    flights = {}

    def plan(itinerary):
        if len(flights) == 0:
            return itinerary

        cur = itinerary[0]
        if cur in flights:
            dest = flights.pop(cur)
        else:
            return None

        if len(dest) == 1:
            itinerary += dest
            return plan(itinerary)
        else:
            for i, option in enumerate(dest):
                itinerary.append(option)
                flights[cur] = dest[i - 1:i]
                attempt = plan(itinerary)
                if attempt is not None:
                    return attempt
                else:
                    itinerary.pop()
                    flights.pop(cur)
        return itinerary

    for dept, arr in routes:
        if dept not in flights:
            flights[dept] = [arr]
        else:
            bisect.insort(flights[dept], arr)

    return plan([start])

# don't know a straightforward better way than backtracking