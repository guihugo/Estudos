def selection (v):
    for i in range (0,len(v)-1):
        menor = v[i]
        for j in range (i+1,len(v)):
            if v[j] < menor:
                v[i] = v[j]
                v[j] = menor

    
    return v



print(selection([3,5,11,2,76]))