class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        arr = []
        for word in words:
            x = word.split(separator)
            for k in x:
                if(k != ""):
                    arr.append(k)
        return arr
print(Solution().splitWordsBySeparator(["$easy$","$problem$"], "$"))