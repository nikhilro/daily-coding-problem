import time


def decode(msg):
    if msg == "":
        return 1
    if 10 <= int(msg[:2]) <= 26:
        return decode(msg[1:]) + decode(msg[2:])
    else:
        return decode(msg[1:])


start = time.time()
print(decode('1221'))
print(time.time() - start)

lookup = {}


def decode_memoized(msg):
    if msg in lookup:
        return lookup[msg]

    ans = 0
    if msg == "":
        ans = 1
    elif 10 <= int(msg[:2]) <= 26:
        ans = decode(msg[1:]) + decode(msg[2:])
    else:
        ans = decode(msg[1:])

    lookup[msg] = ans

    return ans


start = time.time()
print(decode_memoized('1221'))
print(time.time() - start)


def decode_iter_bottom_up(msg):
    prev = 1
    current = 1

    for i in reversed(range(len(msg) - 1)):
        temp = current
        current += prev if int(msg[i:i+2]) else 0
        prev = temp

    return current


start = time.time()
print(decode_iter_bottom_up('1221'))
print(time.time() - start)

def decode_iter_bottom_up_golf(msg):
    prev = 1
    current = 1

    for i in reversed(range(len(msg) - 1)):
        current, prev = \
            (current + prev, current) if int(msg[i:i+2]) else (current, current)

    return current


start = time.time()
print(decode_iter_bottom_up_golf('1221'))
print(time.time() - start)
