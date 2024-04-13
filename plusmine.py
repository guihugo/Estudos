def plusMinus(arr):
    # Write your code here
    size = len(arr)
    positivo = []
    negativo = []
    zero = []
    
    
    for i in range(0,size):
        if arr[i] > 0:
            positivo.append(arr[i])
        
        elif arr[i] == 0:
            zero.append(arr[i])
            
        elif arr[i] < 0:
            negativo.append(arr[i])
            
    pos = len(positivo)/size
    neg = len(negativo)/size
    none = len(zero)/size

    print("{:.6f}".format(pos))
    print("{:.6f}".format(neg))
    print("{:.6f}".format(none))

plusMinus([1,2,3,-1,-2,-3,0,0])