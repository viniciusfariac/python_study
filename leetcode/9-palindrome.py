class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0 or (x % 10 == 0 and x != 0):
        #     return False
        x_str = str(x)

        reverse = x_str[::-1]
        return reverse == x_str
        

print(Solution.isPalindrome("", 1021))



# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0 or (x % 10 == 0 and x != 0):
#             return False
#         reverse_number = 0

#         while(x > reverse_number):
#             rest = x % 10
#             reverse_number = reverse_number * 10 + rest
#             x = x // 10
#         return reverse_number == x or reverse_number // 10 == x
        