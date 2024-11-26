import a_limpia_ter
import json

accion = '{"nombre": "Repsol", "precio":5}'
print(type(accion))

a= json.loads(accion) # pasa de string a diccionario

b= json.dumps({"nombre":"hola"}) # pasa de diccionario a string