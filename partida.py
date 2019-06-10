import base_datos
###CREO UNA VARIABLE GLOBAL SOBRE EL NOMBRE DE PARTIDA. LA VA A MODIFICAR DENTRO DE LA FUNCION###
nombre_partida=''

########## ESTA ES LA PRIMERA FUNCION DE TODAS PARA INICIAR EL JUEGO
### LE PIDO AL USUARIO QUE ME DIGA SI QUIERE INICIAR UNA NUEVA PARTIDA O REANUDAR UNA PARTIDA
### SEGUN LA OPCION QUE INGRESA ME PIDE UN NOMBRE, NO ME PERMITE INGRRESAR ALGO DISTINTO DE 1 O 2

def opcion_partida():
    global nombre_partida
    opcion=int(input("Ingrese una opcion:\n"
          "1-Nueva Partida\n"
          "2-Reanudar Partida"))
    if opcion==1:
        nombre_partida = input("Ingrese el nombre de la nueva partida:")
    elif opcion==2:
        nombre_partida = input("Ingrese el nombre de la partida que desea reanudar:")
    else:
        print("La opción seleccionada no es valida")
    return opcion

### CON EL NOMBRE INICIADO ME LO GUARDA DENTRO DE LA VARIABLE NOMBRE_PARTIDA
### SI SELECCIONE:
### 1- NUEVA PARTIDA: ESTA FUNCION LO QUE VA A HACER ES DECIRME SI EXISTE O NO EL NOMBRE QUE INGRESE:
##################### SI NO EXISTE EL NOMBRE QUE INGRESE ME LO VA A GUARDAR EN LA BASE DE DATOS
##################### SI EL NOMBRE YA EXISTE ME VA A DECIR QUE INGRESE OTRO NOMBRE NUEVAMENTE, VUELVE CICLO.
### 2 - REANUDAR PARTIDA: ESTA FUNCION ME VA A BUSCAR EL ID DE LA PARTIDA SEGUN EL NOMBRE QUE INGRESE EN LA
######################### BASE DE DATOS.
def iniciar_partida():
    continuar=True
    global nombre_partida
    opcion=opcion_partida()
    while continuar==True:
        if opcion==1:
            busqueda=base_datos.buscar_partida(nombre_partida)
            if busqueda==False:
                return base_datos.guardar_partida(nombre_partida)
            else:
                nombre_partida=input("El nombre de la partida ya existe. Por favor ingrese otro nombre:")
        elif opcion==2:
            return base_datos.buscar_partida(nombre_partida)


#####PROBANDO NUEVA PARTIDA.
###def verificar_opcion():
#    if opcion_partida()==1:
#        base_datos_avanzado.buscar_partida(nombre_partida)
#        existe =base_datos_avanzado.ar_partida(nombre_partida)
#        if not existe:
#            guardar_partida(nombre_partida)
#        else:
#            print(existe)
#    elif opcion_partida()==2:
#        base_datos_avanzado.buscar_partida(nombre_partida)


