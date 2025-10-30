# def minCoinsGreedy(coins, V):
#     coins.sort()
#     ans = 0

#     for i in range(len(coins)-1, -1, -1):

#         while V >= coins[i]:
#             V -= coins[i]
#             ans += 1


#     return ans

# print(minCoinsGreedy([1, 2, 3], 4))

# import heapq
# def getMinimumBoxes(boxes, capacity):

#     min_Heap = heapq.heapify(boxes)
#     ans = 0

#     while not min_Heap[-1] <= capacity* min_Heap[0]:
#         ans += 1
#         heapq.heappop(min_Heap)

#     return ans

def manageCart(cart, queries):

    mapp = {}

    for i in range(len(cart)):
        if mapp.get(cart[i]) is None:
            mapp[cart[i]] = [i]
        else:
            mapp[cart[i]].append(i)

    
    for query in queries:
        print(mapp, cart)
        if query < 0:
            cart[mapp[-query].pop(0)] = "X"
        
        else:
            cart.append(query)

            if mapp.get(query) is None:
                mapp[query] = [len(cart) - 1]

            else:
                mapp[query].append(len(cart) - 1)

    print(mapp)
    return [i for i in cart if i != "X"]

cart = [2, 3, 2]
queries = [2, -2, -2]
print(manageCart(cart, queries))