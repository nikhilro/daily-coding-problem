def validate(rules):
    parsed_rules, seen = {}, set()

    def commit_rule(start, end, vertical, horizontal):
        parsed_rules[(start, end)] = (vertical, horizontal)
        parsed_rules[(end, start)] = (-1 * vertical, -1 * horizontal)

    def calibrate(direction):
        if direction > 0:
            return 1
        elif direction < 0:
            return -1 
        else:
            return 0

    def direction_sum(vertical, horizontal, delta):
        nv, nh = vertical + delta[0], horizontal + delta[1]
        return calibrate(nv), calibrate(nh)

    
    def parser(rule):
        direction_to_tuple = { 'N': (1, 0), 'S': (-1, 0), 'E': (0, 1), 'W': (0, -1), \
            'NE': (1, 1), 'NW': (1, -1), 'SE': (-1, 1), 'SW': (-1, -1) }
        
        start, direction, end = rule.split()
        vertical, horizontal = direction_to_tuple[direction]
    
        print(parsed_rules, start, end, (start, end) in parsed_rules)
        print((start, end) in parsed_rules and parsed_rules[(start, end)], (vertical, horizontal))
        if (start, end) in parsed_rules and parsed_rules[(start, end)] != (vertical, horizontal):
            return False

        commit_rule(start, end, vertical, horizontal)
        
        for point in seen:
            if point != start and (end, point) in parsed_rules:
                nv, nh = direction_sum(vertical, horizontal, parsed_rules[(end, point)])
                commit_rule(start, point, nv, nh)

            if point != end and (start, point) in parsed_rules:
                nv, nh = direction_sum(vertical, horizontal, parsed_rules[(point, start)])
                commit_rule(end, point, nv, nh)
        
        seen.add(start)
        seen.add(end)

    for rule in rules:
        parser(rule)

    return True

rules = ["A N B", "B NE C", "C N A"]

print(validate(rules))

rules = ["A NW B", "A N B"]

print(validate(rules))