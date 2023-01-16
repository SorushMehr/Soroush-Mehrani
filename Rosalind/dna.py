def count_DNA(string):
    countA = string.count("A")
    countC = string.count("C")
    countG = string.count("G")
    countT = string.count("T")
    return countA, countC, countG, countT

if __name__ == "__main__":
    with open(r"C:\Users\slend\Downloads\rosalind_dna (3).txt", 'r') as f:
        string = f.readline().strip()
        countA, countC, countG, countT = count_DNA(string)
        print(countA, countC, countG, countT)
