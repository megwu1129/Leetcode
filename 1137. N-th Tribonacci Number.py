# iteration
class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c = 0,1,1

        for i in range(n):
            a, b, c = b, c, a+b+c
        
        return a
      
      
# recursion
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or 2:
            return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
      
