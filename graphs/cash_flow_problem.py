N = 3

def getMin(arr):
    minInd = 0
    for i in range(1, N):
        if(arr[i] < arr[minInd]):
            minInd = i

    return minInd

def getMax(arr):
    maxInd = 0
    for i in range(1, N):
        if(arr[i] > arr[maxInd]):
            maxInd = i

    return maxInd

def minCashFlowRec(amount):
    mxCredit = getMax(amount)
    mxDebit = getMin(amount)

    if (amount[mxCredit] == 0 and amount[mxDebit] == 0):
        return 0


    minn = min(-amount[mxDebit], amount[mxCredit])
    amount[mxCredit] -= minn
    amount[mxDebit] += minn

    print("Person " , mxDebit , " pays " , minn
        , " to " , "Person " , mxCredit)


    minCashFlowRec(amount)

def minCashFlow(graph):

    amount = [0 for i in range(N)]

    for p in range(N):
        for i in range(N):
            amount[p] += (graph[i][p] - graph[p][i])
    print(amount)
    minCashFlowRec(amount)


graph = [ [0, 1000, 2000],
          [0, 0, 5000],
          [0, 0, 0] ]

print(minCashFlow(graph))