class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        # using Counter Library
#         rn, mg = Counter(ransomNote), Counter(magazine)
        
#         if rn & mg == rn:
#             return True
#         return False
        
        # using Counter Library, but implement it in one liner
        return not collections.Counter(ransomNote) - collections.Counter(magazine)