def revc():
    compl_DNA = ''
    string = reversed(str(DNA))
    for nucleotide in string:
        if nucleotide == 'G':
            compl_DNA += 'C'
        elif nucleotide == 'C':
            compl_DNA += 'G'
        elif nucleotide == 'T':
            compl_DNA += 'A'
        elif nucleotide == 'A':
            compl_DNA += 'T'
    print(compl_DNA)

with open(r"C:\Users\slend\Downloads\rosalind_revc.txt", 'r') as f:
    DNA = str(f.readline())
    
revc()
