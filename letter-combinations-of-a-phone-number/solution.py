class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = [] 
        subset = ""
        letters = ["", "", "abc", "def", "ghi", "jkl","mno","pqrs", "tuv", "wxyz"]
        
        def dfs(i):
            nonlocal subset

            if i >= len(digits):
                res.append(subset)
                return
     
            currDigit = int(digits[i])

            subset += letters[currDigit][0]
            dfs(i+1)
            subset = subset[:-1]

            subset += letters[currDigit][1]
            dfs(i+1)
            subset = subset[:-1]

            subset += letters[currDigit][2]
            dfs(i+1)
            subset = subset[:-1]

            if currDigit in (7,9):
                subset += letters[currDigit][3]
                dfs(i+1)
                subset = subset[:-1]
            
        dfs(0)
        return res