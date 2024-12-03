import re
from aocd import get_data, submit

data = get_data(year=2024, day=3)


def solution_1():
    mul_calls = re.findall(
        "mul\([1-9][0-9]?[0-9]?,[1-9][0-9]?[0-9]?\)",
        data,
    )
    res = 0
    for call in mul_calls:
        x, y = re.findall(
            "[1-9][0-9]?[0-9]?", call
        )  # At this point we know there's only 2 results.
        res += int(x) * int(y)
    return res


# print(solution_1())
# submit(solution_1())


def solution_2():
    mul_calls = re.findall(
        "do\(\)|don't\(\)|mul\([1-9][0-9]?[0-9]?,[1-9][0-9]?[0-9]?\)",
        data,
    )
    res = 0
    enabled = True
    for call in mul_calls:
        enabled = False if call == "don't()" else True if call == "do()" else enabled
        x, y = (
            re.findall("[1-9][0-9]?[0-9]?", call)
            if enabled and call != "do()"
            else (0, 0)
        )  # At this point we know there's only 2 results.
        res += int(x) * int(y)
    return res


# print(solution_2())
submit(solution_2())
