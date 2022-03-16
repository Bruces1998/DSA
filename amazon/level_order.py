def level_order(root):
    queue = [root]
    ans = []

    while queue:
        next_queue = []
        local_ans = []
        while queue:
            curr_node = queue.pop(0)
            local_ans.append(curr_node.val)

            if curr_node.left:
                next_queue.append(curr_node.left)

            if curr_node.right:
                next_queue.append(curr_node.right)

        ans.append(local_ans)
        queue = next_queue

    return ans
