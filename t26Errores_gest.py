def division(x,y):
    if y==0:
        raise ZeroDivisionError("No se puede dividir por cero !!!")
    return x/y
    
try :
    x=division(10,0)
except ZeroDivisionError as error:
    print(error)
#