def match(string, regex):  # O(max(len(regex), len(string))) time, O(1) space
    ptr_regex, ptr_str = 0, 0
    while ptr_str < len(string) and ptr_regex < len(regex):
        if regex[ptr_regex] == '.':
            ptr_regex, ptr_str = ptr_regex + 1, ptr_str + 1
        elif regex[ptr_regex] == '*':
            while match(string[ptr_str], regex[ptr_regex - 1]) \
                    and not match(string[ptr_str], regex[ptr_regex + 1]):
                ptr_str += 1
            ptr_regex += 1
        elif regex[ptr_regex] == string[ptr_str]:
            ptr_regex, ptr_str = ptr_regex + 1, ptr_str + 1
        else:
            break

    if ptr_regex == len(regex) and ptr_str == len(string):
        return True
    else:
        return False


print(match('ray', 'ra.'), match('raymond', 'ra.'), match('chat', '.*at'))
