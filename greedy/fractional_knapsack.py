from more_itertools import sort_together
def knapsack(n, w, values, weight):
    
    v_w = [(i/j) for i, j in zip(values, weight)]

    _, values, weight = sort_together([v_w, values, weight], reverse = True)
    print(values, weight)

    curr_weight = 0
    profit = 0
    i = 0
    while i < n:
        curr_weight += weight[i]
        if curr_weight > w:
            break
        profit += values[i]
        i += 1

    if i < n:
        print(curr_weight)
        curr_weight -= weight[i]
        print(w, curr_weight)
        profit += ((w - curr_weight)*values[i])/weight[i]
    return profit

print(knapsack(3, 50, [100, 60, 120], [20, 10, 30]))