class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        '''
        1)словарь: 'анаграмма - [слова-перестановки]'
        2)ключ = кортеж(т.к. содержит только строки(символы) -> хэшируем) или строка(хэшируема по умолчанию)
        '''
        word_dict = {}
        for i in strs:
            key = tuple(sorted(i)) # key = "".join(sorted(i))
            if key not in word_dict:
                word_dict[key] = [i]
            elif key in word_dict:
                word_dict[key].append(i)
        return [x for x in word_dict.values()]