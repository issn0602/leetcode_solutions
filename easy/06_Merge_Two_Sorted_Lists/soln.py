class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 != None:
            if l2 !=None:
                if l1.val >= l2.val:
                    temp = l2
                    l2 = l2.next
                    temp.next = self.mergeTwoLists(l1, l2)
                else:
                    temp = l1
                    l1 = l1.next
                    temp.next = self.mergeTwoLists(l1, l2)
            else:
                return l1
        else:
            return l2