class Node:
    def __init__(self,val):
        self.value = val
        self.next = None
        self.bottom = None


def flatten(root):
    if root == None or root.next == None:
        return root
    root.next = flatten(root.next)
    root = mergeLists(root, root.next)

    return root


def mergeLists(nodeA, nodeB):
    temp = Node(0)
    result = temp

    while nodeA != None or nodeB != None:
        if nodeA.val < nodeB.val:
            temp.bottom = nodeA
            temp = temp.bottom
            nodeA = nodeA.bottom
        else:
            temp.bottom = nodeB
            temp = temp.bottom
            nodeB = nodeB.bottom

    if nodeA == None:
        temp.bottom = nodeB

    else:
        temp.bottom = nodeA

    return result.bottom 