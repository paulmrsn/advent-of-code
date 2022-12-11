import aocd 
import re

data = aocd.get_data(day=5, year=2022).split('\n\n')

def build_stacks(crates: str) -> list[list[str]]:
    lines = [line[1::4] for line in crates.splitlines()[-2::-1]]
    return [[crate for crate in column if crate != " "] for column in zip(*lines)]

def crate_mover_9000(crates: str, moves: list[tuple]) -> list[list[str]]:
    stacks = build_stacks(crates) 
    for move in moves:
        (times, from_stack, to_stack) = move
        for i in range(int(times)):
            crate = stacks[int(from_stack) -1].pop()
            stacks[int(to_stack) - 1].append(crate)
    return stacks 

def crate_mover_9001(crates: str, moves: list[tuple]) -> list[list[str]]:
    stacks = build_stacks(crates) 
    for move in moves:
        (times, from_stack, to_stack) = move
        crates_to_move = []
        for _ in range(int(times)):
            crate = stacks[int(from_stack) -1].pop()
            crates_to_move.append(crate)
        for crate in crates_to_move[::-1]:
            stacks[int(to_stack) - 1].append(crate)
    return stacks

crates = data[0]
commands_pattern = re.compile(r'move (\d+) from (\d+) to (\d+)')
moves = [re.findall(commands_pattern, command)[0] for command in data[1].splitlines()]

print("Part 1:", "".join([stack[-1] for stack in crate_mover_9000(crates, moves)]))
print("Part 2:", "".join([stack[-1] for stack in crate_mover_9001(crates, moves)]))