# base_datos
#algunas funciones de base de datos
import tablero
import sqlite3
from datetime import datetime
base=sqlite3.connect('C://Noelia_base//base_datos.db')
c=base.cursor()

###FUNCION QUE ME PERMITE GUARDAR LOS NOMBRES DE LOS JUGADORES EN LA TABLA JUGADORES CUANDO SE INGRESAN###
###LLAMA A LA VARIABLE JUGADORES, LISTA QUE SE OBTIENE DE LA FUNCION DE AGREGAR LA CANTIDAD DE JUGADORES##
###SEGUIDA POR LOS NOMBRES###

def guardar_jugadores(jugadores):
    for i in jugadores:
        c.execute('insert into JUGADORES (NOMBRES) values ("{}");'.format(i))
    base.commit()

###FUNCION QUE GUARDA EL NOMBRE DE LA PARTIDA EN LA TABLA DE PARTIDAS, JUNTO CON SU FECHA Y HORA AL MOMENTO DE INGRESARLA###
def guardar_partida(nombre_partida):
    fecha = datetime.now()
    c.execute('insert into PARTIDA (NOMBRE_PARTIDA,FECHA_HORA) values ("{}","{}");'.format(nombre_partida,fecha))
    base.commit()


###NECESITO QUE UNA VEZ QUE EL JUGADOR TIRÓ Y SE QUEDO CON LOS DADOS: ME QUEDE EN UNA LISTA LA CANTIDAD DE PUNTAJE QUE OBTUVO
###EN ESA JUGADA: EJEMPLO:
###1 2 3 4 5 6 E F P G 2G
##[0,0,0,8,0,0,0,0,0,0,0]

####VA A LLEGAR UNA LISTA QUE CONTIENE:
####["1",0,0,0]#  - "1": ES LA CATEGORIA, PUEDE FER "E","G",ETC. ... LA CANTIDAD DE 0 ES LA CANTIDAD DE JUGADORES QUE HAY,

def guardar_result_parciales(id_partida,id_jugadores,resultados_parciales,dados,contadorTiradas):
    query='insert into RESULTADOS_PARCIALES_USUARIOS ("ID_PARTIDA",' \
          '"ID_JUGADORES","1","2","3","4","5","6",E,F,P,G,"2G","d1","d2","d3","d4","d5","LANZADAS") ' \
          'values ({},{},{},{},{},{},{},{},{},{},{},{},{},"{}","{}","{}","{}","{}",{} );'.format((id_partida),
                                                                                       (id_jugadores),
                                                                                       (resultados_parciales[0]),
                                                                                       (resultados_parciales[1]),
                                                                                       (resultados_parciales[2]),
                                                                                       (resultados_parciales[3]),
                                                                                       (resultados_parciales[4]),
                                                                                       (resultados_parciales[5]),
                                                                                       (resultados_parciales[6]),
                                                                                       (resultados_parciales[7]),
                                                                                       (resultados_parciales[8]),
                                                                                       (resultados_parciales[9]),
                                                                                       (resultados_parciales[10]),
                                                                                       (dados[0]),
                                                                                       (dados[1]),
                                                                                       (dados[2]),
                                                                                       (dados[3]),
                                                                                       (dados[4]),
                                                                                       (contadorTiradas))
    c.execute(query)
    base.commit()

#####################################################################################################
###funcion buscar partida:
###La voy a utilizar para saber si la partida existe, si existe segun el nombre, me va a devolver el id.
###Si no existe me va a devolver False
#####################################################################################
def buscar_partida(nombre_partida):
    query='SELECT ID FROM PARTIDA WHERE NOMBRE_PARTIDA="{}" LIMIT 1'.format(nombre_partida)
    c.execute(query)
    partida=c.fetchall()
    if not partida:
        return False
    else:
        return partida[0][0]


##### FUNCION PARA CREAR PARTIDA:
### si no existe el nombre de la partida me va a crear una con ese nombre:
# CAMBIARLE NOMBRE:
#def no_existe_partida(nombre_partida):
#    existe = buscar_partida(nombre_partida)
#    if not existe:
#        guardar_partida(nombre_partida)
#    else:
#        print(existe)


######CUANDO HAGO UN SELECT UTILIZO fetchal######
######c.execute('select * from JUGADORES')#######
######r = c.fetchall()###########################
######print(r)###################################

#####################################################
###ACA ESTOY SIMULANDO LA LLAMADA DE LAS FUNCIONES###
#####################################################
#jugadores=tablero.jugadores
#guardar_jugadores(jugadores)

#nombre_partida=input("ingrese nombre de la partida")
#guardar_partida(nombre_partida)

''' 
resultados_parciales=[0,0,0,12,0,0,0,0,0,0,0]
dados=[1,2,3,4,5]
contadorTiradas = 2
id_partida=1
id_jugadores=1
nombre_partida=input("ingrese el nombre de una partida:")'''

#print(buscar_partida(nombre_partida))
#id_jugadores='SELECT ID FROM JUGADORES WHERE JUGADORES.NOMBRES={});'.format(jugadores)
#guardar_idJugadores()



##### esto es si no existe una partida con ese nombre la cree.
#####existe=existe_partida(nombre_partida)
#####if not existe:
#####  guardar_partida(nombre_partida)
#####else:
#####   print(existe)