from typing import List
from random import randint
def find_kth_largest_element(k: int, arr: List[int]) -> int:
    def find_kth(left: int, right: int, pivot_idx: int) -> int:
        pivot_value = arr[pivot_idx]
        new_pivot_idx = left
        arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
        for i in range(left, right):
            if arr[i] > pivot_value:
                arr[i], arr[new_pivot_idx] = arr[new_pivot_idx], arr[i]
                new_pivot_idx += 1
        arr[new_pivot_idx], arr[right] = arr[right], arr[new_pivot_idx]
        return new_pivot_idx
    left, right = 0, len(arr) - 1
    while left <= right:
        pivot_idx = randint(left, right)
        new_pivot_idx = find_kth(left, right, pivot_idx)
        if new_pivot_idx == k - 1:
            return arr[new_pivot_idx]
        elif new_pivot_idx > k - 1:
            right = new_pivot_idx - 1
        else:
            left = new_pivot_idx + 1


    