from typing import List

list = [1, 1, 3, 4, 5, 6, 6, 7]
val = 6

def removeDuplicates(self, list: List[int], val: int) -> int:
    i = 0
    while i < len(list):
        if list[i] == val:
            list[i], list[-1] = list[-1], list[i]
            list.pop()
        else:
            i += 1
    return len(list)

print(removeDuplicates(None, list, val))
print(list)