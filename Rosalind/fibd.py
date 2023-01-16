with open(r"C:\Users\slend\Downloads\rosalind_fibd.txt", 'r') as f:
    f = f.readline().split(' ')
    n = int(f[0])
    m = int(f[1])
def fibd(n, m):
    G = [1, 1, 1]
    for i in range(3, n + 1):
        G.append(G[i-1] + G[i-2])
        if i > m:
            G[i] -= G[i - m - 1]
    print(G[n])
fibd(n, m)
