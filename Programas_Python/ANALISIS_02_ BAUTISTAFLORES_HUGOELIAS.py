#!/usr/bin/env python
# coding: utf-8

# # PROYECTO 02
# 
# Autor: Hugo Elias Bautista Flores
# #### Correo: elias.bautistaflores@outlook.com

# In[1]:


#Librerias
import pandas as pd
#import numpy as np
#import os
#import collections


# In[2]:


#Leer el archivo csv con pandas (el archivo esta en la misma carpeta)
data = pd.read_csv("synergy_logistics_database.csv")


# In[3]:


#Comprobamos que se haya cargado correctamente
data.head(5)


# In[4]:


#Revisamos el numero de filas y columnas del df
data.shape


# ## Análisis Preliminar

# In[5]:


#Obtenemos una lista de todos los paises que aparecen en la columna origen
pais_orig = pd.unique(data["origin"]).tolist()
print("Lista paises origen:")
print(pais_orig)


# In[6]:


#Obtenemos una lista de todos los paises que aparecen en la columna destino
pais_dest = pd.unique(data["destination"]).tolist()
print("Lista paises destino:")
print(pais_dest)


# In[7]:


#Una lista de todos los medios de transporte que aparecen en la columna transport_mode
transportes = pd.unique(data["transport_mode"]).tolist()
print("Lista transportes:")
print(transportes)


# In[8]:


#Pruebas de condiciones al df
data[(data["direction"]=="Exports") & (data["origin"]=="France") & (data["destination"]=="Austria")]


# In[9]:


#Hay valores 0 en la columna total_value
data_valor_cero = data[data["total_value"]==0]
data_valor_cero.head()


# In[10]:


#Crear dataframe sin las filas que tengan 0 en la columna total_value
df_withNoZeroValues = data
df_withNoZeroValues = df_withNoZeroValues.drop(df_withNoZeroValues[df_withNoZeroValues["total_value"] == 0].index, axis=0)
df_withNoZeroValues.shape


# In[11]:


#Numero de filas con 0 en la columna total_value
data.shape[0] - df_withNoZeroValues.shape[0]


# # CONSIGNAS
# ## Opción 1

# In[12]:


#Funcion que devuelve un diccionario con la ruta y las veces que se utilizo dado como parametros la actividad("Exports", "Imports")
                    #Y como segundo parametro el dataframe con el que trabajara(el completo o el que no tiene ceros)
def rutaOperaciones(actividad, df):
    numeroOp = []
    ruta = []
    for pais_o in pais_orig: #Por cada pais de origen se itera sobre un pais de destino
        for pais_d in pais_dest:
            if (df[(df["direction"]==actividad) & (df["origin"]==pais_o) & (df["destination"]==pais_d)].shape[0]) == 0: 
                continue #Si en esa ruta no hay operaciones continua con el ciclo y no lo agrega a la lista
            else:
                numeroOp.append(df[(df["direction"]==actividad) & (df["origin"]==pais_o) & (df["destination"]==pais_d)].shape[0])#Toma el numero de filas que cumplen con la condicion
                ruta.append(pais_o+"-"+pais_d) #La ruta pais de origen - pais de destino
    demanda = dict(zip(ruta,numeroOp))
    return demanda


# In[13]:


#Funcion para convertir de diccionario a DF, primer parametro el diccionario, segundo parametro los nombres de las columnas
def dictToDf(dic, col):
    df = pd.DataFrame([[key, dic[key]] for key in dic.keys()], columns=col)
    
    return df


# In[14]:


#Funcion para calcular el valor total de la ruta
#Funcion casi identica a la de rutaOperaciones
def rutaCosto(actividad, df):
    costo = []
    ruta = []
    for pais_o in pais_orig:
        for pais_d in pais_dest:
            if (df[(df["direction"]==actividad) & (df["origin"]==pais_o) & (df["destination"]==pais_d)].shape[0]) == 0:
                continue
            else:
                costo.append(df.loc[(df["direction"]==actividad) & (df["origin"]==pais_o) & (df["destination"]==pais_d), 'total_value'].sum())#Suma las filas en la columna total_value que cumplan con la condicion
                ruta.append(pais_o+"-"+pais_d)
    costo_d = dict(zip(ruta, costo))
    return costo_d


# In[15]:


#Ordena un diccionario por sus valores, de mayor a menor
def ordenarDic(dic):
    return dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))


# In[16]:


#Une dos dataframes mediante el metodo Outer join, parametros(primer dataframe, segundo dataframe, nombre de la columna que hara la union)
def outerJoin(tabla1, tabla2, columna):
    tabla = pd.merge(left = tabla1, right=tabla2,
                       how = "outer", left_on = columna, right_on=columna)
    return tabla


# In[17]:


#Le da formato de dinero a una columna dado como parametros el dataframe y el nombre de la columna
def formatoDinero(df, columna):
    df[columna] = (df[columna]).apply(lambda x: "${:0,.2f}".format(x))


# In[18]:


#Usamos las funciones creadas para generar 2 diccionaros con el No. de Exportaciones e Importaciones por ruta
dicEx1 = ordenarDic(rutaOperaciones("Exports",data))
dicIm1 = ordenarDic(rutaOperaciones("Imports",data))

#Generamos 2 diccionarios con los costos de las operaciones por ruta
dicEx2 = ordenarDic(rutaCosto("Exports",data))
dicIm2 = ordenarDic(rutaCosto("Imports",data))

#Los convertimos a dataframes
dEx1 = dictToDf(dicEx1,["Ruta","No. Operaciones"])
dIm1 = dictToDf(dicIm1,["Ruta","No. Operaciones"])
dEx2 = dictToDf(dicEx2,["Ruta","Costo de Operaciones"])
dIm2 = dictToDf(dicIm2,["Ruta","Costo de Operaciones"])

#Unimos los dataframes para tener uno de exportaciones y uno de importaciones
exportaciones = outerJoin(dEx1,dEx2,"Ruta")
importaciones = outerJoin(dIm1,dIm2,"Ruta")


# In[19]:


#Exactamente el mismo procedimiento pero aqui se utilizara el dataframe sin valores 0 en la columna total_values

#Usamos las funciones creadas para generar 2 diccionaros con el No. de Exportaciones e Importaciones por ruta
dicEx1_z = ordenarDic(rutaOperaciones("Exports",df_withNoZeroValues))
dicIm1_z = ordenarDic(rutaOperaciones("Imports",df_withNoZeroValues))

#Generamos 2 diccionarios con los costos de las operaciones por ruta
dicEx2_z = ordenarDic(rutaCosto("Exports",df_withNoZeroValues))
dicIm2_z = ordenarDic(rutaCosto("Imports",df_withNoZeroValues))

#Los convertimos a dataframes
dEx1_z = dictToDf(dicEx1_z,["Ruta","No. Operaciones"])
dIm1_z = dictToDf(dicIm1_z,["Ruta","No. Operaciones"])
dEx2_z = dictToDf(dicEx2_z,["Ruta","Costo de Operaciones"])
dIm2_z = dictToDf(dicIm2_z,["Ruta","Costo de Operaciones"])

#Unimos los dataframes para tener uno de exportaciones y uno de importaciones
exportaciones_z = outerJoin(dEx1_z,dEx2_z,"Ruta")
importaciones_z = outerJoin(dIm1_z,dIm2_z,"Ruta")


# In[20]:


#Este frame no contempla a las filas donde total_value es igual a 0
#dataframes con terminacion "_z"
exportaciones_z.head(10)


# In[22]:


#Suma del valor de las rutas de exportacion mas demandadas
totalRutEx = exportaciones_z.iloc[:10,[2]].sum()
print("Total rutas de Importacion más demandadas(Sin contar datos 0 en total_value) -> $",format(int(totalRutEx),',d'))


# In[24]:


importaciones_z.head(10)


# In[23]:


#Suma del valor de las rutas de importacion mas demandadas
totalRutIm = importaciones_z.iloc[:10,[2]].sum()
print("Total rutas de Importacion más demandadas(Sin contar datos 0 en total_value) -> $",format(int(totalRutIm),',d'))


# In[25]:


#Suma del valor de las rutas de importacion y exportacion mas demandadas
t_total = totalRutIm + totalRutEx
print("Total Rutas Importacion y Exportacion más demandadas(Sin contar datos 0 en total_value) -> $",format(int(t_total),',d'))


# In[26]:


#Este frame contempla todo el csv original
importaciones.head(10)


# In[27]:


#Suma del valor de las rutas de importacion mas demandadas
totalRutIm2 = importaciones.iloc[:10,[2]].sum()
print("Total rutas de Importacion más demandadas -> $",format(int(totalRutIm2),',d'))


# In[28]:


exportaciones.head(10)


# In[29]:


#Suma del valor de las rutas de exportacion mas demandadas
totalRutEx2 = exportaciones.iloc[:10,[2]].sum()
print("Total rutas de Exportacion más demandadas -> $",format(int(totalRutEx2),',d'))


# In[30]:


#Suma del valor de las rutas de importacion y exportacion mas demandadas
t_total2 = totalRutIm2 + totalRutEx2
print("Total Rutas Importacion y Exportacion más demandadas(Contando 0 en total_value) -> $",format(int(t_total2),',d'))


# In[31]:


#Las 5 rutas de Importacion con mayor valor
imports = importaciones.sort_values('Costo de Operaciones', ascending=False)
imports.head(5)


# In[32]:


#Las 5 rutas de exportacion con mayor valor
export = exportaciones.sort_values('Costo de Operaciones', ascending=False)
export.head(5)


# ## Opción 2

# In[33]:


#Agrupar por transporte y sumar la columna total value
data.groupby(["transport_mode"])['total_value'].sum().reset_index()


# In[34]:


#Transportes registrados para el df con ceros en la columna total_value
data_valor_cero['transport_mode'].value_counts()


# In[35]:


#Metodos de transporte en todo el dataframe
data['transport_mode'].value_counts()


# In[36]:


#Metodos de transporte en el dataframe sin ceros en la columna total_value
df_withNoZeroValues['transport_mode'].value_counts()


# In[37]:


#Agrupar por medio de transporte y sumar su valor
transportes = data.groupby(["transport_mode"])['total_value'].sum().reset_index()
#Darle formato de dinero al valor
#formatoDinero(transportes, "total_value")
transportes


# In[38]:


#Suma del valor de los transportes
totalTrans = transportes.iloc[[0,1,3],[1]].sum()
print("Suma del valor de los 3 principales metodos de transporte(Sin el metodo Road) -> $",format(int(totalTrans),',d'))


# In[39]:


#Crear un diccionario con las veces que se utilizo cada medio de transporte en una ruta
trans = dict(data['transport_mode'].value_counts())


# In[40]:


transportes2= dictToDf(trans,["transport_mode","No. Operaciones"])
transportes2


# In[41]:


formatoDinero(transportes, "total_value")
transportes


# In[42]:


#Unir los frames con el valor y las veces que se utilizo cada medio de transporte
metodosTransporte = outerJoin(transportes, transportes2, "transport_mode")
metodosTransporte.rename(columns={"transport_mode":"Metodo de transporte","total_value":"Valor total"},inplace=True)
metodosTransporte


# ### Valor Total en la columna total_value

# In[43]:


#Suma total de la columna total value en todo el dataframe original
print("Total en todo el Dataframe: $",format(data['total_value'].sum(),',d'))


# ### Comprobaciones

# In[44]:


#Suma de las exportaciones
format(exportaciones['Costo de Operaciones'].sum(),',d')


# In[45]:


#Suma de las importaciones
format(importaciones['Costo de Operaciones'].sum(),',d')


# In[46]:


#Esta suma tiene que ser igual al total del dataframe original
format((exportaciones['Costo de Operaciones'].sum() + importaciones['Costo de Operaciones'].sum()),',d')


# In[47]:


#80% del valor del total(total_value)
j = int(data['total_value'].sum()*(0.80))
print("Representa el 80% -> ",format(j,',d'))


# ## Opción 3

# In[48]:


def paisesExportadores(df):
    valor = []
    paises = []
    for pais_o in pais_orig:
        if (df[(df["direction"]=="Exports") & (df["origin"]==pais_o)].shape[0]) == 0: #Si aparece en la lista de paises de origen pero no exporta lo ignoramos
            continue
        else:
            valor.append(df.loc[(df["direction"]=="Exports") & (df["origin"]==pais_o), 'total_value'].sum())#Suma las filas en la columna total_value que cumplan con la condicion
            paises.append(pais_o)
    paisesEx = dict(zip(paises, valor))
    return paisesEx


# In[49]:


def paisesImportadores(df):
    valor = []
    paises = []
    for pais_d in pais_dest:
        if (df[(df["direction"]=="Imports") & (df["destination"]==pais_d)].shape[0]) == 0: #Si aparece en la lista de paises de destino pero no importa productos lo ignoramos
            continue
        else:
            valor.append(df.loc[(df["direction"]=="Imports") & (df["destination"]==pais_d), 'total_value'].sum())#Suma las filas en la columna total_value que cumplan con la condicion
            paises.append(pais_d)
            
    paisesIm = dict(zip(paises, valor))
    return paisesIm


# In[50]:


def exportacionesPorPais(df):
    operaciones = []
    paises = []
    for pais_o in pais_orig:
        if (df[(df["direction"]=="Exports") & (df["origin"]==pais_o)].shape[0]) == 0: #Si aparece en la lista de paises de origen pero no exporta lo ignoramos
            continue
        else:
            operaciones.append(df[(df["direction"]=="Exports") & (df["origin"]==pais_o)].shape[0])
            paises.append(pais_o)
    paisesEx = dict(zip(paises, operaciones))
    return paisesEx


# In[51]:


def importacionesPorPais(df):
    operaciones = []
    paises = []
    for pais_d in pais_dest:
        if (df[(df["direction"]=="Imports") & (df["destination"]==pais_d)].shape[0]) == 0: #Si aparece en la lista de paises de origen pero no exporta lo ignoramos
            continue
        else:
            operaciones.append(df[(df["direction"]=="Imports") & (df["destination"]==pais_d)].shape[0])
            paises.append(pais_d)
    paisesEx = dict(zip(paises, operaciones))
    return paisesEx


# In[52]:


#Generar los dataframes
df_paisesExp = outerJoin((dictToDf(paisesExportadores(data),["Pais","Valor Exportaciones"])),(dictToDf(exportacionesPorPais(data),["Pais","Exportaciones"])),"Pais")
df_paisesImp = outerJoin((dictToDf(paisesImportadores(data),["Pais","Valor Importaciones"])),(dictToDf(importacionesPorPais(data),["Pais","Importaciones"])),"Pais")


# In[53]:


df_paisesImp


# In[54]:


df_paisesExp


# In[55]:


#Exportaciones de USA
data[(data["direction"]=="Exports") & (data["origin"]=="USA")]
#Asi se comprueba que el procedimiento anterior es correcto


# In[56]:


#Ordenar a los paises con mayor valor en exportaciones
df_paisesExp = df_paisesExp.sort_values('Valor Exportaciones', ascending=False)
df_paisesExp


# In[57]:


#Suma del valor de las exportaciones
total1 = df_paisesExp.iloc[:,[1]].sum()
print("Suma de los paises que Exportan $",format(int(total1),',d'))


# In[58]:


#Ordenar a los paises con mayor valor en importaciones
df_paisesImp = df_paisesImp.sort_values('Valor Importaciones', ascending=False)
df_paisesImp.head(11)


# In[59]:


#Suma del valor de las importaciones
total2 = df_paisesImp.iloc[:,[1]].sum()
print("Suma de los paises que Importan $",format(int(total2),',d'))


# In[60]:


#Creamos un dataframe con paises que tengan exportaciones e importaciones
df_paisesExpImp = pd.merge(left = df_paisesExp, right = df_paisesImp,
                       how = "inner", left_on = "Pais", right_on = "Pais")


# In[61]:


df_paisesExpImp


# In[62]:


#Añadimos una columna con la suma del valor de Exportaciones e Importaciones por pais
df_paisesExpImp["Total"] = df_paisesExpImp["Valor Exportaciones"] + df_paisesExpImp["Valor Importaciones"]


# In[63]:


df_paisesExpImp = df_paisesExpImp.sort_values("Total", ascending=False)
df_paisesExpImp


# In[67]:


#Suma de la columna Total
total = df_paisesExpImp.iloc[0:8,[5]].sum()
print("Total de los paises que importan y exportan $",format(int(total),',d'))


# In[65]:


#Notamos que hay cuatro paises que aportan gran cantitad de valor pero no realizan ambas actividades
#Francia, Corea del Sur, Rusia -> Unicamente Exportan
#Tailandia -> Unicamente Importa

#Si los sumamos obtenemos
k=18614332000+14621146000+13223000000+13745000000
format(k,',d')


# In[66]:


valor_paises = total + k
print("Valor sumando los 4 paises: $",format(int(valor_paises),',d'))


# In[68]:


#El formato de dinero debe ser al ultimo ya que convierte a String y asi no se le pueden aplicar cambios
formatoDinero(exportaciones, "Costo de Operaciones")
formatoDinero(importaciones, "Costo de Operaciones")


# In[71]:


formatoDinero(exportaciones_z, "Costo de Operaciones")
formatoDinero(importaciones_z, "Costo de Operaciones")


# In[69]:


exportaciones.head(10)


# In[70]:


importaciones.head(10)


# In[73]:


exportaciones_z.head(10)


# In[74]:


importaciones_z.head()

