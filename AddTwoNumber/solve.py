# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    curr = None
    head = None
    #The solution list is now init
    remaining = 0
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        while l1 or l2 or self.remaining != 0: #While there is something to calculate
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + self.remaining 
            newnode = ListNode(total%10) #Create new node with val of total % 10
            
            if total >= 10: #Setting the remaining if there is
                self.remaining = total // 10
            else:
                self.remaining = 0
                
            if self.head == None: #If the solution list is empty, add newnode into list to be the head
                self.head = newnode
                
            if self.curr != None: #If there is a curr node (All loops excluding first one)
                self.curr.next = newnode #The next node of the previous loop node would be our new node
            
            self.curr = newnode #Set the newnode to be our curr node
            
            l1 = (l1.next if l1 else None) #If there is l1.next, point to the next, else set it to None
            l2 = (l2.next if l2 else None) #Apply the same thing with l2
            
        return self.head
                
                
            
        