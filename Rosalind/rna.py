def dnarna(string):
    return string.replace('T','U')

if __name__ == "__main__":
    with open(r"C:\Users\slend\Downloads\rosalind_rna.txt", 'r') as f:
        string = f.readline().strip()
        rst = dnarna(string)
        print(rst)
