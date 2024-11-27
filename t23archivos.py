f= open("abc.txt","r")
print(f.encoding)
print(f.name)
print(f.closed)

#leerlo readline
s = f.readline()  # lee linea a linea 1º lineas del archivo Hola mundo
print(s)
s = f.readline() # lee linea a linea 2º lineas del archivo que tal estas
print(s)

# leerlo readlines
for i in f.readlines():
    print(i)



f.close()