def decode(encoded): # O(n) space, O(n) time, not tested
    decoded, num = "", ""
    for char in encoded:
        if char.isdigit():
            num += char 
        else:
            decoded += int(num) * char 
    return decoded 

def encode(message): # O(n) space, O(n) time, not tested
    encoded, i, num = "", 0, 1
    for i, char in enumerate(message[1:]):
        if char != message[i]:
            encoded += str(num) + message[i]
            num = 0
        num += 1
    encoded += str(num) + message[-1]
