class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        res = [True]*n
        res[0] = False
        res[1] = False
        
        for i in range(2, int(sqrt(n))+1):
            if res[i] is True:
                for j in range(i*i, n, i):
                    res[j] = False
                    
        return sum(res)
                    
