asignatura = input("Ingrese nombre de la asignatura: ")

integrante = input("Ingrese el nombre de los integrante: ")

acl_num = input("Ingrese el número de ACL IPv4: ")

try:
    acl_num = int(acl_num)
except ValueError:
    print("El número ingresado no es válido.")
    exit()

if acl_num >= 1 and acl_num <= 99:
    print("La ACL", acl_num, "es una ACL Estándar.")
elif acl_num >= 100 and acl_num <= 199:
    print("La ACL", acl_num, "es una ACL Extendida.")
else:
    print("El número ingresado no corresponde a una lista de acceso IPv4.")