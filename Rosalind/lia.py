if __name__ == "__main__":
    with open(r"C:\Users\slend\Downloads\rosalind_lia.txt", "r") as f:
        k, n = [int(i) for i in f.readline().strip().split(" ")]

M = 2**k
sum_ = 0

def fact(n):
    if(n==1 or n==0) : return 1
    return n * fact(n-1)

def comb(n,m) :
    return fact(n)/fact(n-m)/fact(m)
        
for i in range(0,n) :
    sum_ += comb(M,i)*((0.25)**i)*((0.75)**(M-i))
    
print(1-sum_)
