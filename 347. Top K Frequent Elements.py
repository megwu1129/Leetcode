class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for num in nums:
            dict1[num] = dict1.get(num, 0) + 1
            
        res = []
        for key, value in dict1.items():
            res.append((key, value))
        
        res = sorted(res, key = lambda e:e[1], reverse = True)
        
        final = []
        for i in range(len(res)):
            if i==k:
                break
            final.append(res[i][0])
            
        return final
