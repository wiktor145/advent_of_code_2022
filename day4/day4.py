class Range:
    def __init__(self, start: str, end: str):
        self.start = start
        self.end = end

        self.range_set = set(range(int(start), int(end) + 1))

    def fully_contains(self, other_range) -> bool:
        for element in other_range.range_set:
            if element not in self.range_set:
                return False

        return True


class Pair:
    def __init__(self, first_range: Range, second_range: Range):
        self.first_range = first_range
        self.second_range = second_range

    def one_contain_the_other(self):
        return self.first_range.fully_contains(self.second_range) \
            or self.second_range.fully_contains(self.first_range)


def read_input(filename="input.txt") -> list[Pair]:
    pairs_list = []
    with open(filename, "r") as file:
        for line in file:
            first_range_str, second_range_str = line.split(",")
            first_range = Range(*first_range_str.split("-"))
            second_range = Range(*second_range_str.split("-"))

            pairs_list.append(Pair(first_range, second_range))

    return pairs_list


def count_pairs_that_one_range_fully_contain_other(pairs_list: list[Pair]) -> int:
    count: int = 0
    for pair in pairs_list:
        if pair.one_contain_the_other():
            count += 1

    return count


if __name__ == '__main__':
    pairs_list: list[Pair] = read_input()
    number_of_containing_pairs: int = count_pairs_that_one_range_fully_contain_other(pairs_list)

    print("In how many assignment pairs does one range fully contain the other?")
    print(f"Answer: {number_of_containing_pairs}")
