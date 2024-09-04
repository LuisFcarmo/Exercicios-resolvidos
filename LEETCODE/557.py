class Solution:
    def reverseWords(self, s: str) -> str:
        vect = s.split(" ")
        rtr = ""
        for c in range(0, len(vect)):
            vect[c] = vect[c][::-1]
        for c in range(len(vect)):
            if(c!= len(vect)-1):
                rtr += vect[c] + " "
            else:
                rtr += vect[c]
        return rtr
print(Solution().reverseWords("Let's take LeetCode contest"))