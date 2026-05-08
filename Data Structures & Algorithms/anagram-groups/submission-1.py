class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = defaultdict(list)
        for string in strs:
            sorted_string = ''.join(sorted(string))
            map[sorted_string].append(string)
        return list(map.values())





    
    