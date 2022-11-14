from typing import List, Set, Dict, Tuple, Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    '''
    Input: l1 = (2->4->3), l2 = (5->6->4)
    Output: (7->0->8)
    Explanation: 342 + 465 = 807.
    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        result = root
        excess = 0
        while l1 or l2 or excess:
            if l1:
                excess += l1.val
                l1 = l1.next
            if l2:
                excess += l2.val
                l2 = l2.next
            
            result.next = ListNode(excess%10)
            result = result.next
            excess = excess//10
            
        return root.next 

if __name__ == '__main__':

    l1 = [2,4,3]
    l2 = [5,6,4]
    L1_linked_data=ListNode()
    l1_1 = ListNode(2)
    l1_2 = ListNode(4)
    l1_3 = ListNode(3)

    l2_linked_data = ListNode(5)
    l2_2 = ListNode(6)
    l2_3 = ListNode(4)
    l2_linked_data.next=l2_2

    answer=Solution().addTwoNumbers(

    )
    print(answer)