class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = defaultdict(int)

        for i in s:
            map[i] += 1
        for j in  t:
            map[j] -= 1
        
        for v in map.values():
            if v != 0:
                return False
        return True