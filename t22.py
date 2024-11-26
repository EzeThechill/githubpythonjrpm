texto = """"    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. 
Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. 
Cuando contratamos nuevos empleados. Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. 
Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. 
Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil        """
a=texto.count("ython")
b=texto.lower().count("python")
print (a)
print (b)
c= texto.lower().find("python")
print (f"La primera posicion de la palabra Python es : {c}  ")
d=texto.lower().find("python", 48)
e= c + 52
print (f"La segunda posicion de la palabra Python es : {e} ")
if "código" in texto :
    print ("La palabra Codigo esta en el texto")
else :
    print ("La palabra Codigo no esta en el texto")
texto = texto.replace("Python", "PYTHON").replace("python", "PYTHON")
print (texto)
texto.swapcase()
#----------------------------------------------------------------------
texto = "Hola Todos"
ord("A") + 1
codificacion = []
for i in texto :
    codificacion.append(ord(i)+1)
print (codificacion)
for i in codificacion :
    codificacion.update(chr(i)-1)
print (codificacion)