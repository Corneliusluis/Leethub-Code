class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        for i, wealth in enumerate(accounts):
            accounts[i] = sum(wealth)

        return max(accounts)
        