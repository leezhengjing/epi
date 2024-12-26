from typing import List
def alternate(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        arr[i: i + 2] = sorted(arr[i: i + 2], reverse = i % 2)
    return arr

