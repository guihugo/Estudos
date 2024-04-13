def gridChallenge(grid):
    new = []
    for i in range(len(grid)):
        temp = []
        for j in range(len(grid[0])):
            temp_1= ord(grid[i][j])
            temp.append(temp_1) 
            temp.sort()
        new.append(temp)

    for row in range(len(new)):
        for line in range(1,len(new[0])):
            if new[row][line] < new[row-1][line]:
                return 'NO'
    
    return 'YES'


print(gridChallenge(['eabcd','fghij''olkmn','trpqs','xywuv']))