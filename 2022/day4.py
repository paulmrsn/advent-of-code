import aocd

class Section:
    def __init__(self, input: str):
        [start, _, end] = input.partition("-")
        self.start = int(start)
        self.end = int(end)
    
    def __contains__(self, other):
        return (self.start <= other.start and other.start <= self.end and 
        self.start <= other.end and other.end <= self.end)

    def intersects(self, other):
        return self.start <= other.end and self.end >= other.start

def from_pair(pair: str):
    [s1, _, s2] = pair.partition(',')
    return (Section(s1), Section(s2))

sections = [from_pair(pair) for pair in aocd.get_data(day=4, year=2022).splitlines()]

print("Part 1:",sum(1 for s1, s2 in sections if s1 in s2 or s2 in s1))
print("Part 2:",sum(1 for s1, s2 in sections if s1.intersects(s2)))
