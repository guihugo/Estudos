def flipping_matrix(m): 
    sum = 0
    n = len(m)

    for i in range(0, n//2):
        for j in range(0, n//2):
            sum += max(m[i][j], m[i][n-j-1], m[n-1-i][j], m[n-1-i][n-1-j])    
    
    return sum

print(flipping_matrix([[4,2],[1,3]]))