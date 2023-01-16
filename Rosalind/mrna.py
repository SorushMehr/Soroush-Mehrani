
with open(r"C:\Users\slend\Downloads\rosalind_mrna.txt", 'r') as f:                         
    seq = f.read().replace('\n', '')

def mrna():
    # from the RNA CODON TABLE we see how many codons respond to
    # each amino acid, excluding the 3 stop codons
    codon = {
        'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1, 'P': 4, 'H': 2, 'Q': 2, 'R': 6,
        'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2, 'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4
    }
    
    p = 1

    for i in seq:
        p = (p * codon[i]) % 1000000 
    # Since there are 3 possible stop codons we have to multiply the result by 3
    # then we compute the modulo again
    numr = (p * 3) % 1000000  
    print(numr) 
mrna()
