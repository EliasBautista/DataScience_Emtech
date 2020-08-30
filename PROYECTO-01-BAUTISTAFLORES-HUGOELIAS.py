"""
This is the LifeStore-SalesList data:

lifestore-sales = [id search, content search, date, hour (24:00)]
lifestore-searches = [id sale, id product, id user, score (from 1 to 10), returned (true or false)]
lifestore-products = [id product, name, description, category, on stock]
"""

#lifestore_sales = []
#lifestore_searches = []
#lifestore_products = []

# INICIO DEL LOGIN DE USUARIO #

UserList = []
PassList = []

print("Bienvenid@ a LifeStore\n")

ans = input("¿Tienes una cuenta? por favor ingresa s/n:")

if ans == 'n' or 'N':
    print("Registro de usuario")
    User = input("Ingresa un nombre de usuario: ")
    UserList.append(User)
    Pass = input("Ingresa una contraseña: ")
    PassList.append(Pass)
    print("Usuario registrado! ", UserList, PassList)
    print("Has creado una nueva cuenta en LifeStore, ya puedes ingresar\n")
    User1 = input("Usuario: ")
    Pass1 = input("Contraseña: ")
    if User1 == (UserList) and Pass1 == (PassList):
        print("---MENU---")

    else:
        print("Usuario o contraseña invalidos, intente de nuevo...")