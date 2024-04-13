def diagonal(arr):
    sum_1 = 0
    sum_2 = 0
    n = len(arr)
    for i in range(0,len(arr)):
        sum_1+=arr[i][i]
        sum_2+=arr[i][n-i-1]
            
    x = sum
    return sum_1,sum_2
print(diagonal([[11,2,4],[4,5,6],[10,8,-12]]))