with open(r"C:\Users\slend\Downloads\rosalind_splc.txt", "r") as f:
    I = f.read().split()
seqs = ['']*100


itr = -1
for value in I:
    if '>' in value: itr+=1 
    else: seqs[itr]+=value
        
main_strand = seqs[0]
introns = seqs[1:]

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


for intron in introns :
    main_strand = main_strand.replace(intron,'')


splc = ''
for i in range(0,len(main_strand),3):
    if(codon_dict[main_strand[i:i+3]] == 'Stop') : break
    splc += codon_dict[main_strand[i:i+3]]
    
print(splc)
