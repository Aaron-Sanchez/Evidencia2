import datetime
import numpy as np

productos_cosmeticos = {'Nombre del articulo':['Decolorante','Protector solar','Lapiz labial','Delineador'],
                        'Codigo del articulo':[2001,2002,2003,2004],
                        'Descripcion del articulo':['Sirve para decolorar el cabello','Te proteje de los rayos UV','Hidrata tus labios','Define el contorno de los ojos'],
                        'Cantidad en almacen':[20,30,40,50,60],
                        'Precio de venta':[100,150,200,220]}
print(f"La cosmetica cuenta con lo siguiente: {productos_cosmeticos}")

atendio= 'Lo atendio Aaron'
tienda= 'Cosmeticos AARON SANCHEZ'
print('MENU')
print('[1]Registar una venta')
print('[2]Consultar una venta')
print('[3]Reporte de ventas por fecha')
print('[4]Salir')
print('')
while True:
    opcion= int(input('¿Que opcion desea?: \n'))
    if (opcion==1):
        print('Registros de Ventas')
        pregunta = int(input('¿Deseas agregar una venta? (1 es si/0 es no):\n'))
        print('Nota: en caso de querer mas de 1 de cantidad ingresa la cantidad que seas y si solo deseas 1 articulo ingresa 0 despues de poner el articulo.')
        print('Nota2:Al momento de ir en descripcion y solo llevas un articulo presionale enter.')
        if (pregunta==1):
            lista_fecha=[]
            lista_folio=[]
            lista_articulo=[]
            lista_descripcion=[]
            lista_cantidad=[]
            lista_precio=[]
            while True:
                pre3=input('Ingrese la fecha (dd/mm/aaaa):  \n')
                convercion_fecha = datetime.datetime.strptime(pre3, "%d/%m/%Y").date()
                lista_fecha.append(pre3)
                break
            while True:
                pre4=int(input('Ingrese el folio de la venta: \n'))
                lista_folio.append(pre4)
                break
            while True:
                pre5=int(input('Ingrese el codigo del articulo: \n'))
                if(pre5==0):
                    break
                lista_articulo.append(pre5)
            while True:
                pre6=input("Ingrese una descripcion del articulo:\n")
                if(pre6==''):
                    break
                lista_descripcion.append(pre6)
            while True:
                pre7=int(input("Ingrese la cantidad de piezas a vender:\n"))
                if(pre7==0):
                    break
                lista_cantidad.append(pre7)
            while True:
                pre8=int(input("Ingrese el precio de venta: \n"))
                if(pre8==0):
                    break
                lista_precio.append(pre8)
            print(tienda)
            print(atendio)
            print(f"Fecha:{lista_fecha}")
            print(f"Folio de venta: {lista_folio}")
            print(f"Codigos de los articulos: {lista_articulo}")
            print(f"Descripcion de cada producto: {lista_descripcion}")
            print(f"Cantidad de piezas a vender por cada articulo:{lista_cantidad}")
            print(f"Precio por unidad de articulo:{lista_precio}")
            arraypre7= np.array(lista_cantidad)
            arraypre8= np.array(lista_precio)
            multiplicacion= arraypre7 * arraypre8
            print(f"El total de cada articulo es:{multiplicacion}")
            suma=sum(multiplicacion)
            print(f"El total a pagar es de: ${suma}")
    if(opcion==2):
        print('Ventas')
        while True:
            ventas=int(input('Ingresa el folio que deseas consultar:\n'))
            if (ventas==0):
                print('Gracias por su tiempo.')
                break
            indice = lista_folio.index(pre4)
            print(f"La venta se encuentra en la posicion: {indice}")
            print(tienda)
            print(atendio)
            print(f"Fecha:{lista_fecha}")
            print(f"Folio de venta: {lista_folio}")
            print(f"Codigos de los articulos: {lista_articulo}")
            print(f"Descripcion de cada producto: {lista_descripcion}")
            print(f"Cantidad de piezas a vender por cada articulo:{lista_cantidad}")
            print(f"Precio por unidad de articulo:{lista_precio}")
            print(f"El total de cada articulo es:{multiplicacion}")
            print(f"El total a pagar es de: ${suma}")
            
    if(opcion==3):
        print('Ventas por fecha')
        Fecha=input('Ingresa la fecha que deseas consultar:\n')
        convercion_fecha = datetime.datetime.strptime(Fecha, "%d/%m/%Y").date()
        if(Fecha==pre3):
            print(tienda)
            print(atendio)
            print(f"Fecha:{lista_fecha}")
            print(f"Folio de venta: {lista_folio}")
            print(f"Codigos de los articulos: {lista_articulo}")
            print(f"Descripcion de cada producto: {lista_descripcion}")
            print(f"Cantidad de piezas a vender por cada articulo:{lista_cantidad}")
            print(f"Precio por unidad de articulo:{lista_precio}")
            print(f"El total de cada articulo es:{multiplicacion}")
            print(f"El total a pagar es de: ${suma}")
    if(opcion==4):
        print('Por favor espere')
        print('...')
        print("Gracias por su visita ,vuelva pronto")
        break
        
        
        
        
        
        
