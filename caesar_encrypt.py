def caesar (n,s):
    lower = list('abcdefghijklmnopqrstuvwxyz')
    up = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    text = list(s)
    new = []
    for i in range(len(s)):
        if text[i] in lower:
            get = lower.index(text[i])
            get = (get + n) % 26  
            new.append(lower[get])
        elif text[i] in up:
            get = up.index(text[i])
            get = (get + n) % 26  
            new.append(up[get])
        else:
            new.append(text[i])
    
    string = ''.join(new)
    return string

print(caesar(2,'middle-Outz'))