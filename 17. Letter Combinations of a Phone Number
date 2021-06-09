class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict1 = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7': 'pqrs', '8':'tuv', '9':'wxyz'} 
        
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return dict1[digits]
        
        result = []
        def helper(i, curr_lst):
            if len(curr_lst) == len(digits):
                result.append("".join(curr_lst))
                return
                
            temp = dict1[digits[i]]
            for letter in temp:
                curr_lst.append(letter)
                helper(i+1, curr_lst)
                curr_lst.pop()
  
        helper(0,[])
        return result
        
        
# brute-force approach
import collections
class Solution:
    def letterCombinations(self, digits: str):
        mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = collections.deque([''])
        for d in digits:
            for _ in range(len(result)):
                prev = result.popleft()
                for letter in mapping[int(d)]:
                    result.append(prev + letter)
        return result if digits else ''
        
        
        
# approach 3        
class Solution:
    dict_of_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        result = []
        self.backtrack('', digits, result)
        return result

    def backtrack(self, combination, next_digits, result):
        if len(next_digits) == 0:
            result.append(combination)
        else:
            for letter in self.dict_of_letters[next_digits[0]]:
                self.backtrack(combination + letter, next_digits[1:], result)
