

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        
        if not headA or not headB:
            return None
        
        pA = headA
        pB = headB
        
        # Traverse both lists until they meet or both reach the end (null)
        while pA != pB:
            # If pA is at the end, redirect it to headB, otherwise move to the next node
            pA = pA.next if pA else headB
            
            # If pB is at the end, redirect it to headA, otherwise move to the next node
            pB = pB.next if pB else headA
            
        return pA # pA is the intersection node, or null if no intersection