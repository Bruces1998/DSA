def find_order(number_of_courses, prereq):
    if number_of_courses == 1:
        return [0]

    graph = [[] for _ in range(number_of_courses)]
    inorder = [0] * number_of_courses

    for dest, src in prereq:
        inorder[dest] +=1
        graph[src].append(dest)
    
    queue = []

    for i in range(number_of_courses):
        if inorder[i] == 0:
            queue.append(i)
    
    top_order = []
    while queue:
        curr = queue.pop()
        top_order.append(curr)

        for neigh in graph[curr]:
            inorder[neigh] -= 1
            if inorder[neigh] == 0:
                queue.append(neigh)
    
    if len(top_order) == number_of_courses:
        return top_order
    
    return []