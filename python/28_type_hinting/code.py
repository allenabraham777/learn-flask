from typing import List


def list_avg(sequence: List[int]) -> float:
    return sum(sequence) / len(sequence)


list_avg([123, 456])
