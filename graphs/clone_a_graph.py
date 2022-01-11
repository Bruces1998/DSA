from collections import defaultdict
class Node:
    def __init__(self, val = 0):
        self.val = val
        self.neighbors = []

def cloneGraph(node:None)-> Node:
    if node == None:
        return None

    queue = [node]
    mapp = {}

    while queue:
        curr_node = queue.pop(0)
        if mapp.get(curr_node.val) == None:
            mapp[curr_node.val] = Node(curr_node.val)

        copy_node = mapp[curr_node.val]

        for neighbor in curr_node.neighbors:
            if mapp.get(neighbor.val) is None:
                mapp[neighbor.val] = Node(neighbor.val)

            copy_node.neighbors.append(mapp[neighbor.val])
            queue.append(neighbor)

    return mapp[1]



