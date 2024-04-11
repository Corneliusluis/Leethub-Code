class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # converted int to str method
        # return str(x) == str(x)[::-1]
        
        # reversing the number 
        
        # negative number is excluded
        if x < 0:
            return False
        
        # begin reversing
        reversed_num = 0
        temp = x
        
        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10
            
        return x == reversed_num
        
        
        
        
        