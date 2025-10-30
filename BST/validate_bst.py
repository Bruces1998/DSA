'''
Validate BST
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def validateBST(root):


    def isValidNode(node, low, high):
        if node == None:
            return True

        if not (low < node.val < high):
            return False

        return isValidNode(node.left, low, node.val) and isValidNode(node.right, node.val, high)



    return isValidNode(root, float("-inf"), float("inf"))


    