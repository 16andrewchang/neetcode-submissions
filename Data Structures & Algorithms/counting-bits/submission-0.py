class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            res.append(self.countones(num))
        return res
    def countones(self,n):
        count = 0
        while n > 0:
            n &= (n-1)
            count += 1
        return count

        