class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = ""

        def dfs(numOpened):
            nonlocal subset
            if len(subset) == n * 2:
                res.append(subset)
                return

            if numOpened == n:
                # should only add ")"
                subset += ")"
                dfs(numOpened)
                subset = subset[:-1]
                return
            
            subset += "("
            dfs(numOpened + 1)
            subset = subset[:-1]

            if numOpened > len(subset) - numOpened:
                subset += ")"
                dfs(numOpened)
                subset = subset[:-1]
        dfs(0)
        return res
