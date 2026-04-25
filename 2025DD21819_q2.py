class matrix:
    def __init__(self, L):
        self.n = len(L)
        self.m = len(L[0])
        self.B = []
        for row in L:
            self.B.append(row.copy())

    def __add__(self, other):
        
        if self.n != other.n or self.m != other.m:
            print('Invalid')
            return matrix([[0]])  # or print("Invalid") and return
    
        temp = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                row.append(self.B[i][j] + other.B[i][j])
            temp.append(row)
        return matrix(temp)
    
    
    
    def __mul__(self, other):
        if self.m != other.n:
            print('Invalid')
            return matrix([[0]])
        
        temp = []
        for i in range(self.n):
            row = []
            for j in range(other.m):
                s = 0
                for k in range(self.m):
                    s += self.B[i][k] * other.B[k][j] 
                row.append(s)
            temp.append(row)
        
        return matrix(temp)

    
    
    def __eq__(self, other):
        if self.n != other.n or self.m != other.m:
            return False
        
        for i in range(self.n):
            for j in range(self.m):
                if (self.B[i][j] != other.B[i][j]):
                    return False
        return True
    

    def display(self):
        for i in range(self.n):
            for j in range(self.m):
                if (j < self.m-1): print(self.B[i][j], end=" ")
                else: print(self.B[i][j])

def read_and_return_nested_list(r, c):
    L = []
    for i in range(r):
        K = list(map(int,input().split()))
        if len(K) != c :
            print('Invalid')
            return matrix([[0]])
        L.append(K)
    return L

m1 = int(input())
n1 = int(input())
M1 = matrix(read_and_return_nested_list(m1, n1))

m2 = int(input())
n2 = int(input())
M2 = matrix(read_and_return_nested_list(m2, n2))

X = M1+M2
Y = M1*M2

X.display()
Y.display()
print(X==Y)
