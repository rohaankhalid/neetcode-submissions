# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def quickSortHelper(self, arr: List[Pair], s: int, e: int) -> None:
        # base case
        if (e - s + 1) <= 1:
            return 

        pivot = arr[e] # pivot is the last element
        left = s # pointer for left side

        # Partition: elements smaller than pivot on left side
        for i in range(s, e):
            if arr[i].key < pivot.key:
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left += 1

        # Move pivot in-between left & right sides
        arr[e] = arr[left]
        arr[left] = pivot

        # quick sort recursivel on left and right sides
        self.quickSortHelper(arr, s, left - 1)
        self.quickSortHelper(arr, left + 1, e)