class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        div = 1
        arr = []
        while(True):
            if(n == div):
                arr.append(n)
                break
            if(n%div == 0):
                arr.append(div)
            div+=1
           
        if(len(arr) < k):
            return -1
        return arr[k-1]
print(Solution().kthFactor(7, 2))
