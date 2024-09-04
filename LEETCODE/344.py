class Solution:
    def swap(self, vect, ind1, ind2):
        vect[ind1], vect[ind2] = vect[ind2], vect[ind1]
        return vect
        
    def reverseString(self, s: list[str]) -> None:
        end = len(s)-1
        begin = 0
        while(begin < end):
            s = self.swap(s, begin, end)
            begin+=1
            end-=1
