from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_map = defaultdict()
        
        for word in strs:
            char_count = [0]*26
            for c in word:
                char_count[ord(c) - ord('a')] += 1 
            char_count = tuple(char_count)
            
            if char_count in count_map:
                count_map[char_count].append(word)
            else:
                count_map[char_count] = [word]

        return list(count_map.values())
