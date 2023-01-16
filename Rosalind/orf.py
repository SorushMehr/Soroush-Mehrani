with open(r"C:\Users\slend\Downloads\rosalind_orf (1).txt", "r") as f:
    I = f.read().split()
seq=''
complements = str.maketrans('ATGC','TACG')


for value in I:
    if '>' not in value: seq+=value


comp=seq.translate(complements)
rev_comp=''.join(reversed(comp))

frames = set()
ATGs = [[] for _ in range(6)]
codon = """TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA Stop   CAA Q      AAA K      GAA E
TAG Stop   CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA Stop   CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G """.split()
codon_dict = dict(zip(codon[::2],codon[1::2]))
targets = seq, seq[1:], seq[2:], rev_comp, rev_comp[1:], rev_comp[2:]


for idx, frame in enumerate(targets) :
    for i in range(len(frame)-2):
        triplet = ''
        if(i%3==0) :
            triplet = frame[i] + frame[i+1] + frame[i+2]
            if(codon_dict[triplet] == 'M'):
                ATGs[idx].append(i)
                

for idx, frame in enumerate(targets) :
    for start in ATGs[idx] :
        PROT = ''
        for i in range(len(frame[start:])-2) :
            triplet = ''
            if(i%3==0) :
                triplet = frame[start+i] + frame[start+i+1] + frame[start+i+2]
                
                
                if(codon_dict[triplet] == 'Stop'):
                    frames.add(PROT)
                    break
                
                PROT+=codon_dict[triplet]

for i in frames:
    print(i)
