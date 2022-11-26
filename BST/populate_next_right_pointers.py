"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root == None:
            return None
        queue = [root]
        
        
        while queue:

            next_queue = []
            last = None
            
            while queue:
                
                curr_node = queue.pop(0)

                if curr_node.right:
                    next_queue.append(curr_node.right)

                if curr_node.left:
                    next_queue.append(curr_node.left)

                
                curr_node.next = last
                last = curr_node
                
                    
            queue = next_queue
            
        return root