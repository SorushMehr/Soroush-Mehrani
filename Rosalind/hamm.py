def ham(str1, str2):
    distance = 0
    assert len(str1) == len(str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance

if __name__ == "__main__":
    with open(r"C:\Users\slend\Downloads\rosalind_hamm (1).txt", "r") as f:
        str1 = f.readline().strip()
        str2 = f.readline().strip()
    print(ham(str1, str2))
