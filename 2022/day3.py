import aocd
import string 

backpacks = aocd.get_data(day=3, year=2022).splitlines()

def find_wrong_fruit(backpack: str) -> str:
    middle = len(backpack) // 2
    [fruit] = set(backpack[:middle]).intersection(set(backpack[middle:]))
    return fruit

priorities = {fruit: index for index, fruit in enumerate(string.ascii_letters, 1)}

def find_badge(backpack: str, *backpacks: str) -> str:
    [badge] = set(backpack).intersection(*backpacks)
    return badge 

def find_all_badges(*backpacks):
    iterator = iter(backpacks)
    for group in zip(iterator, iterator, iterator):
        yield find_badge(*group)

print("Part 1:", sum([priorities[find_wrong_fruit(backpack)] for backpack in backpacks]))
print("Part 2:", sum([priorities[badge] for badge in find_all_badges(*backpacks)]))
