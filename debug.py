def findZigZagSequence(a):
    n = len(a)
    a.sort()
    mid= int(((n + 1)/2)-1)
    a[mid], a[n-1] = a[n-1], a[mid]

    for i in range(mid,n-1):
        st = i
        for j in range(1,mid):
            ed = n - j
            while(a[st] < a[ed]):
                a[st], a[ed] = a[ed], a[st]
                ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

findZigZagSequence([1,2,3,4,5,6,7]) ##Esperado 1,2,3,7,6,5,4