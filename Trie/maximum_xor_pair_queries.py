class TrieNode:
    def __init__(self):
        self.child = {}
        
    def increase(self, number):
        cur = self
        for i in range(31, -1, -1):
            bit = (number >> i) & 1
            if bit not in cur.child: cur.child[bit] = TrieNode()
            cur = cur.child[bit]
            
    def findMax(self, number):
        cur, ans = self, 0
        for i in range(31, -1, -1):
            bit = (number >> i) & 1
            if (1-bit) in cur.child:
                cur = cur.child[1 - bit]
                ans |= (1 << i)
            else:
                cur = cur.child[bit]
        return ans
    
class Solution:
    def findMaximumXORQueries(self, nums, queries):

        ans = [0]*len(queries)
        sorted_queries = []

        for i in range(len(queries)):
            sorted_queries.append(queries[i][1], (queries[0], i))

        sorted_queries.sort()

        trie = TrieNode()
        i = 0
        n = len(nums)

        for limit, (start, index) in sorted_queries:

            while i < n and nums[i] <= limit:
                trie.insert(nums[i])
                i += 1
            
            if i != 0:
                ans[index] = trie.findMax(start)

        return ans

