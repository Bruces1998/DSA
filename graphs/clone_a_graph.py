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
        
        if mapp.get(curr_node.val) is None:
            mapp[curr_node.val] = [Node(curr_node), 0]

        if mapp[curr_node.val][1] == 1:
            continue

        mapp[curr_node.val][1] = 1
        copy_node = mapp[curr_node.val][0]

        for neighbor in curr_node.neighbors:
            if mapp.get(neighbor.val) is None:
                mapp[neighbor.val] = [Node(neighbor.val), 0]

            copy_node.neighbors.append(mapp[neighbor.val][0])
            queue.append(neighbor)

    return mapp[1][0]

