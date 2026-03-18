class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def rec(j, i):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return

            if self.isPali(s, j, i):
                part.append(s[j:i+1]) # explore
                rec(i+1, i+1) # recurse
                part.pop() # de-explore
            
            rec(j, i+1)

        rec(0, 0)
        return res

    
    def isPali(self, s, l, r) -> bool: # check palindrome using the i and j pointers.
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

