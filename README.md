# Curso de Análisis de datos con Python - Emtech 🏫

_En este repositorio se encuentran los proyectos relacionados al primer nivel del Learning Path "Data Science" impartido por EMTECH: Emerging Technologies Institute_
<br/><br/>

## Proyecto 1 📝

LifeStore es una tienda virtual que maneja una amplia gama de artículos, 
recientemente, la Gerencia de ventas, se percató que la empresa tiene una 
importante acumulación de inventario. Asimismo, se ha identificado una reducción 
en las búsquedas de un grupo importante de productos, lo que ha redundado en 
una disminución sustancial de sus ventas del último trimestre.

### Consigna 📌
Realizar un ánalisis de la rotación de productos para la gerencia de ventas, identificando los siguientes elementos:
<br/>

* Productos más vendidos y productos rezagados a partir del análisis de las categorías con menores ventas y categorías con menores búsquedas.
* Productos por reseña en el servicio a partir del análisis de categorías con mayores ventas y categorías con mayores búsquedas.
* Sugerir una estrategia de productos a retirar del mercado así como sugerencia de cómo reducir la acumulación de inventario considerando los datos de ingresos y ventas mensuales.

[Documentación 📂](https://github.com/EliasBautista/Curso_Emtech/blob/master/Requerimientos/ProyectoFinal1.pdf) - Aquí se puede consultar y descargar la documentación completa del primer proyecto.

[Fuente de datos 📋](https://github.com/EliasBautista/Curso_Emtech/blob/master/Requerimientos/ProyectoFinal2.pdf) - Aquí se puede consultar y descargar los datos en formato de listas en python, con la información relevante para resolver el proyecto.

### Solución 🔎
Como solución a las necesidades de la gerencia de ventas se pesentó un reporte con un análisis detallado de los elementos más importantes relacionados al inventario de productos. Dentro del documento se sugiere una estrategia de productos a retirar del mercado, así como un par de observaciones respecto a la base de dato

[Reporte 📑](https://github.com/EliasBautista/Curso_Emtech/blob/master/Soluciones/REPORTE-01-BAUTISTAFLORES-HUGOELIAS.pdf) - Aquí se puede consultar y descargar el reporte entregado a la gerencia de ventas, la solución al primer proyecto.

[Código Python 💻](https://github.com/EliasBautista/Curso_Emtech/tree/master/Programas_Python) - Aquí se puede descargar el código Python utilizado para analizar los datos del inventario (Listas.py + Proyecto01.py).

[Probar Código 👨🏻‍💻](https://replit.com/@EliasBautista/Proyecto01#main.py) - En este link se puede probar el código generado de este proyecto, como reto no se pueden usar funciones ni métodos, únicamente listas y bucles.

<br/>
<hr/>
<br/>

## Proyecto 2 📝
Synergy Logistics es una empresa dedicada a la intermediación de servicios de importación y exportación de diferentes productos. Actualmente la empresa cuenta con una base de datos que refleja las rutas más importantes que opera desde el año 2015, con su respectivo origen y destino, año, producto, modo de transporte y valor total. Su propósito, es que a partir de estos datos se genere un análisis que sirva de la base para la estructuración de su estrategia operativa.

### Consigna 📌
La Dirección de Synergy Logistics ha solicitado al equipo operativo, realizar una propuesta que permita enfocar las prioridades de la estrategia operativa 2021; para ello, se plantea analizar la viabilidad de 3 opciones de enfoque: rutas de importación y exportación, medio de transporte utilizado y valor total de importaciones y exportaciones.

* <b>Opción 1) Rutas de importación y exportación.</b> Synergy logistics está considerando la posibilidad de enfocar sus esfuerzos en las 10 rutas más demandadas. Acorde a los flujos de importación y exportación, ¿cuáles son esas 10 rutas? ¿le conviene implementar esa estrategia? ¿porqué?
* <b>Opción 2) Medio de transporte utilizado.</b> Cuáles son los 3 medios de transporte más importantes para Synergy logistics considerando el valor de las importaciones y exportaciones? ¿Cuál es medio de transporte que podrían reducir?
* <b>Opción 3) Valor total de importaciones y exportaciones.</b> Si Synergy Logistics quisiera enfocarse en los países que le generan el 80% del valor de las exportaciones e importaciones ¿en qué grupo de países debería enfocar sus esfuerzos?

[Documentación 📂](https://github.com/EliasBautista/Curso_Emtech/blob/master/Requerimientos/ProyectoFinal2.pdf) - Aquí se puede consultar y descargar la documentación completa del segundo proyecto.

[Fuente de datos 📋](https://github.com/EliasBautista/Curso_Emtech/blob/master/Requerimientos/ProyectoFinal2.pdf) - Aquí se puede consultar y descargar los datos en formato csv, con la información relevante para resolver el proyecto.

### Solución 🔎
De las anteriores opciones la mejor es la opción número dos, ya que aun excluyendo el método de transporte “Road”, la suma del valor total de los tres medios de transporte restantes es mayor al 80% del valor total que se considera en la opción tres y también es el doble del valor de la opción uno.
Por lo que mi recomendación es reducir el método de transporte “Road” y priorizar el resto.

A modo de conclusión me gustaría agregar que no es la mejor opción enfocarse en las rutas más demandadas ya que estas no generan el valor suficiente, comparado a las otras dos opciones y la tercera opción genera un valor similar a la segunda opción, pero a mi consideración la tercera opción es más compleja que la segunda.

[Reporte 📑](https://github.com/EliasBautista/Curso_Emtech/blob/master/Soluciones/REPORTE_02_BAUTISTAFLORES_HUGOELIAS.pdf) - Aquí se puede consultar y descargar el reporte entregado a la Synergy Logistics, la solución al segundo proyecto.

[Reporte Jupiter Notebook 📓](https://github.com/EliasBautista/Curso_Emtech/blob/master/Soluciones/REPORTE_02_BAUTISTAFLORES_HUGOELIAS.pdf) - Para reforzar la información del reporte se puede consultar también este reporte generado a partir del código hecho en un notebook de Jupiter con Python.

[Código Python 💻](https://github.com/EliasBautista/Curso_Emtech/tree/master/Programas_Python) - Aquí se puede descargar el código Python utilizado para analizar los datos del inventario (synergy_logistics_database.csv + Proyecto02.py).

[Probar Código 👨🏻‍💻](https://replit.com/@EliasBautista/Proyecto02#main.py) - En este link se puede probar el código generado de este proyecto, se utilizaron varias librerías como numpy y pandas para generar dataframes a partir del csv.

### Capturas 📷
