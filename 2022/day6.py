import aocd 

def find_marker(data_stream: str, k: int = 4) -> int:
    l = 0
    r = 0
    freq = {}
    duplicates = False
    while r < len(data_stream):
        character_r = data_stream[r]
        freq[character_r] = freq.get(character_r, 0) + 1
        if freq[character_r] > 1:
            duplicates = True
        while duplicates or r - l + 1 > k:
            character_l = data_stream[l]
            freq[character_l] -= 1
            if freq[character_l] == 1:
                duplicates = False
            if freq[character_l] == 0:
                freq.pop(character_l)
            l += 1
        if r - l + 1 == k and not duplicates:
            return r + 1
        r += 1

data = aocd.get_data(day=6, year=2022)
print("Part 1:", find_marker(data))
print("Part 2:", find_marker(data, 14))