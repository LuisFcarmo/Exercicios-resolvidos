class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_integers = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]
        for gd_integer in good_integers:
            if(gd_integer in num):
                return gd_integer
        return ""