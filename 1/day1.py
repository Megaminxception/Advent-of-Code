from typing import *
import heapq
from collections import defaultdict
from aocd import get_data

data = tuple((int(d[0]), int(d[-1])) for d in [x.split(" ") for x in get_data(year=2024, day=1).splitlines()])

def d1p1_solution():
    q1, q2 = [], []

    heapq.heapify(q1)
    heapq.heapify(q2)

    for x, y in data:
        heapq.heappush(q1, x)
        heapq.heappush(q2, y)

    distance = 0
    while q1 and q2:
        x, y = heapq.heappop(q1), heapq.heappop(q2)
        distance += abs(x - y)

    return distance

# print(read_input("/Users/elijahtruitt/Documents/code/advent_of_code/day1p1.txt"))
print(d1p1_solution())

"""
================================================
PART 2
================================================
"""

def d1p2_solution():
    d = defaultdict(int)
    for _, y in data:
        d[y] += 1
    
    similarity_score = 0
    for x, _ in data:
        similarity_score += x * d[x]
    
    return similarity_score


print(d1p2_solution())