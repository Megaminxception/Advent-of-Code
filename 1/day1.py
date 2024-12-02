from typing import *
import heapq
from collections import defaultdict

def read_input(file_path: str) -> List[tuple]:
    res = []
    with open(file_path) as file:
        for line in file:
            split_lines = line.split(" ")
            res.append((int(split_lines[0]), int(split_lines[-1])))
    return res

def d1p1_solution():
    file_input = read_input("Advent-of-Code/1/day1p1.txt")
    
    q1, q2 = [], []

    heapq.heapify(q1)
    heapq.heapify(q2)

    for x, y in file_input:
        heapq.heappush(q1, x)
        heapq.heappush(q2, y)

    distance = 0
    while q1 and q2:
        x, y = heapq.heappop(q1), heapq.heappop(q2)
        distance += abs(x - y)

    return distance

# print(read_input("/Users/elijahtruitt/Documents/code/advent_of_code/day1p1.txt"))
# print(d1p1_solution())

"""
================================================
PART 2
================================================
"""

def d1p2_solution():
    file_input = read_input("Advent-of-Code/1/day1p1.txt")


    d = defaultdict(int)
    for _, y in file_input:
        d[y] += 1
    
    similarity_score = 0
    for x, _ in file_input:
        similarity_score += x * d[x]
    
    return similarity_score


print(d1p2_solution())