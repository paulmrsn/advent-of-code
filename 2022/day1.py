import heapq
import aocd

elves_by_calories = [sum(map(int, filter(None, elf.split('\n')))) for elf in aocd.get_data(day=1, year=2022).split('\n\n')]

print("Part 1:",  max(elves_by_calories))
print("Part 2:", sum(heapq.nlargest(3, elves_by_calories)))
