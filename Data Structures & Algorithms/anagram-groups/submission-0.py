class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = defaultdict(list)
        res = []
        for string in strs:
            sorted_string = ''.join(sorted(string))
            map[sorted_string].append(string)
        for key in map:
            temp = []
            for v in map[key]:
                temp.append(v)
            res.append(temp)
        
        return res





    
    