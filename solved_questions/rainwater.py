class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        stack = []
        water = 0
        for i in range(len(A)):
            print(stack)
            while (stack!=[] and A[stack[-1]] < A[i]):

                top = stack[-1]
                stack.pop(-1)

                if stack!=[]:
                    distance = i- stack[-1] - 1
                    height=min(A[i],A[stack[-1]])-A[top];
                    water+=distance*height;

            stack.append(i)


        return water



sol = Solution()
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
