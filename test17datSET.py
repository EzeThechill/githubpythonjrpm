par = set({2, 4, 6, 8, 10, 12, 14, 16})
print(type(par))

impar = {1, 3, 5, 7, 9, 11, 13}
print(type(impar))

print(1 in impar)

impar.add(11)
impar.add(11) # SET no Admite duplicados, pero no genera error
impar.discard(11)
impar.discard(11)

print(impar)

for i in impar :
    print (i)

x = (par|impar) # union de SETs
print (x)

x= par.union(impar)
print(x)

x = list (par) # Convertir un SET en lista /  x = set (correos) elimina duplicados

x = par - impar # 