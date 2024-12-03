from aocd import get_data, submit

data = get_data(year=2024, day=2)


def solution_1():
    # Sheesh this solution is mid
    safe_reports = 0
    for report in data.splitlines():
        dec, inc, safe = False, False, True
        prev: int = None
        for level in report.split(" "):
            level = int(level)
            if not prev:
                prev = level
                continue

            if abs(level - prev) not in [1, 2, 3]:
                safe = False
                break

            if not dec and not inc:
                if level > prev:
                    inc = True
                else:
                    dec = True  # level == prev is already checked above.

            safe = True if inc and level > prev else (dec and level < prev)

            if not safe:
                break
            prev = level

        if safe:
            safe_reports += 1

    return safe_reports


# print(solution())
# submit(solution_1())


def check_safe(report):
    return all(
        abs(int(report[i]) - int(report[i - 1])) in [1, 2, 3]
        for i in range(1, len(report))
    ) and (
        all(int(report[i]) > int(report[i - 1]) for i in range(1, len(report)))
        or all(int(report[i]) < int(report[i - 1]) for i in range(1, len(report)))
    )


# Adds problem dampener.
def solution_2():
    safe_reports = 0
    for report in data.splitlines():
        report = report.split(" ")
        if check_safe(report):
            safe_reports += 1
            continue

        for i in range(len(report)):
            if check_safe(report[:i] + report[i + 1:]):
                safe_reports += 1
                break

    return safe_reports


# print(solution_2())
submit(solution_2())
