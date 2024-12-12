class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        
        vowel_count = [0] * (n + 1)
        consonant_count = [0] * (n + 1)
        
        for i in range(1, n + 1):
            vowel_count[i] = vowel_count[i - 1] + (1 if s[i - 1] in vowels_set else 0)
            consonant_count[i] = consonant_count[i - 1] + (0 if s[i - 1] in vowels_set else 1)
        
       
        count = 0
        for start in range(n):
            for end in range(start + 1, n + 1):
                vowels = vowel_count[end] - vowel_count[start]
                consonants = consonant_count[end] - consonant_count[start]
                if vowels == consonants and (vowels * consonants) % k == 0:
                    count += 1
                    
        return count

