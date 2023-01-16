def IPRB():
    pop = k + m + n

    i = [k*m*1, m*k*1, k*n*1, n*k*1, m*n*0.5, n*m*0.5, k*(k-1)*1, m*(m-1)*0.75, 0*n*(n-1)]

    probability = sum(i)/pop/(pop-1)
    print(probability)

with open(r"C:\Users\slend\Downloads\rosalind_iprb.txt", 'r') as f:
    k, m, n = f.read().split(' ')
    k, m, n = int(k), int(m), int(n)
    
IPRB()
