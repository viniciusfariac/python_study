class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0
        preview = 0

        for i in s[::-1]:
            current = roman.get(i)
            ## 5 > 1
            if (current >= preview):
                sum += current
            else:
                sum -= current
            preview = current
        
        return sum

print(Solution.romanToInt("", "MCMXCIV"))