class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        start = newInterval[0]
        end = newInterval[1]
        for interval in intervals: # doesn't overlap
            if interval[1] < newInterval[0] or interval[0] > newInterval[1]:
                result.append(interval)
            else: # overlap
                start = min(interval[0], start)
                end = max(interval[1], end)
        result.append([start, end])
        return sorted(result)
      
# time: O(nlogn)
# space: O(n)
