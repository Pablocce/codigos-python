import getpass
p=getpass.getpass("Introduzca password:")
pConfirmada = ""
while p != pConfirmada:
    pConfirmada = getpass.getpass("Confirme la contraseña:")
