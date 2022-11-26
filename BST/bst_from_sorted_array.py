# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(arr, start, end):
    if start > end:
        return None
    
    i = (start+end)//2
    root = TreeNode(arr[i])
    
    root.left = inorder(arr, start, i-1)
    root.right = inorder(arr, i+1, end)
    
    return root

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums == []:
            return None
        
        return inorder(nums, 0, len(nums)-1)