from heapq import heappush, heappop
def merge_k_sorted(arr):
    dummy = Node(None)
    heap = []
    for ll in arr:
        if ll:
            heap.heappush((ll.val, ll))

    while heap:
        curr.next = heap.heappop()[1]
        curr = curr.next
        if curr.next:
            heappush(heap, (curr.next.val, curr.next))


    return dummy.next