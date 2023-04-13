print("Evaluación N°1")
asignatura = input("Por favor, ingrese el nombre de la asignatura: ")
cant_integrantes = int(input("Ingrese la cantidad de integrantes en el grupo: "))

integrantes = []

for i in range(cant_integrantes):
    nombre = input("Ingrese el nombre del integrante {}: ".format(i+1))
    integrantes.append(nombre)

print("La asignatura es: ", asignatura)
print("La cantidad de integrantes es: ", cant_integrantes)
print("Los integrantes son: ")
for integrante in integrantes:
    print("-", integrante)
    