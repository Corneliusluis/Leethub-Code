class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        return ["Fizz" * (not i % 3) + "Buzz" * (not i % 5) or str(i) for i in range(1, n+1)]
        
#         result = []
#         base3 = 3
#         base5 = 5
#         base15 = 15
        
#         for i in xrange(1, n+1):
#             if i == base15:
#                 result.append('FizzBuzz')                
#                 base3 = base15 + 3
#                 base5 = base15 + 5
#                 base15 += 15
#             elif i == base3:
#                 result.append('Fizz')
#                 base3 += 3
#             elif i == base5:
#                 result.append("Buzz")
#                 base5 += 5
#             else:
#                 result.append(str(i))
#         return result