import regex as re


class Stack:
    def __init__(self):
        self.items_list: list[str] = []

    def add(self, item: str):
        self.items_list.append(item)

    def get(self) -> str:
        return self.items_list.pop()

    def peek(self) -> str:
        if self.items_list:
            return self.items_list[len(self.items_list) - 1]
        else:
            return ""

    def reverse(self):
        self.items_list.reverse()

    def __str__(self):
        return str(self.items_list)


class Move:
    def __init__(self, from_stack: int, to_stack: int, items_number: int):
        self.from_stack: int = from_stack
        self.to_stack: int = to_stack
        self.items_number: int = items_number


class Cargo:
    def __init__(self, stacks: list[Stack]):
        self.stacks: list[Stack] = stacks

    def __str__(self):
        string = ""
        for stack in self.stacks:
            string += str(stack) + "\n"

        return string

    def move_items(self, move: Move):
        for _ in range(move.items_number):
            self.stacks[move.to_stack - 1].add(self.stacks[move.from_stack - 1].get())

    def get_tops_of_stacks(self) -> str:
        tops: str = ""
        for stack in self.stacks:
            tops += stack.peek()

        return tops


def make_moves(list_of_moves: list[Move], cargo: Cargo):
    for move in list_of_moves:
        cargo.move_items(move)


def parse_cargo(cargo_part) -> Cargo:
    stacks = [Stack() for _ in range((len(cargo_part.split("\n")[0]) + 1) // 4)]

    for line in cargo_part.split("\n"):
        line = line + " "
        groups = [line[i:i + 4] for i in range(0, len(line), 4)]

        for i, group in enumerate(groups):
            if group[0] == "[":
                stacks[i].add(group[1])

    for stack in stacks:
        stack.reverse()

    return Cargo(stacks=stacks)


def pase_list_of_moves(moves_part) -> list[Move]:
    pattern = "^move (\d+) from (\d+) to (\d+)$"
    list_of_moves = []

    for line in moves_part.split("\n"):
        match = re.search(pattern, line)
        list_of_moves.append(Move(from_stack=int(match.group(2)),
                                  to_stack=int(match.group(3)),
                                  items_number=int(match.group(1))))

    return list_of_moves


def read_input(filename="input.txt") -> (Cargo, list[Move]):
    with open(filename, "r") as file:
        cargo_part: str = ""
        moves_part: str = ""

        cargo_ready = False

        for line in file:
            if not line.strip():
                cargo_ready = True
                continue

            if cargo_ready:
                moves_part += line
            else:
                cargo_part += line

        cargo: Cargo = parse_cargo(cargo_part)
        list_of_moves: list[Move] = pase_list_of_moves(moves_part)

        return cargo, list_of_moves


if __name__ == '__main__':
    cargo, list_of_moves = read_input()
    print(cargo)
    make_moves(list_of_moves=list_of_moves, cargo=cargo)
    print(cargo.get_tops_of_stacks())
