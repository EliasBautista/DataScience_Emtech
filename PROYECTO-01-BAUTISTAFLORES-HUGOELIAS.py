"""
This is the LifeStore-SalesList data:

lifestore-sales = [id search, content search, date, hour (24:00)]
lifestore-searches = [id sale, id product, id user, score (from 1 to 10), returned (true or false)]
lifestore-products = [id product, name, description, category, on stock]
"""
from Listas import lifestore_products
from Listas import lifestore_sales
from Listas import lifestore_searches

# INICIO DEL LOGIN DE USUARIO #
users = {'Admin': 'root'}
status = ""
opcion = ""

while status != "q":
    print(" --------------------")
    print("|   LIFESTORE®      |")
    print(" --------------------")
    status = input("¿Estas Registrado? s/n (Ingresa q para salir): ")
    status = status.lower()
    if status == "s":
        login = input("Ingresa tu usuario: ")
        passw = input("Ingresa tu contraseña: ")
        #print(users)
        if login in users and users[login] == passw:
            print("\n====> Has iniciado sesión como ", login,"☺")
            print("--------------------------------------------")
            while opcion != "0":
                print()
                print("---------------------------MENU---------------------------------------------------")
                print("|  1.- Lista de los 50 Productos con Mayores Ventas                               |")
                print("|  2.- Lista de los 100 Productos con Mayores Busquedas                           |")
                print("|  3.- Lista de los 50 Productos con Menores Ventas (Agrupados por categoría)     |")
                print("|  4.- Lista de los 100 Productos con Menores Busquedas (Agrupados por categoría) |")
                print("|  5.- Lista de los Productos con Mejor Reseña (Unicamente con 5 de score)        |")
                print("|  6.- Lista de los Productos con Mejor Reseña (5 o 4 de Score)                   |")
                print("|  7.- Lista de los Productos con Peor Reseña (1 o 2 de Score)                    |")
                print("|  8.- Lista de los Productos con Peor Reseña (Unicamente con 1 de score)         |")
                print("|  9.- TOTAL DE INGRESOS, DINERO EN DEVOLUCIONES                                  |")
                print("|  10.- VENTAS POR MES Y PROMEDIO MENSUAL                                         |")
                print("|  11.- VENTAS QUE NO ESTAN DENTRO DEL AÑO 2020                                   |")
                print("|  12.- PRODUCTOS DEVUELTOS                                                       |")
                print("|  13.- LISTA DE PRODUCTOS CON MENORES VENTAS Y MAYOR STOCK                       |")
                print("|  14.- VALOR DEL INVENTARIO POR PRODUCTO                                         |")
                print("|  15.- VENTAS POR CATEGORIA                                                      |")
                print("|  16.- PRODUCTOS CON MENOR BUSQUEDA Y MAYOR STOCK                                |")
                print("|  0- Salir                                                                       |")
                print("----------------------------------------------------------------------------------")

                opcion=input("Selecciona una opcion...")
                if opcion == '1':
                    #INICIO LISTA 50 PRODUCTOS MAS VENDIDOS#
                    productos_venta = []
                    #Itero sobre los productos, por cada producto itero sobre las ventas y mediante un if identifico cuales son las coincidencias
                    for n in range(len(lifestore_products)):
                        y = [] #En esta lista iran los productos y sus respectivas ventas, reseteo su valor para que cada producto tenga su sublista con su nombre y sus respectivas ventas
                        x=0
                        id_p = lifestore_products[n][0]
                        name = lifestore_products[n][1]
                        stock = lifestore_products[n][4]
                        for j in range(len(lifestore_sales)):
                            if (lifestore_products[n][0] == lifestore_sales[j][1]) and (lifestore_sales[j][4] == 0): #Al añadir esta condicion no tomara en cuenta a los productos con devolucion
                                x+=1 #Al encontrar una coincidencia en el Id_Producto de ambas listas le suma uno a la variable x, al final tendra el valor de las veces que se vendio dicho producto
                        y.append(id_p)
                        y.append(name) #Añado el nombre del producto y = ["Nombre_Prod"]
                        y.append(x) #Añado el total de ventas del producto y = ["Nombre_Prod", no_Ventas]
                        y.append(stock) #Añado el stock y = ["Nombre_Prod", no_Ventas, Stock]
                        productos_venta.append(y) #Añado esa lista a otra lista, donde iran todos los productos y sus ventas

                    #productos_venta es la lista de listas que contiene el producto y cuantas ventas tiene [Producto, Ventas, Stock]
                    #print(productos_venta)
                    print("=====>NO SE INCLUYEN PRODUCTOS CON DEVOLUCION")
                    print("--ID--||-------------PRODUCTOS-------------------|| -----------------VENTAS---------------||------STOCK---")
                    #Utilizo el metodo bubble sort y le agrego el parametro reverse para ordenar la lista de mayor a menor, utilizando la segunda posicion de la sublista.
                    l = len(productos_venta)
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (productos_venta[j][2] < productos_venta[j + 1][2]):
                                tempo = productos_venta[j]
                                productos_venta[j]= productos_venta[j + 1]
                                productos_venta[j + 1]= tempo
                    for n in range(50):
                        print(n+1,".-", end=" ")
                        for j in range(len(productos_venta[n])):
                            print(productos_venta[n][j], end=" ")
                            print(" || ", end= ' ')
                        print()
                    #FIN DE LA LISTA#
                elif opcion == '2':
                    #INICIO LISTA 100 PRODUCTOS MAS BUSCADOS#
                    productos_busqueda = []

                    for n in range(len(lifestore_products)):
                        y = []
                        x=0
                        name = lifestore_products[n][1]
                        for j in range(len(lifestore_searches)):
                            if lifestore_products[n][0] == lifestore_searches[j][1]:
                                x+=1
                        y.append(lifestore_products[n][0])
                        y.append(name)
                        y.append(x)
                        productos_busqueda.append(y)
                    #productos_busqueda es la lista de listas que contiene el producto y cuantas busquedas tiene [Producto, Busquedas]
                    #print(productos_busqueda)
                    print("---ID---||-------------PRODUCTOS-------------------|| -------------BUSQUEDAS--------------------")
                    #Utilizo el metodo sort y le agrego el parametro reverse para ordenar la lista de mayor a menor, utilizando la segunda posicion de la sublista.
                    #productos_busqueda.sort(key=lambda x: x[2], reverse=True)
                    #Utilizamos el metodo sort para odrenar
                    l = len(productos_busqueda)
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (productos_busqueda[j][2] < productos_busqueda[j + 1][2]):
                                tempo = productos_busqueda[j]
                                productos_busqueda[j]= productos_busqueda[j + 1]
                                productos_busqueda[j + 1]= tempo

                    for n in range(len(productos_busqueda)):
                        print(n+1,".-", end=" ")
                        for j in range(len(productos_busqueda[n])):
                            print(productos_busqueda[n][j], end=" ")
                            print(" || ", end= ' ')
                        print()
                    #FIN LISTA 100 PRODUCTOS MAS BUSCADOS
                elif opcion == '3':
                    #LISTA 5O PRODUCTOS CON MENOS VENTAS, AGRUPADOS POR CATEGORIA#
                    productos_con_menorventa= []

                    #Mismo Procedimiento que las listas anteriores, solo que aqui añadiremos el valor categoria la lista y, para despues poder agruparla por categoria
                    for n in range(len(lifestore_products)):
                        y = []
                        x=0
                        name = lifestore_products[n][1] #Tomamos el nombre de la categoria del producto
                        category = lifestore_products[n][3]
                        for j in range(len(lifestore_sales)):
                            if (lifestore_products[n][0] == lifestore_sales[j][1]) and (lifestore_sales[j][4] == 0):
                                x+=1
                        y.append(name)
                        y.append(category) #Insertamos el nombre de la categoria, en la lista
                        y.append(x)
                        productos_con_menorventa.append(y) #La lista final que se añadira sera y = ["Producto", "Categoria", Ventas]

                    #productos_con_menorventa es la lista de listas que contiene el producto y cuantas busquedas tiene [Producto, Categoria, Ventas]
                    print("------------------PRODUCTOS------------------------------------------||---------------CATEGORIA-----------------------||-------------VENTAS--------------------")
                    #Utilizo el metodo sort, aqui utilizamos la segunda posicion que es donde estan las ventas
                    l = len(productos_con_menorventa)
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (productos_con_menorventa[j][1] != productos_con_menorventa[j + 1][1]):
                                tempo = productos_con_menorventa[j]
                                productos_con_menorventa[j]= productos_con_menorventa[j + 1]
                                productos_con_menorventa[j + 1]= tempo
                    #Despues de ordenar los productos mostrando primero los que tienen menores ventas, ordenamos por categoria y de esa forma agrupamos los datos por categoria
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (productos_con_menorventa[j][2] > productos_con_menorventa[j + 1][2]):
                                tempo = productos_con_menorventa[j]
                                productos_con_menorventa[j]= productos_con_menorventa[j + 1]
                                productos_con_menorventa[j + 1]= tempo

                    for n in range(len(productos_con_menorventa)):
                        print(n+1,".-", end=" ")
                        for j in range(len(productos_con_menorventa[n])):
                            print(productos_con_menorventa[n][j], end=" ")
                            print(" || ", end= ' ')
                        print()
                    #FIN LISTA 5O PRODUCTOS CON MENOS VENTAS, AGRUPADOS POR CATEGORIA#
                elif opcion == '4':
                    #LISTA 100 PRODUCTOS CON MENOS BUSQUEDAS, AGRUPADOS POR CATEGORIA#
                    productos_con_menorbusqueda= []
                    #Mismo Procedimiento que las listas anteriores, solo que aqui añadiremos el valor categoria la lista y, para despues poder agruparla por categoria
                    for n in range(len(lifestore_products)):
                        y = []
                        x=0
                        name = lifestore_products[n][1] #Tomamos el nombre de la categoria del producto
                        category = lifestore_products[n][3]
                        for j in range(len(lifestore_searches)):
                            if lifestore_products[n][0] == lifestore_searches[j][1]:
                                x+=1
                        y.append(name)
                        y.append(category) #Insertamos el nombre de la categoria, en la lista
                        y.append(x)
                        productos_con_menorbusqueda.append(y) #La lista final que se añadira sera y = ["Producto", "Categoria", Busqueda]
                    #productos_con_menorventa es la lista de listas que contiene el producto y cuantas busquedas tiene [Producto, Categoria, Busqueda]
                    print("------------------PRODUCTOS------------------------------------------||---------------CATEGORIA-----------------------||-------------BUSQUEDAS--------------------")
                    #Utilizo el metodo sort, aqui utilizamos la segunda posicion que es donde estan las busquedas
                    l = len(productos_con_menorbusqueda)
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (productos_con_menorbusqueda[j][2] < productos_con_menorbusqueda[j + 1][2]):
                                tempo = productos_con_menorbusqueda[j]
                                productos_con_menorbusqueda[j]= productos_con_menorbusqueda[j + 1]
                                productos_con_menorbusqueda[j + 1]= tempo
                    #Despues de ordenar los productos mostrando primero los que tienen menores ventas, ordenamos por categoria y de esa forma agrupamos los datos por categoria
                    l = len(productos_con_menorbusqueda)
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (productos_con_menorbusqueda[j][2] != productos_con_menorbusqueda[j + 1][2]):
                                tempo = productos_con_menorbusqueda[j]
                                productos_con_menorbusqueda[j]= productos_con_menorbusqueda[j + 1]
                                productos_con_menorbusqueda[j + 1]= tempo
                    for n in range(len(productos_con_menorbusqueda)):
                        print(n+1,".-", end=" ")
                        for j in range(len(productos_con_menorbusqueda[n])):
                            print(productos_con_menorbusqueda[n][j], end=" ")
                            print(" || ", end= ' ')
                        print()
                    #FIN LISTA 100 PRODUCTOS CON MENOS BUSQUEDAS, AGRUPADOS POR CATEGORIA#
                elif opcion == '5':
                    #PRODUCTOS CON MEJOR EVALUACION (SCORE = 5)#
                    productos_con_mejorevaluacion = []
                    for n in range(len(lifestore_products)):
                        y = []
                        x=0
                        name = lifestore_products[n][1]
                        for j in range(len(lifestore_sales)):
                            if (lifestore_products[n][0] == lifestore_sales[j][1]) and (lifestore_sales[j][2] == 5):
                                x+=1
                        if x > 0:
                            y.append(lifestore_products[n][0])
                            y.append(name)
                            y.append(x)
                            productos_con_mejorevaluacion.append(y)


                    print("---ID---||-------PRODUCTOS-------------------|| -------------VECES QUE A SIDO EVALUADO CON 5--------------------")
                    #Utilizo el metodo sort y le agrego el parametro reverse para ordenar la lista de mayor a menor, utilizando la segunda posicion de la sublista.
                    l = len(productos_con_mejorevaluacion)
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (productos_con_mejorevaluacion[j][2] < productos_con_mejorevaluacion[j + 1][2]):
                                tempo = productos_con_mejorevaluacion[j]
                                productos_con_mejorevaluacion[j]= productos_con_mejorevaluacion[j + 1]
                                productos_con_mejorevaluacion[j + 1]= tempo
                    for n in range(len(productos_con_mejorevaluacion)):
                        print(n+1,".-", end=" ")
                        for j in range(len(productos_con_mejorevaluacion[n])):
                            print(productos_con_mejorevaluacion[n][j], end=" ")
                            print(" || ", end= ' ')
                        print()
                    #FIN PRODUCTOS CON MEJOR EVALUACION (SCORE = 5)#
                elif opcion == '6':
                    #PRODUCTOS CON MEJOR EVALUACION (SCORE = 5 ó Score = 4, se toma en cuenta 5 y 4 de calificacion)#
                    productos_con_mejorevaluacion = []
                    for n in range(len(lifestore_products)):
                        y = []
                        x=0
                        name = lifestore_products[n][1]
                        for j in range(len(lifestore_sales)):
                            if (lifestore_products[n][0] == lifestore_sales[j][1]) and (lifestore_sales[j][2] == 5 or lifestore_sales[j][2] == 4):
                                x+=1
                        if x > 0:
                            y.append(lifestore_products[n][0])
                            y.append(name)
                            y.append(x)
                            productos_con_mejorevaluacion.append(y)


                    print("---ID---||-------PRODUCTOS-------------------|| -------------VECES QUE A SIDO EVALUADO CON 5, 4 --------------------")
                    #Utilizo el metodo sort y le agrego el parametro reverse para ordenar la lista de mayor a menor, utilizando la segunda posicion de la sublista.
                    l = len(productos_con_mejorevaluacion)
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (productos_con_mejorevaluacion[j][2] < productos_con_mejorevaluacion[j + 1][2]):
                                tempo = productos_con_mejorevaluacion[j]
                                productos_con_mejorevaluacion[j]= productos_con_mejorevaluacion[j + 1]
                                productos_con_mejorevaluacion[j + 1]= tempo
                    for n in range(len(productos_con_mejorevaluacion)):
                        print(n+1,".-", end=" ")
                        for j in range(len(productos_con_mejorevaluacion[n])):
                            print(productos_con_mejorevaluacion[n][j], end=" ")
                            print(" || ", end= ' ')
                        print()
                    #FIN PRODUCTOS MEJOR EVALUADOS#
                elif opcion == '7':
                    #PRODUCTOS CON MENOR EVALUACION (SCORE = 1 ó Score = 2, se toma en cuenta 1 y 2 de calificacion)#
                    productos_con_menorevaluacion = []
                    for n in range(len(lifestore_products)):
                        y = []
                        x=0
                        name = lifestore_products[n][1]
                        for j in range(len(lifestore_sales)):
                            if (lifestore_products[n][0] == lifestore_sales[j][1]) and (lifestore_sales[j][2] == 1 or lifestore_sales[j][2] == 2):
                                x+=1
                        if x > 0:
                            y.append(lifestore_products[n][0])
                            y.append(name)
                            y.append(x)
                            productos_con_menorevaluacion.append(y)


                    print("---ID---||-------PRODUCTOS-------------------|| -------------VECES QUE A SIDO EVALUADO CON 1, 2 --------------------")
                    #Utilizo el metodo sort y le agrego el parametro reverse para ordenar la lista de mayor a menor, utilizando la segunda posicion de la sublista.
                    l = len(productos_con_menorevaluacion)
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (productos_con_menorevaluacion[j][2] < productos_con_menorevaluacion[j + 1][2]):
                                tempo = productos_con_menorevaluacion[j]
                                productos_con_menorevaluacion[j]= productos_con_menorevaluacion[j + 1]
                                productos_con_menorevaluacion[j + 1]= tempo
                    for n in range(len(productos_con_menorevaluacion)):
                        print(n+1,".-", end=" ")
                        for j in range(len(productos_con_menorevaluacion[n])):
                            print(productos_con_menorevaluacion[n][j], end=" ")
                            print(" || ", end= ' ')
                        print()
                    #FIN#
                elif opcion == '8':
                    #PRODUCTOS CON MENOR EVALUACION (SCORE = 1)#
                    productos_con_menorevaluacion = []
                    for n in range(len(lifestore_products)):
                        y = []
                        x=0
                        name = lifestore_products[n][1]
                        for j in range(len(lifestore_sales)):
                            if (lifestore_products[n][0] == lifestore_sales[j][1]) and (lifestore_sales[j][2] == 1):
                                x+=1
                        if x > 0:
                            y.append(lifestore_products[n][0])
                            y.append(name)
                            y.append(x)
                            productos_con_menorevaluacion.append(y)


                    print("---ID---||-------PRODUCTOS-------------------|| -------------VECES QUE A SIDO EVALUADO CON 1 --------------------")
                    #Utilizo el metodo sort y le agrego el parametro reverse para ordenar la lista de mayor a menor, utilizando la segunda posicion de la sublista.
                    l = len(productos_con_menorevaluacion)
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (productos_con_menorevaluacion[j][2] < productos_con_menorevaluacion[j + 1][2]):
                                tempo = productos_con_menorevaluacion[j]
                                productos_con_menorevaluacion[j]= productos_con_menorevaluacion[j + 1]
                                productos_con_menorevaluacion[j + 1]= tempo
                    for n in range(len(productos_con_menorevaluacion)):
                        print(n+1,".-", end=" ")
                        for j in range(len(productos_con_menorevaluacion[n])):
                            print(productos_con_menorevaluacion[n][j], end=" ")
                            print(" || ", end= ' ')
                        print()
                    #FIN#
                elif opcion == '9':
                    #INICIO TOTAL DE INGRESOS Y DEVOLUCIONES#
                    ingresos = []
                    #Itero sobre los productos, por cada producto itero sobre las ventas y mediante un if identifico cuales son las coincidencias
                    for n in range(len(lifestore_products)):
                        y = [] #En esta lista iran los productos y sus respectivas ventas, reseteo su valor para que cada producto tenga su sublista con su nombre y sus respectivas ventas
                        x=0
                        id_p = lifestore_products[n][0]
                        name = lifestore_products[n][1]
                        price = lifestore_products[n][2]
                        for j in range(len(lifestore_sales)):
                            if (lifestore_products[n][0] == lifestore_sales[j][1]) and (lifestore_sales[j][4] == 0): #Al añadir esta condicion no tomara en cuenta a los productos con devolucion
                                x+=1 #Al encontrar una coincidencia en el Id_Producto de ambas listas le suma uno a la variable x, al final tendra el valor de las veces que se vendio dicho producto
                        y.append(id_p)
                        y.append(name) #Añado el nombre del producto y = ["Nombre_Prod"]
                        y.append(x) #Añado el total de ventas del producto y = ["Nombre_Prod", no_Ventas]
                        y.append(price * x) #Añado el ingreso del producto y = ["Nombre_Prod", no_Ventas, ingreso]
                        ingresos.append(y) #Añado esa lista a otra lista, donde iran todos los productos, ventas y ingreso

                    print("--ID---||-------------PRODUCTOS-------------------|| -----------------VENTAS------------------||---------INGRESOS--------")
                    #Utilizo el metodo sort y le agrego el parametro reverse para ordenar la lista de mayor a menor, utilizando la segunda posicion de la sublista.
                    l = len(ingresos)
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (ingresos[j][3] < ingresos[j + 1][3]):
                                tempo = ingresos[j]
                                ingresos[j]= ingresos[j + 1]
                                ingresos[j + 1]= tempo
                    for n in range(len(ingresos)):
                        print(n+1,".-", end=" ")
                        for j in range(len(ingresos[n])):
                            print(ingresos[n][j], end=" ")
                            print(" || ", end= ' ')
                        print()

                    #Sumamos los ingresos de cada prodcuto para sacar el total
                    total_ingresos = 0
                    for n in range(len(ingresos)):
                        total_ingresos+=ingresos[n][3]

                    print("--------------------------------------------------------------------------------------------------------------------")
                    print()
                    print("----TOTAL DE INGRESOS  ======> ", total_ingresos)
                    print()
                    print("--------------------------------------------------------------------------------------------------------------------")

                    ingresos_con_devolucion = []

                    #Itero sobre los productos, por cada producto itero sobre las ventas y mediante un if identifico cuales son las coincidencias
                    for n in range(len(lifestore_products)):
                        y = [] #En esta lista iran los productos y sus respectivas ventas, reseteo su valor para que cada producto tenga su sublista con su nombre y sus respectivas ventas
                        x=0
                        name = lifestore_products[n][1]
                        price = lifestore_products[n][2]
                        for j in range(len(lifestore_sales)):
                            if (lifestore_products[n][0] == lifestore_sales[j][1]): #Contando a los productos con devolucion
                                x+=1 #Al encontrar una coincidencia en el Id_Producto de ambas listas le suma uno a la variable x, al final tendra el valor de las veces que se vendio dicho producto
                        y.append(name) #Añado el nombre del producto y = ["Nombre_Prod"]
                        y.append(x) #Añado el total de ventas del producto y = ["Nombre_Prod", no_Ventas]
                        y.append(price * x) #Añado el ingreso del producto y = ["Nombre_Prod", no_Ventas, ingreso]
                        ingresos_con_devolucion.append(y) #Añado esa lista a otra lista, donde iran todos los productos, ventas y ingreso

                    #Suma de los ingresos contando las devoluciones
                    total_ingresos_con_devolucion = 0
                    for n in range(len(ingresos)):
                        total_ingresos_con_devolucion+=ingresos_con_devolucion[n][2]

                    print("--------------------------------------------------------------------------------------------------------------------")
                    print()
                    print("----DEVOLUCIONES  ======> ", total_ingresos_con_devolucion - total_ingresos)
                    print()
                    print("--------------------------------------------------------------------------------------------------------------------")
                    #FIN TOTAL DE INGRESOS Y DEVOLUCIONES#
                elif opcion == '10':
                    #VENTAS POR MES#
                    meses = [0,0,0,0,0,0,0,0,0,0,0,0]
                    meses_ventas = [0,0,0,0,0,0,0,0,0,0,0,0]
                    #Itero sobre las ventas, por cada venta itero sobre los productos y mediante un if identifico cuales son las coincidencias
                    for n in range(len(lifestore_sales)):
                        #y = [] #En esta lista iran los productos y sus respectivas ventas, reseteo su valor para que cada producto tenga su sublista con su nombre y sus respectivas ventas
                        x=0
                        date = lifestore_sales[n][3]
                        mes = date.split(sep='/')
                        for j in range(len(lifestore_products)):
                            if (lifestore_sales[n][1] == lifestore_products[j][0]) and (lifestore_sales[n][4] == 0):
                                if mes[1] == '01':
                                    meses_ventas[0]+=lifestore_products[j][2]
                                    meses[0]+=1
                                if mes[1] == '02':
                                    meses_ventas[1]+=lifestore_products[j][2]
                                    meses[1]+=1
                                if mes[1] == '03':
                                    meses_ventas[2]+=lifestore_products[j][2]
                                    meses[2]+=1
                                if mes[1] == '04':
                                    meses_ventas[3]+=lifestore_products[j][2]
                                    meses[3]+=1
                                if mes[1] == '05':
                                    meses_ventas[4]+=lifestore_products[j][2]
                                    meses[4]+=1
                                if mes[1] == '06':
                                    meses_ventas[5]+=lifestore_products[j][2]
                                    meses[5]+=1
                                if mes[1] == '07':
                                    meses_ventas[6]+=lifestore_products[j][2]
                                    meses[6]+=1
                                if mes[1] == '08':
                                    meses_ventas[7]+=lifestore_products[j][2]
                                    meses[7]+=1
                                if mes[1] == '09':
                                    meses_ventas[8]+=lifestore_products[j][2]
                                    meses[8]+=1
                                if mes[1] == '10':
                                    meses_ventas[9]+=lifestore_products[j][2]
                                    meses[9]+=1
                                if mes[1] == '11':
                                    meses_ventas[10]+=lifestore_products[j][2]
                                    meses[10]+=1
                                if mes[1] == '12':
                                    meses_ventas[11]+=lifestore_products[j][2]
                                    meses[11]+=1

                    print("--MES--||----NUMERO DE VENTAS---||--TOTAL INGRESOS POR MES--")
                    print()
                    print("Enero: ||", meses[0]," || $",meses_ventas[0])
                    print("Febrero: ||", meses[1]," || $",meses_ventas[1])
                    print("Marzo: ||", meses[2]," || $",meses_ventas[2])
                    print("Abril: ||", meses[3]," || $",meses_ventas[3])
                    print("Mayo: ||", meses[4]," || $",meses_ventas[4])
                    print("Junio: ||", meses[5]," || $",meses_ventas[5])
                    print("Julio: ||", meses[6]," || $",meses_ventas[6])
                    print("Agosto: ||",meses[7]," || $",meses_ventas[7])
                    print("Septiembre: ||", meses[8]," || $",meses_ventas[8])
                    print("Octubre: ||", meses[9]," || $",meses_ventas[9])
                    print("Noviembre: ||", meses[10]," || $",meses_ventas[10])
                    print("Diciembre: ||", meses[11]," || $",meses_ventas[11])
                    print()
                    print("------------------------------------------------------------------")
                    print("TOTALES: ",sum(meses)," || $",sum(meses_ventas)," ||")
                    print("------------------------------------------------------------------")
                    print("PROMEDIO MENSUAL: $", float((sum(meses_ventas)/12)))
                    print("------------------------------------------------------------------")
                    #FIN VENTAS POR MES#
                elif opcion == '11':
                    #FECHAS QUE NO ESTAN DENTRO DEL 2020#
                    x=0
                    print("Ventas Registradas en un año diferente al 2020")
                    for n in range(len(lifestore_sales)):
                        date = lifestore_sales[n][3]
                        año = date.split(sep='/')
                        for j in range(len(lifestore_products)):
                            if (lifestore_sales[n][1] == lifestore_products[j][0]):
                                if año[2] != '2020':
                                    print("Id_Venta: ",lifestore_sales[n][0], " Month: ",año[1], " Year: ",año[2])
                                    x+=lifestore_products[j][2]
                    print("Cantidad: ",x)
                    #FIN FECHAS#
                elif opcion == '12':
                    #PRODUCTOS CON DEVOLUCION
                    productos_devueltos = []
                    for n in range(len(lifestore_products)):
                        name = lifestore_products[n][1]
                        for j in range(len(lifestore_sales)):
                            if (lifestore_products[n][0] == lifestore_sales[j][1]) and (lifestore_sales[j][4] == 1):
                                y = []
                                y.append(lifestore_sales[j][1])#Id_Producto
                                y.append(name) #Nombre Producto
                                y.append(lifestore_sales[j][4]) #Devolucion
                                productos_devueltos.append(y)
                    print()
                    print("Cantidad de Productos devueltos: ", len(productos_devueltos))
                    print("-------------------ID-------------------|| -----------------PRODUCTO------------------||-------REFUND-----")
                    #Utilizo el metodo sort y le agrego el parametro reverse para ordenar la lista de mayor a menor, utilizando la segunda posicion de la sublista.
                    l = len(productos_devueltos)
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (productos_devueltos[j][1] < productos_devueltos[j + 1][1]):
                                tempo = productos_devueltos[j]
                                productos_devueltos[j]= productos_devueltos[j + 1]
                                productos_devueltos[j + 1]= tempo
                    for n in range(len(productos_devueltos)):
                        print(n+1,".-", end=" ")
                        for j in range(len(productos_devueltos[n])):
                            print(productos_devueltos[n][j], end=" ")
                            print(" || ", end= ' ')
                        print()
                    #FIN PRODUCTOS CON DEVOLUCION#
                elif opcion == '13':
                    productos_con_menorventa= []
                    #Mismo Procedimiento que las listas anteriores, solo que aqui añadiremos el valor categoria la lista y, para despues poder agruparla por categoria
                    for n in range(len(lifestore_products)):
                        y = []
                        x=0
                        id_p = lifestore_products[n][0]
                        name = lifestore_products[n][1] #Tomamos el nombre de la categoria del producto
                        category = lifestore_products[n][3]
                        stock = lifestore_products[n][4]
                        for j in range(len(lifestore_sales)):
                            if (lifestore_products[n][0] == lifestore_sales[j][1]) and (lifestore_sales[j][4] == 0):
                                x+=1
                        y.append(id_p)
                        y.append(name)
                        y.append(category) #Insertamos el nombre de la categoria, en la lista
                        y.append(x)
                        y.append(stock)
                        productos_con_menorventa.append(y) #La lista final que se añadira sera y = ["Producto", "Categoria", Ventas]

                    #productos_con_menorventa es la lista de listas que contiene el producto y cuantas busquedas tiene [Producto, Categoria, Ventas]
                    print("--ID--||-----------PRODUCTOS------------------------------------------||-------------CATEGORIA-------------||---------VENTAS---------||-------STOCK-------")
                    #Utilizo el metodo sort, aqui utilizamos la segunda posicion que es donde estan las ventas
                    l = len(productos_con_menorventa)
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (productos_con_menorventa[j][3] < productos_con_menorventa[j + 1][3]):
                                tempo = productos_con_menorventa[j]
                                productos_con_menorventa[j]= productos_con_menorventa[j + 1]
                                productos_con_menorventa[j + 1]= tempo
                    #Ordeno por stock(mayor a menor)
                    l = len(productos_con_menorventa)
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (productos_con_menorventa[j][4] < productos_con_menorventa[j + 1][4]):
                                tempo = productos_con_menorventa[j]
                                productos_con_menorventa[j]= productos_con_menorventa[j + 1]
                                productos_con_menorventa[j + 1]= tempo
                    for n in range(len(productos_con_menorventa)):
                        print(n+1,".-", end=" ")
                        for j in range(len(productos_con_menorventa[n])):
                            print(productos_con_menorventa[n][j], end=" ")
                            print(" || ", end= ' ')
                        print()
                    #FIN LISTA 5O PRODUCTOS CON MENOS VENTAS CON STOCK#
                elif opcion == '14':
                    #VALOR DEL INVENTARIO#
                    inventario = []
                    total_inv = 0
                    for n in range(len(lifestore_products)):
                        y = []
                        name = lifestore_products[n][1]
                        id_p = lifestore_products[n][0]
                        valor = lifestore_products[n][2] * lifestore_products[n][4]
                        y.append(id_p)
                        y.append(name)
                        y.append(valor)
                        inventario.append(y)

                    for n in range(len(inventario)):
                        total_inv+=inventario[n][2]

                    print()
                    print("--ID--||---PRODUCTO---------------------||----VALOR DEL INVENTARIO-----")
                    l = len(inventario)
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (inventario[j][2] < inventario[j + 1][2]):
                                tempo = inventario[j]
                                inventario[j]= inventario[j + 1]
                                inventario[j + 1]= tempo
                    for n in range(len(inventario)):
                        print(n+1,".-", end=" ")
                        for j in range(len(inventario[n])):
                            print(inventario[n][j], end=" ")
                            print(" || ", end= ' ')
                        print()

                    print("TOTAL ==> $", total_inv)
                    #FIN VALOR DEL INVENTARIO#
                elif opcion == '15':
                    #Categorias Ventas#
                    y = []
                    for n in range(len(lifestore_products)):
                        y.append(lifestore_products[n][3])

                    categorias = []
                    for x in y:
                        if x not in categorias:
                            categorias.append(x)
                    #print (categorias)

                    categoria_ventas = [0,0,0,0,0,0,0,0]
                    for n in range(len(lifestore_products)):
                        for k in range(len(lifestore_sales)):
                            if lifestore_products[n][0] == lifestore_sales[k][1]:
                                for j in range(len(categorias)):
                                    if lifestore_products[n][3] == categorias[j]:
                                        categoria_ventas[j]+=1

                    for n in range(len(categorias)):
                        print("Categoria: ",categorias[n], "|| Ventas: ",categoria_ventas[n])
                    #FIN CATEGORIAS VENTA#
                elif opcion == '16':
                    productos_con_menorbusqueda= []
                    #Mismo Procedimiento que las listas anteriores, solo que aqui añadiremos el valor categoria la lista y, para despues poder agruparla por categoria
                    for n in range(len(lifestore_products)):
                        y = []
                        x=0
                        name = lifestore_products[n][1] #Tomamos el nombre de la categoria del producto
                        stock = lifestore_products[n][4]
                        for j in range(len(lifestore_searches)):
                            if lifestore_products[n][0] == lifestore_searches[j][1]:
                                x+=1
                        y.append(lifestore_products[n][0])
                        y.append(name)
                        y.append(stock) #Insertamos el stock
                        y.append(x)
                        productos_con_menorbusqueda.append(y)

                    print("------ID----||------------PRODUCTOS-------------------------------||------------STOCK--------------------||---------BUSQUEDAS---------------")
                    #Utilizo el metodo sort, aqui utilizamos la segunda posicion que es donde esta el stock
                    l = len(productos_con_menorbusqueda)
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (productos_con_menorbusqueda[j][2] < productos_con_menorbusqueda[j + 1][2]):
                                tempo = productos_con_menorbusqueda[j]
                                productos_con_menorbusqueda[j]= productos_con_menorbusqueda[j + 1]
                                productos_con_menorbusqueda[j + 1]= tempo
                    #Despues de ordenar los productos mostrando primero los que tienen menores busquedas
                    for i in range(0, l):
                        for j in range(0, l-i-1):
                            if (productos_con_menorbusqueda[j][3] > productos_con_menorbusqueda[j + 1][3]):
                                tempo = productos_con_menorbusqueda[j]
                                productos_con_menorbusqueda[j]= productos_con_menorbusqueda[j + 1]
                                productos_con_menorbusqueda[j + 1]= tempo
                    for n in range(len(productos_con_menorbusqueda)):
                        print(n+1,".-", end=" ")
                        for j in range(len(productos_con_menorbusqueda[n])):
                            print(productos_con_menorbusqueda[n][j], end=" ")
                            print(" || ", end= ' ')
                        print()
                else:
                    print("INGRESA UNA OPCION VALIDA DEL MENU!!!")
        else:
            print("\nEl usuario no existe o la contraseña es erronea\n")
    elif status == "n":
        createLogin = input("Introduce un nombre de usuario: ")
        if createLogin in users:
            print("\nEse usuario ya existe!\n")
        else:
            createPassw = input("Introduce una contraseña: ")
            users[createLogin] = createPassw
            print("\nUsuario creado satisfactoriamente!\n")
