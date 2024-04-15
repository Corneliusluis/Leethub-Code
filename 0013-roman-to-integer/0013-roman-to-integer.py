class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        symbol = ["I", "V", "X", "L", "C", "D", "M", "IV", "IX", "XL", "XC", "CD", "CM"]
        value = [1, 5, 10, 50, 100, 500, 1000, 4, 9, 40, 90, 400, 900]
        
        roman_num = dict(zip(symbol, value))
        
        # my own method - 15 Apr 2024
        
#         i = 0
#         num = 0
        
#         while i < len(s):
#             if s[i:i+2] in roman_num:
#                 num += roman_num[s[i:i+2]]
#                 i += 2
#             else:
#                 num += roman_num[s[i]]
#                 i += 1
        
#         return num

        # method from discussion
        num = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and roman_num[s[i]] < roman_num[s[i+1]]:
                num -= roman_num[s[i]]
            else:
                num += roman_num[s[i]]
        
        return num
        
                