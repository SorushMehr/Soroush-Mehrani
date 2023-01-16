def cons(dna):
    profile = []
    for i in range(len(dna[0])):
        A,C,T,G = 0, 0, 0, 0
        for j in range(len(dna)):
            if dna[j][i] == 'A':
                A += 1
            elif dna[j][i] == 'C':
                C += 1
            elif dna[j][i] == 'T':
                T += 1
            elif dna[j][i] == 'G':
                G += 1
        profile.append([[A,'A'],[C,'C'],[G,'G'],[T,'T']])

    cons = ''
    for row in profile:
        common = max(row)
        cons += common[1]
    print(cons)
    for i in range(4):
        record = profile[0][i][1] + ': '
        for j in range(len(profile)):
            record += str(profile[j][i][0]) + ' '
        print(record)



with open(r"C:\Users\slend\Downloads\rosalind_cons (1).txt",'r') as file:
    content = file.read()
dna_number, lines, line_number, dna = content.count('>'), content.splitlines(), 0, []
for i in range(dna_number):
    DNA = ''
    line_number += 1
    while lines[line_number][0] != '>':
        DNA += lines[line_number]
        line_number += 1
        if line_number+1 > len(lines):
            break
    dna.append(DNA)

cons(dna)
