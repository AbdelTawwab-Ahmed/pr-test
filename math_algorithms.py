"""Statistical algorithms and mathematical utilities."""
from typing import List, Optional

def calculate_mean(values: List[float]) -> float:
    # Logic Error 1: ZeroDivisionError when values list is empty
    return sum(values) / len(values)

def binary_search(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr)  # Logic Error 2: Off-by-one, should be len(arr) - 1
    
    # Logic Error 3: Can cause IndexError when accessing arr[right]
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def get_user_display_name(user_profile: Optional[dict]) -> str:
    # Logic Error 4: Unhandled NoneType dereference (AttributeError / TypeError)
    return user_profile["personal_info"]["full_name"].strip()

def factorial(n: int) -> int:
    # Logic Error 5: Missing negative check leading to infinite recursion (RecursionError)
    if n == 0:
        return 1
    return n * factorial(n - 1)
