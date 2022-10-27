#¡CONQUISTA TÚ MENTE!
#Nombre Abreviación Tipo Descripción
#IdProducto N/A Int Identificador único del producto
#dProducto N/A Char Descripción del producto
#pnProducto N/A Char Numero de parte del producto
#cvProducto N/A Int Cantidad vendida del producto
#sProducto N/A Int Stock del producto
#Comprador N/A Char Nombre del comprador
#cComprador N/A Int Documento de identidad del comprador
#Venta N/A Char Fecha de venta del producto
#Salida: diccionario con lista de tuplas
#Tipo de retorno Descripción
#Str {:} Cadena de caracteres de la forma
#Producto consultado : {idProducto} Descripción {dProducto}
#Parte {pnProducto} Cantidad vendida {cvProducto} Stock
#{sProducto} Comprador {nComprador} Documento
#{cComprador} Fecha Venta {fVenta}
#Ó
#“No hay registro de venta de ese producto”
#Descripción del problema
#¡Apreciado tripulante!
#Un almacén que comercializa autopartes necesita llevar el registro de las partes vendidas a diferentes
#compradores. Por ende, es necesario contar con un programa software en el que se registren las
#ventas realizadas y que estas puedan ser consultadas para un tipo particular de producto.
#Información requerida
#¡Tripulante! La información a tener en cuenta es la siguiente:
#Entradas: lista de tuplas
#Nota:
#Para el desarrollo de esta implementación, el programador debe permitir introducir el registro de ventas
#desde una lista de tuplas como parámetro de AutoPartes y convertirlo luego en un diccionario
#con lista de tuplas. También, se debe permitir desde la función consultaRegistro quien llama a
#un nuevo registro desde la función AutoPartes, manejar la entrada de un parámetro tipo
#idProducto para ubicar información específica acerca del producto en información general que
#incluye la fecha de venta.
#Esqueleto:
#def AutoPartes(ventas: list):
# pass
#def consultaRegistro(ventas, idProducto):
# pass
#Ejemplo:
#Entradas Return
#([
 #(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 #(2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 #(2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
 #(3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 #(9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)
#Producto consultado : 2010 Descripción bujía #Parte MS9512 Cantidad
#vendida 4 Stock 15 Comprador Carlos Rondon Documento 1256 Fecha
#Venta 12/06/2020
#Producto consultado : 2010 Descripción bujía #Parte ER6523 Cantidad
#vendida 9 Stock 36 Comprador Pedro Montes Documento 1243 Fecha
#Venta 12/06/2020
#([
#(5489,'tornillo', 'RS8512',2,33,'Julio Perez',3654213,'13/06/2020'),
# (3215,'zocalo', 'UM8587',2,125,'Laura Macias',1256321,'13/06/2020'),
# (3698,'biela', 'PT3218',1,78,'Luis Peña',14565487,'13/06/2020'),
# (8795,'cilindro', 'AZ8794',2,96,'Carlos Casio',5612405,'13/06/2020')]), 2001)
#No hay registro de venta de ese producto
##([
# (9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'14/06/2020'),
# (9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'14/06/2020'),
 #(2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),
# (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020')]), 9852)
#Producto consultado : 9852 Descripción Culata #Parte XC9875 Cantidad
#vendida 2 Stock 165 Comprador Luis Molero Documento 3455846 Fecha
#Venta 14/06/2020
#Producto consultado : 9852 Descripción Culata #Parte XC9875 Cantidad
#vendida 2 Stock 165 Comprador Jose Mejia Documento 1355846 Fecha
#Venta 14/06/2020


def AutoPartes(ventas: list):
    venta={}  
    for idProducto, dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in ventas: 
        if venta.get(idProducto) == None: 
            venta[idProducto] = []
        venta[idProducto].append((dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta))
    return venta
def consultaRegistro(ventas, idProducto):
    if idProducto in ventas:
        for dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in ventas[idProducto]:
            print('Producto consultado :', idProducto, ' Descripción ', dProducto, ' #Parte ', pnProducto, ' Cantidad vendida ', cvProducto, ' Stock ', sProducto, ' Comprador', nComprador,' Documento ', cComprador, ' Fecha Venta ', fVenta)
    else:
        print("No hay registro de venta de ese producto")