from os import system

output = ""
file_name="empleados.csv"
with open (file_name, "r") as f:
    f.readline()
    print(f)
    for i in f.readlines():
        empleado =i.split (",")
        output = output + "NAME:" + empleado[1]
        output = output + "EMAIL:" + empleado [3] + "@NAZARET.COM"
        output = output + "\n"
        print(output)
output_file = "empleados_out.txt"
with open(output_file, "w") as f:
    f.write(output) 
