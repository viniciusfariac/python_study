# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(l1, l2):
        sum_l1 = 0
        sum_l2 = 0
        for i in range(len(l1)):
            value = len(l1) - i - 1
            sum_l1 += pow(10, value) * l1[value]

        for i in range(len(l2)):
            value = len(l2) - i - 1
            sum_l2 += pow(10, value) * l2[value]

        sum = sum_l2 + sum_l1

        return [int(digito) for digito in str(sum)]

print(Solution.addTwoNumbers(l1=[2,4,3], l2=[5,6,4]))