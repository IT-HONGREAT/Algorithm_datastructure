# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
주어진 조건에 결과 잘 출력 하지만 링크드리스트 노드개념이 아님.
class Solution:
    def addTwoNumbers(self, l1, l2):

        l1_str = ""
        for s in l1:
            l1_str += str(s)

        l2_str = ""
        for s in l2:
            l2_str += str(s)

        summation = l1_str + '+' + l2_str


        summation = str(eval(summation))

        answer_num = summation[::-1]

        answer = [int(s) for s in answer_num]

        print(answer)
        # print(type(l1_str), l1_str)
        return answer"""

# 리스트 노드 하나씩 바로 적용
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next



test = Solution()
test.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4])
test.addTwoNumbers( l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9])
test.addTwoNumbers( l1 = [0], l2 = [0])