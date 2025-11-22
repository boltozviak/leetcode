from collections import Counter

class Solution:
    '''
    O(n)

    '''
    def firstUniqChar(self, s: str) -> int:
        frequent_dict = {}
        for letter in s:
            frequent_dict[letter] = frequent_dict.get(letter, 0) + 1
        for i, v in enumerate(s):
            if frequent_dict[v] == 1:
                return i
        return -1
    
    # def firstUniqChar(self, s: str) -> int:
    #     '''
    #     O(n)
    #     '''
    #     c = Counter(s)
    #     for i, v in enumerate(s):
    #         if c[v] == 1:
    #             return i
    #     return -1