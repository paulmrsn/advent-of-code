import aocd
from enum import Enum

class Shape:
    def __init__(self, name, score, beats, loses):
        self.name = name
        self.score = score 
        self.beats = beats 
        self.loses = loses

    def __gt__(self, other):
        return other.name == self.beats

class Shapes(Enum):
    Rock = Shape("Rock", 1, "Scissors", "Paper") 
    Paper = Shape("Paper", 2, "Rock", "Scissors")
    Scissors = Shape("Scissors", 3, "Paper", "Rock")

    def __gt__(self, other):
        return self.value > other.value

strategy = list(filter(None, aocd.get_data(day=2, year=2022).splitlines()))

shapes_p1 = {"A": Shapes.Rock, "B": Shapes.Paper, "C": Shapes.Scissors}
shapes_p2 = {"X": Shapes.Rock, "Y": Shapes.Paper, "Z": Shapes.Scissors}

def play_game(p1: Shapes, p2: Shapes) -> int: 
    if p2 > p1:
        return 6
    elif p1 > p2:
        return 0
    else:
        return 3

def generate_game(p1: Shapes, outcome: str) -> tuple[int, Shapes]: 
    match outcome: 
        case 'X': # lose
            return (0, Shapes[p1.value.beats])
        case 'Y': # draw
            return (3, p1)
        case 'Z': # win
            return (6, Shapes[p1.value.loses])

def play_round(input: str) -> int:
    [p1, _, p2]= input.partition(" ")
    p1 = shapes_p1[p1]
    p2 = shapes_p2[p2]

    return play_game(p1, p2) + p2.value.score

def play_round_2(input: str) -> int:
    [p1, _, outcome_code]= input.partition(" ")
    p1 = shapes_p1[p1]
    game_outcome = generate_game(p1, outcome_code)

    return game_outcome[0] + game_outcome[1].value.score

print("Part 1:", sum([play_round(round) for round in strategy]))
print("Part 2:", sum([play_round_2(round) for round in strategy]))