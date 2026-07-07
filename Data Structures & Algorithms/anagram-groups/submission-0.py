class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        wordMap = defaultdict(list)

        for word in strs:
            alpha = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                alpha[index] += 1
            key = tuple(alpha)
            wordMap[key].append(word)
        
        return list(wordMap.values())