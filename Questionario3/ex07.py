n1, n2, n3 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3) 
p1, p2, p3 = input().split()
p1 = int(p1)
p2 = int(p2)
p3 = int(p3)
prod1 = n1 * p1
prod2 = n2 * p2
prod3 = n3 * p3
soma_prod = prod1 + prod2 + prod3
soma_peso = p1 + p2 + p3 
media_pond = soma_prod / soma_peso
print(f'{media_pond:.6f}')