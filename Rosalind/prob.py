import math
def prob():
    with open(r"C:\Users\slend\Downloads\rosalind_prob.txt", 'r') as f:
        DNA = f.readline()
        for line in f:
            if line[0] != 'A' and line[0] != 'T' and line[0] != 'G' and line[0] != 'C':
                aaarray = line.split()
                GC_content = [float(x) for x in aaarray]
        A = DNA.count('A')
        C = DNA.count('C')
        G = DNA.count('G')
        T = DNA.count('T')
        AT = A + T
        GC = G + C

        barray = []
        for numb in range(len(GC_content)):
            prob1 = AT*(math.log10((1-GC_content[numb])/2)) + GC*(math.log10(GC_content[numb]/2))
            barray.append(prob1)
        print(*barray, sep=' ')
prob()
