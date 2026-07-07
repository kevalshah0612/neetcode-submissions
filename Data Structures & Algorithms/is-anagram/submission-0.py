class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        buildMap = Counter(s)

        for char in t:
            if char not in buildMap:
                return False
            buildMap[char] -= 1
            if buildMap[char] == 0:
                del buildMap[char]
        if buildMap:
            return False
        return True 
        