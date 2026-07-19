class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = defaultdict(list)
        for i in strs :
            sorted_i = ''.join(sorted(i))
            arr[sorted_i].append(i)
        return list(arr.values())
