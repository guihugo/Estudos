def lonely(a):
    for i in a:
        if a.count(i) == 1:
            result = i
    return result
print(lonely([1,2,3,4,3,2,1])) #Esperado 4