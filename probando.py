import tablero
import sqlite3
base=sqlite3.connect('C://Noelia_base//base_datos.db')
c=base.cursor()

id_partida=1
id_jugadores=1
resultados_parciales=tablero.puntajeParcial
dados=[1,2,3,4,5]
contadorTiradas=2

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


guardar_result_parciales(id_partida,id_jugadores,resultados_parciales,dados,contadorTiradas)