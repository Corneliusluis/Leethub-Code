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
        # return not collections.Counter(ransomNote) - collections.Counter(magazine)
        
        # using count method
        return all(ransomNote.count(i) <= magazine.count(i) for i in set(ransomNote))
        
        # [WIP] using my own counter implementation based on dictionary method
#         def myCounter(word):
#             counter = {}

#             for letter in word:
#                 counter[letter] = word.count(letter)

#             return counter

#         if not [myCounter(ransomNote)[x] <= myCounter(magazine)[x] for x in myCounter(ransomNote) if x in myCounter(magazine)]:
#             return False
#         return all([myCounter(ransomNote)[x] <= myCounter(magazine)[x] for x in myCounter(ransomNote) if x in myCounter(magazine)])