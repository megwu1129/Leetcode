# map
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        
        for ele in s:
            if ele in map_s:
                map_s[ele]+=1
            else:
                map_s[ele] = 1
        
        for ele in t:
            if ele in map_t:
                map_t[ele]+=1
            else:
                map_t[ele] = 1
            
        return map_s == map_t
      
      
# Time: O(n)
# Space: O(1)



# sort
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      
        s=sorted(s)
        t=sorted(t)
        
        if s!=t:
            return False

        return True
# Time: O(nlogn)
# Space: O(1)
