class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            index = word.index(ch)
            reverse = word[0:index+1]
            reverse = reverse[::-1] + word[index+1:len(word)]
            return reverse
        except:
            return word
      
x = Solution().reversePrefix("abcdefd", "d")
