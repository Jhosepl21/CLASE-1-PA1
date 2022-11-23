n = int(input("Ingrese el tamaño del arreglo:"))
m = int(input("Ingrese un numero para su multiplo:"))
A = []
for i in range (1,n+1):
 A.append(i*m)
print (A)