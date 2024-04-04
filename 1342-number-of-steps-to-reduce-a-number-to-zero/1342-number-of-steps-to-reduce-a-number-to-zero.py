class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        # Iterative Solution
        
#         steps = 0
        
#         while num != 0:
#             steps += 1
#             if num & 1:
#                 num -= 1
#             else:
#                 num >>= 1
            
#         return steps

        # Bit Manipulation Solution
    
        """
        bin(num).count('1') -> to count steps for odd number. Total of number 1 is the same as the time needed to subtract the value by 1.
        len(bin(num)) -> to count steps for even number. When it try to divide the value by 2, it's similar to do bitwise right shift. The length of the binary version of the specified int is the same as the number of steps to reduce it to zero.
        -1 -> it's to remove the steps of bit manipulation where we don't want to bitwise right shift again after 1 bit left.
        -2 -> to remove excess length from the bin function that always start with 0b.
        """
        return bin(num).count('1') + len(bin(num)) - 2 - 1
    
        
    
        