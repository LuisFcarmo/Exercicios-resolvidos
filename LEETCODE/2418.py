from typing import List

class pessoa:
    def __init__(self, name, height):
        self._name = name
        self._heigth = height
    def __lt__(self, other):
        return self._heigth > other._heigth
    def __repr__(self):
        return f"{self._name} {self._heigth}"
    @property
    def name(self):
        return self._name
    @property
    def heigth(self):
        return self._heigth
    
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = []
        resp = []
        for c in range(0, len(names)):
            arr.append(pessoa(names[c], heights[c]))
        arr = sorted(arr)
        for p in arr:
            resp.append(p.name)
        return resp
Solution().sortPeople(["Mary","John","Emma"], [180,165,170])