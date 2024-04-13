def breed (a,b,l):
    l.append(0)
    id1 = []
    id2 = []
    id3 = []

    ps = [0,0,0]

    for i in range(a,b+1):
        id1.append(1 if l[i] == 1 else 0)
        id2.append(1 if l[i] == 2 else 0)
        id3.append(1 if l[i] == 3 else 0)

        
    ps[0] = len(id1)
    ps[1] = len(id2)
    ps[2] = len(id3)

    return id1,id2,id3

l = [2,1,1,3,2,1]

"""n = int(input(''))
q = int(input(''))

for i in range(n):
    x = int(input(''))
    l.append(x)
"""
[a,b] = input('').split(' ')

print (breed(int(a),int(b),l))