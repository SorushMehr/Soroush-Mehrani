with open(r"C:\Users\slend\Downloads\rosalind_lcsm (1).txt", 'r') as f:
    dnastr = []
    lt = f.read().split('>')[1:] 
    
    for i in range(len(lt)):
        new = lt[i].split('\n', 1)
        seq = new[1].replace('\n', '')
        dnastr.append(seq)
def lcsm():
    lcs = ''
    ss = min(dnastr, key=len)
    
    for i in range(len(ss)):
        for j in range(i, len(ss)+1):
            pt = ss[i:j]
            if len(pt) > len(lcs) and all(pt in string for string in dnastr):
                lcs = pt
                
    print(lcs)
lcsm()
