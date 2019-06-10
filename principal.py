import partida
import tiro
import tablero
import base_datos

partida.iniciar_partida()

jugadores = tablero.jugadores
puntajeParcial = tablero.puntajeParcial
cantidad = tablero.ingresoCantidadJug()
tablero.ingresoNombres(cantidad)
tablero.insertarColumnas(cantidad)
nombre_partida=''
contadorTiradas=1
dados=tiro.dados
id_partida=1
id_jugadores=[1,2,3]


for turno in range(0,1):#El 2 hay que cambiarlo por 11, que es la cantidad de turnos por jugador. Puse 2 para no probar los 11 turnos.
    print("\n* Turno número", str(turno + 1)+" *\n")
    for a in range(0,cantidad):
        print("Debe tirar el jugador Número",(a + 1),":",(jugadores[a]))#Entre esta función y la siguiente hay que agregar la tirada random y lo de jugadas especiales.
        desglosar=tiro.programa_principal()
        puntos=desglosar[0]
        categoria=desglosar[1]
        tablero.anotacion(a+1,categoria,puntos)#Una vez que tenemos la jugada final y la detección de jugada especial se invoca a esta función para anotar.
        # Hay que cambiarle la función donde el usuario ingresa los valores por una función que los agregue automaticamente al detectarlos.
        # O en su defecto, hay que agregar una función que valide si los datos ingresados son correctos.
        tiro.dados.clear()
        tiro.contadorTiradas=1
        print("")
        print("* Resultados Parciales *\n")
    tablero.mostrarPuntajeParcial()# Luego de ingresar cada anotación se muestran los resultados parciales.
    base_datos.guardar_result_parciales(id_partida, id_jugadores, puntajeParcial, dados, contadorTiradas)

tablero.sumaPuntajeFinal(cantidad,puntajeParcial) #Esto solo se pone al final sino va a saltar error.

tablero.mostrarGanador(puntajeParcial,cantidad,jugadores) # Muestra que jugador ganó y con cuántos puntos
