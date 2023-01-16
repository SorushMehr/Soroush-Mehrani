def subs(s, t):
    blank = []
    for i in range(len(s)):
        if s[i:].startswith(t):
            blank.append(i+1)
    return blank

with open(r"C:\Users\slend\Downloads\rosalind_subs.txt", 'r') as f:
    f = f.readlines()
    s = f[0].replace('\n', '')
    t = f[1].replace('\n', '')
    print(*subs(s, t))
