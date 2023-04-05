from typing import List


class DuplicateChecker:
    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    def has_duplicate(self) -> bool:
        sorted_numbers = sorted(self.numbers)
        for i in range(1, len(sorted_numbers)):
            if sorted_numbers[i] == sorted_numbers[i - 1]:
                return True
        return False


class TwoSum:
    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    def find_indices(self, target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(self.numbers):
            remaining = target - self.numbers[i]
            if remaining in seen:
                return [i, seen[remaining]]
            else:
                seen[value] = i


class RotateArray:
    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    def rotate(self, k: int) -> List[int]:
        k = k % len(self.numbers)
        return self.numbers[-k:] + self.numbers[:-k]


class ReverseString:
    def __init__(self, string: str):
        self.string = string

    def reverse(self) -> str:
        return self.string[::-1]


class MedianFinder:
    @staticmethod
    def find_median(x: List[int], y: List[int]) -> float:
        z = sorted(x + y)
        n = len(z)
        if n % 2 == 0:
            result = (z[n // 2] + z[n // 2 - 1]) / 2
        else:
            result = z[n // 2]
        return result