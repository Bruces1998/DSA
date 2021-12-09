def get_ans(string, n):
    ans = {}
    arr = []
    for i in range(n-1):
        for j in range(i+1, n):
            if (j-i+1>=(n//2)):
                ans[int(string[i:j+1], 2)] = (i+1, j+1)
                arr.append(int(string[i:j+1], 2))
    final_ans = []
    m = len(arr)
    for i in range(m-1):
        for j in range(i+1, m):
            if arr[j]!=0 and arr[i]%arr[j]==0:
                if ans[arr[i]][0]==ans[arr[j]][0] and ans[arr[i]][1] == ans[arr[j]][1]:
                    continue
                final_ans.append([ans[arr[i]], ans[arr[j]]])
            if arr[i]!=0 and arr[j]%arr[i]==0:
                if ans[arr[i]][0]==ans[arr[j]][0] and ans[arr[i]][1] == ans[arr[j]][1]:
                    continue
                final_ans.append([ans[arr[j]], ans[arr[i]]])
                
                
    print(final_ans[0][0][0], final_ans[0][0][1], final_ans[0][1][0], final_ans[0][1][1])
    
n = int(input())
inp = []
n_inp = []
for i in range(n):
    n_inp.append(int(input()))
    inp.append(input())
    
for i in range(n):
    get_ans(inp[i], n_inp[i])
