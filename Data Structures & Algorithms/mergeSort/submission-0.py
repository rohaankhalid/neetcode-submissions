# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)  

    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        # base case
        if e - s + 1 <= 1: # length is 1 means only 1 element in array
            return pairs

        # middle index of the array
        m = (s + e) // 2

        # sort the left half
        self.mergeSortHelper(pairs, s, m)

        # sort the right half of the array
        self.mergeSortHelper(pairs, m + 1, e)

        # merge sorted halfs
        self.merge(pairs, s, m, e)

        return pairs

    def merge(self, arr: List[Pair], s: int, m: int, e: int) -> None:
        # copy the sorted left and right halfs to temp array
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        i = 0 # index for L
        j = 0 # index for R
        k = s # index for arr

        # merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # one of the halfs will have elements remaining
        while i < len(L):
            arr[k] = L[i]    
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1