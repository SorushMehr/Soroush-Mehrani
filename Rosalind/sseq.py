def sseq(data, motif):
    position, indices = -1, ''
    for nucleotide in motif:
        position = data.find(nucleotide, position+1)
        indices += str(position+1) + ' '
    print(indices)


with open(r"C:\Users\slend\Downloads\rosalind_sseq.txt", 'r') as f:
    g = f.read()
DNAs_number, lines, line_number, DNAs = g.count('>'), g.splitlines(), 0, []
for i in range(DNAs_number):
    DNA = ''
    line_number += 1
    while lines[line_number][0] != '>':
        DNA += lines[line_number]
        line_number += 1
        if line_number+1 > len(lines):
            break
    DNAs.append(DNA)

sseq(DNAs[0], DNAs[1])
