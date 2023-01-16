def calculate(l):
    offspring = (1*l[0] + 1*l[1] + 1*l[2] + 0.75*l[3] + 0.5*l[4] + 0*l[5]) * 2
    return offspring 

if __name__ == "__main__":
    with open(r"C:\Users\slend\Downloads\rosalind_iev (1).txt", "r") as f:
        l = [float(i) for i in f.readline().strip().split(" ")]
    print(calculate(l))
