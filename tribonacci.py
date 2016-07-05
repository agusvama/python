def tribonacci(a, n):
    suma = 0
    for i in range(n-3):
        lista = ultimos3(a)
        for j in lista:
           suma += j 
        a.append(suma)
        suma = 0
    return a

def ultimos3(a):
    con = 0
    last3 = []
    for i in range(len(a)-1, -1, -1):
        if(con < 3):
            last3.append(a[i])
            con = con + 1
    return last3
        
if __name__ == "__main__":
    print tribonacci([1, 1, 1], 1)
    
