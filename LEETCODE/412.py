class Solution:
    def fizzBuzz(self, n):
        a = list()
        for c in range(1, n+1):
            if(n%3 == 5 and n%5 ==0):
                a.insert(c, "FizzBuzz")
            elif(n%3 == 0):
                a.insert(c, "Fizz")
            elif(n%5 == 0):
                a.insert(c, "Buzz")
            else:
                a.insert(c, str(c))