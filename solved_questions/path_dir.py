class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        L = A.split(sep="/")
        stack = []
        i=0
        print(L)
        while(i<len(L)):
            while(L[i]==" "):
                i+=1
            if(L[i].isalpha()):
                stack.append(L[i])

            if(L[i]==".."):
                if(stack):
                    stack.pop()
            i+=1
        print(stack)
        if(len(stack)==0):
            return("/")
        else:
            res=""
            for i in stack:
                res+="/"+i
            return(res)


sol = Solution()
sol.simplifyPath("/a/./b/../../c/")
