def non_repeating(s:str) -> int:
    queue = []
    mapping = {}
    for char in s:
        mapping[char] = mapping.get(char, 0) + 1

    for i, char in enumerate(s):
        if mapping[char] ==  1:
            return i
    
    return -1

s = "loveleetcode"
print(non_repeating(s))