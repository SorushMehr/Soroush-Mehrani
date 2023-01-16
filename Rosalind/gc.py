def fasta(file):
    alst = []
    blst = file.read().split('>')[1:]        
    for i in range(len(blst)):
        new = blst[i].split('\n', 1)
        id = new[0].replace('\n', '')
        seq = new[1].replace('\n', '')
        alst.append(id)
        alst.append(seq)        
    return (alst)

with open (r"C:\Users\slend\Downloads\rosalind_gc.txt", 'r') as f:
    blst = fasta(f)
    percent = []
    for i in range(len(blst)):
        if i%2 != 0:
            c = 0
            l = len(blst[i])
            for nucleotid in blst[i]:
                if nucleotid == 'C' or nucleotid == 'G':
                    c += 1
            p = (c/l)*100
            percent.append(p)
    print (blst[percent.index(max(percent))*2], max(percent), sep = '\n')
