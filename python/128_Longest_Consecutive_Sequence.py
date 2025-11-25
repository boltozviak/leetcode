class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        '''
        O(n)
        1)из множества значений берём случайное
        2)идём от него в обе стороны, удаляя элементы(чтобы не пересчитывать для каждого элемента последовательностит),
        входящие в последовательность, и считая длину последовательности справа и слева
        '''
        s = set(nums)
        max_seq = 0
        while s:
            i = s.pop()
            j = i
            left = 0
            right = 0
            while i - 1 in s:
                s.remove(i - 1)
                left += 1
                i -= 1
            while j + 1 in s:
                s.remove(j + 1)
                right += 1
                j += 1
            max_seq = max(max_seq, right + left + 1)
        return max_seq


    # def longestConsecutive(self, nums: list[int]) -> int:
    #     '''
    #     вариант с сохранением границ для значений - медленынй
    #     '''
    #     border_dict = {}
    #     max_seq = 0
    #     for n in nums:
    #         if n in border_dict:
    #             continue
    #         left = n
    #         right = n
    #         if n - 1 in border_dict:
    #             left = border_dict[n - 1][0]
    #         if n + 1 in border_dict:
    #             right = border_dict[n + 1][1]
    #         border_dict[n] = (left, right)
    #         border_dict[left] = (left, right)
    #         border_dict[right] = (left, right)
    #         max_seq = max(max_seq, right - left + 1)
    #     return max_seq