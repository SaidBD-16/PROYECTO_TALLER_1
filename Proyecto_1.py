option = ""
admin = ""






#=======================================================================================


#Funcion auxiliar
#E: Fecha
#S: validar si el formato de la fecha es correcto
#R: el formato de la fecha debe ser correcto

def validar_fecha(fecha):

    # valida que la cantidad de digitos sea 9; DD/MM/YYYY = NUEVE DIGITOS
    if len(fecha) != 10:
        return False

    # solo permite ¨/¨ en esas posiciones 
    if fecha[2] != "/" or fecha[5] != "/":
        return False

    # separa manualmete cada digito
    dia = fecha[0] + fecha[1]
    mes = fecha[3] + fecha[4]
    año = fecha[6] + fecha[7] + fecha[8] + fecha[9]

    # valida que cada valiable contenga unicamente digitos
    if dia.isdigit() == False or mes.isdigit() == False or año.isdigit() == False:
        return False
    
    # se convierten en numeros 
    dia = int(dia)
    mes = int(mes)

    # debe respetar el formato ningun mes es menor a 1 ni mayor a 12
    if mes < 1 or mes > 12:
        return False

    # debe respetar el formato ningun dia es menor a 1 ni mayor a 31
    if dia < 1 or dia > 31:
        return False

    # valida que el mes de febrero no sea mayor a 28
    if mes == 2 and dia > 28:
        return False

    # abril, junio, septiembre y noviembre no tienen mas de 30 dias 
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30:
            return False

    return True


#=======================================================================================


#Funcion auxiliar
#E: hora
#S: validar si el formato de la hora es correcto
#R: el formato de la hora debe ser correcto
def validar_hora(hora):
    
    # no puede pasar de la 4 posicion, no seria "5 <" el formato estaria incorrecto; Formato: 00:00 = 4
    if len(hora) != 5:
        return False

    # valida que la posicion 2 unicamente posea ":"
    if hora[2] != ":":
        return False

    horas = hora[0] + hora[1]
    minutos = hora[3] + hora[4]

    # verifica que sean numeros 
    if horas.isdigit() == False or minutos.isdigit() == False:
        return False

    horas = int(horas)
    minutos = int(minutos)

    # valida que las horas ni minutos se pasen de los limites 
    if horas < 0 or horas > 23:
        return False

    if minutos < 0 or minutos > 59:
        return False

    return True


#=======================================================================================







#E: Ninguna
#S: Uno de los dos menús adjuntos
#R: Debe ingresar "1, 2 o 3" como opciones unicas

while option != "3":
    print("")
    print("==========================================")
    print("              MENU PRINCIPAL              ")
    print("==========================================")
    print("(1) Opciones Administrativas")
    print("(2) Opciones de Usuario")
    print("(3) Salir")
    print("")
    option = input("Digite una opcion: ")
    print("")
    
    if option == "1":
        
        usuario    = input("Usuario: ")
        contraseña = input("contraseña: ")

        datos      = usuario + ";" + contraseña

        #E: El nombre del archivo 
        #S: Verifica que "datos" se encuentra en el archivo 
        #R: Solo acepta que los valores ingresados coinsidan con la informacion en el archivo
        with open("acceso.txt", "r") as archivo:
            linea = archivo.readline()

            acceso = False
            while linea != "":  
                linea = linea.strip()
                
                if datos == linea:
                    print("Acceso concedido")
                    acceso = True 
                    linea = ""

                    #E: option
                    #S: Menú administrativo
                    #R: Solo puede ingresar unicamente las opciones permitidas 
 
                    while option != "18":
                        print("")
                        print("==========================================")
                        print("            MENU ADMINISTRATIVO           ")
                        print("==========================================")
                        print("(11) Gestión de modelos de autobús")
                        print("(12) Gestión de unidades")
                        print("(13) Gestión de conductores")
                        print("(14) Gestión de rutas")
                        print("(15) Gestión de paradas por ruta")
                        print("(16) Programación de salidas")
                        print("(17) Consultar historial de abordajes")
                        print("(18) Regresar al menú principal")
                        print("")
                        option = input("Digite una opcion: ")
                        print("")

                        #E: option 11
                        #S: Una de las opciones validas "1, 2, 3, 4 o 5"
                        #R: Solo se deben ingresar opciones permitidas del menú
        
                        while option == "11":
                            print("")
                            print("==========================================")
                            print("       GESTION DE MODELOS DE AUTOBUS      ")
                            print("==========================================")
                            print("(1) Incluir")
                            print("(2) Eliminar")
                            print("(3) Modificar")
                            print("(4) Mostrar")
                            print("(5) Atras")
                            print("")
                            admin = input("Digite una opcion: ")
                            print("")

                            if admin:

                                #E: modelo
                                #S: Modelo incluido en el archivo
                                #R: La descripcion del modelo no se puede repetir 
                                #Incluir 
                                if admin == "1":
                                    
                                    descripcion_del_modelo = input("Descripción del modelo: ")
                                    marca = input("Marca: ")
                                    cantidad_de_asientos = input("Cantidad de asientos: ")
                                    cantidad_espacios_pie = input("Cantidad de espacios de pie: ")

                                    # valida que ningun campo quede vacio
                                    if descripcion_del_modelo == "" or marca == "" or cantidad_de_asientos == "" or cantidad_espacios_pie == "":
                                        print("No se puede agregar el modelo, ningun campo puede quedar vacio")

                                    else:
                                        modelo = descripcion_del_modelo + ";" + marca + ";" + cantidad_de_asientos + ";" + cantidad_espacios_pie

                                        existe = False

                                        # verifica que la descripcion del modelo no se repita en el archivo
                                        with open("modelos.txt", "r") as archivo:
                                            linea = archivo.readline()

                                            while linea != "":
                                                datos = linea.strip().split(";")

                                                if datos[0] == descripcion_del_modelo:
                                                    existe = True

                                                linea = archivo.readline()
                                        # no se incluye
                                        if existe == True:
                                            print("Ya esta incluido")

                                        else:
                                            # se añade al archivo
                                            with open("modelos.txt", "a") as archivo:
                                                archivo.write("\n" + modelo)


                                #E: descripcion
                                #S: el archivo con datos eliminados 
                                #R: La descripcion del modelo no puede estar asociado si desea eliminar
                                #Eliminar             
                                if admin == "2":
                                    descripcion_del_modelo = input("Descripcion del modelo a eliminar: ")

                                    existe = False

                                    # Busca si se encuentra si la descripcion de modelos se encuentra asociado en unidades.txt
                                    with open("unidades.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            if descripcion_del_modelo == datos[1]:
                                                existe = True

                                            linea = archivo.readline()
                                    
                                    if existe == True:
                                        print("El modelo esta asociado a una unidad")
                                    else:
                                        # agrega a nuevo la linea que no sea igual a la descripcion 
                                        nuevo = []

                                        with open("modelos.txt", "r") as archivo:
                                            linea = archivo.readline()

                                            while linea != "":
                                                datos = linea.strip().split(";")

                                                if datos[0] != descripcion_del_modelo:
                                                    nuevo += [linea]

                                                linea = archivo.readline()
                                        # añade linea por linea en modelo.txt 
                                        with open("modelos.txt", "w") as archivo:
                                            i= 0

                                            while i < len(nuevo):
                                                archivo.write(nuevo[i])
                                                i += 1

                                        print("Modelo eliminado")
                                        
                                #E: descripcion
                                #S: el archivo con datos modificados
                                #R: La descripcion del modelo no puede estar asociado si desea modificar
                                #Modificar         
                                if admin == "3":
                                    descripcion_del_modelo = input("Descripcion del modelo a modificar: ")

                                    existe = False
                                    #Busca si se encuentra si la descripcion de modelos se encuentra asociado en unidades.txt
                                    with open("unidades.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            if descripcion_del_modelo == datos[1]:
                                                existe = True

                                            linea = archivo.readline()

                                    if existe == True:
                                        print("No se puede modificar el modelo esta asociado")
                                    else:
                                        nuevo = []
                                        # pasa de varias lineas a una y de una linea pasa a una lista con los datos de la linea 
                                        with open("modelos.txt", "r") as archivo:
                                            linea = archivo.readline()

                                            while linea != "":
                                                datos = linea.strip().split(";")

                                                if datos[0] == descripcion_del_modelo:

                                                    nueva_descripcion = input("Descripcion del modelo: ")
                                                    nueva_marca = input("Marca: ")
                                                    nuevos_asientos = input("Cantidad de asientos: ")
                                                    nuevos_espacios = input("Cantidad de espacios de pie: ")
                                                    # verifica que lo ingresado sea distinto a vacio para poder modificarlo
                                                    if nueva_descripcion == "":
                                                        nueva_descripcion = datos[0]

                                                    if nueva_marca == "":
                                                        nueva_marca = datos[1]
                                                    # verifica si son unicamente numeros, si no se agrega su valor anterior 
                                                    if nuevos_asientos == "":
                                                        nuevos_asientos = datos[2]
                                                    elif nuevos_asientos.isdigit() == False:
                                                        nuevos_asientos = datos[2]

                                                    if nuevos_espacios == "":
                                                        nuevos_espacios = datos[3]
                                                    elif nuevos_espacios.isdigit() == False:
                                                        nuevos_espacios = datos[3]

                                                    modelo = nueva_descripcion + ";" + nueva_marca + ";" + nuevos_asientos + ";" + nuevos_espacios + "\n"

                                                    nuevo += [modelo]

                                                else:
                                                    # si no es igual a la descripcion buscada agrega la misma linea sin modificar
                                                    nuevo += [linea]

                                                linea = archivo.readline()
                                        
                                        with open("modelos.txt", "w") as archivo:
                                            i = 0

                                            while i < len(nuevo):
                                                archivo.write(nuevo[i])
                                                i += 1

                                        print("Modelo modificado")



                                #E: Ninguna
                                #S: muestra los modelos
                                #R: ninguna
                                #Mostrar 
                                if admin == "4":
                                    # recorre el archivo linea por linea mientras cada linea la hace una linea para poner las posiciones de la lista en cada print
                                    with open("modelos.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            
                                            print("------------------------------------------")
                                            print("             MODELO DE AUTOBUS            ")
                                            print("------------------------------------------")
                                            print("Descripcion: " + datos[0])
                                            print("Marca: " + datos[1])
                                            print("Cantidad de asientos: " + datos[2])
                                            print("Cantidad de espacios de pie: " + datos[3])
                                            print("")

                                            linea = archivo.readline()
                                            
                                if admin == "5":
                                    option = "5"                   

                        #E: option 12
                        #S: Una de las opciones validas "1, 2, 3, 4 o 5"
                        #R: Solo se deben ingresar opciones permitidas del menú   
                        while option == "12":
                            print("")
                            print("==========================================")
                            print("            GESTION DE UNIDADES           ")
                            print("==========================================")
                            print("(1) Incluir")
                            print("(2) Eliminar")
                            print("(3) Modificar")
                            print("(4) Mostrar")
                            print("(5) Atras")
                            print("")
                            admin = input("Digite una opcion: ")
                            print("")


                            
                            #E: unidad
                            #S: Unidad incluida en el archivo
                            #R: La placa no se puede repetir y el modelo debe existir
                            #Incluir 
                            if admin == "1":

                                placa = input("Placa: ")
                                modelo = input("Modelo: ")
                                año = input("Año: ")
                                empresa = input("Empresa operadora: ")
                                
                                # las casillas no pueden estar vacias 
                                if placa == "" or modelo == "" or año == "" or empresa == "":
                                    print("No se puede agregar unidades vacias")

                                else:
                                    modelo_existe = False
                                    # se verifica que el modelo exista para poder incluir 
                                    with open("modelos.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            if modelo == datos[0]:
                                                modelo_existe = True

                                            linea = archivo.readline()

                                    if modelo_existe == False:
                                        print("El modelo no esta registrado")

                                    else:
                                        placa_existe = False
                                        # verifica que la placa no se encuentre en el archivo unidades.txt
                                        with open("unidades.txt", "r") as archivo:
                                            linea = archivo.readline()

                                            while linea != "":
                                                datos = linea.strip().split(";")

                                                if placa == datos[0]:
                                                    placa_existe = True

                                                linea = archivo.readline()
                                        # no se añade
                                        if placa_existe == True:
                                            print("La placa ya esta registrada")

                                        else:
                                            # se agrega a un al archivo 
                                            nuevo = placa + ";" + modelo + ";" + año + ";" + empresa

                                            with open("unidades.txt", "a") as archivo:
                                                archivo.write("\n" + nuevo)

                                            print("Unidad agregada")
                                        


                        
                            #E: placa
                            #S: Unidad eliminada del archivo
                            #R: La unidad no puede estar asociada a una salida
                            if admin == "2":

                                placa = input("Placa de la unidad a eliminar: ")

                                existe = False
                                # verifica que la placa no este asociada
                                with open("salidas.txt", "r") as archivo:
                                    linea = archivo.readline()

                                    while linea != "":
                                        datos = linea.strip().split(";")

                                        if placa == datos[2]:
                                            existe = True

                                        linea = archivo.readline()
                                # no elimina 
                                if existe == True:
                                    print("La unidad esta asociada a una salida")

                                else:
                                    # forma nuevamente el contenido del archivo desde cero
                                    nuevo = []

                                    with open("unidades.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            if datos[0] != placa:
                                                nuevo += [linea]

                                            linea = archivo.readline()
                                    
                                    # agrega el contenido nuevo al archivo
                                    with open("unidades.txt", "w") as archivo:
                                        i = 0

                                        while i < len(nuevo):
                                            archivo.write(nuevo[i])
                                            i += 1

                                    print("Unidad eliminada")


                            
                            #E: placa
                            #S: archivo de unidades con los datos modificados
                            #R: La unidad no puede estar asociada a una salida y el modelo debe existir
                            if admin == "3":

                                placa = input("Placa de la unidad a modificar: ")

                                existe = False

                                # Buscamos si la placa esta asociada a una salida
                                with open("salidas.txt", "r") as archivo:
                                    linea = archivo.readline()

                                    while linea != "":
                                        datos = linea.strip().split(";")

                                        if placa == datos[2]:
                                            existe = True

                                        linea = archivo.readline()

                                if existe == True:
                                    print("La unidad esta asociada a una salida")

                                else:

                                    nuevo = []

                                    # Buscamos los valores que se quieren modificar
                                    with open("unidades.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            if datos[0] == placa:

                                                nueva_placa = input("Nueva placa: ")
                                                nuevo_modelo = input("Nuevo modelo: ")
                                                nuevo_año = input("Nuevo año: ")
                                                nueva_empresa = input("Nueva empresa operadora: ")



                                                # Si la placa esta vacia conserva la anterior
                                                if nueva_placa == "":
                                                    nueva_placa = datos[0]



                                                else:
                                                    placa_existe = False
                                                    # de lo contrario busca que no exista 
                                                    with open("unidades.txt", "r") as archivo_unidades:
                                                        linea_unidad = archivo_unidades.readline()

                                                        while linea_unidad != "":
                                                            datos_unidad = linea_unidad.strip().split(";")

                                                            if nueva_placa == datos_unidad[0] and nueva_placa != placa:
                                                                placa_existe = True

                                                            linea_unidad = archivo_unidades.readline()

                                                    if placa_existe == True:
                                                        print("La placa ya esta registrada")
                                                        nueva_placa = datos[0]



                                                # Si el modelo esta vacio conserva el anterior
                                                if nuevo_modelo == "":
                                                    nuevo_modelo = datos[1]



                                                else:
                                                    modelo_existe = False
                                                    # busca que el modelo exista en modelo.txt
                                                    with open("modelos.txt", "r") as archivo_modelos:
                                                        linea_modelo = archivo_modelos.readline()

                                                        while linea_modelo != "":
                                                            datos_modelo = linea_modelo.strip().split(";")

                                                            if nuevo_modelo == datos_modelo[0]:
                                                                modelo_existe = True

                                                            linea_modelo = archivo_modelos.readline()



                                                    # no modifica el modelo 
                                                    if modelo_existe == False:
                                                        print("El modelo no esta registrado")
                                                        nuevo_modelo = datos[1]



                                                # Si el año esta vacio conserva el anterior
                                                if nuevo_año == "":
                                                    nuevo_año = datos[2]



                                                # Si la empresa esta vacia conserva la anterior
                                                if nueva_empresa == "":
                                                    nueva_empresa = datos[3]

                                                unidad = nueva_placa + ";" + nuevo_modelo + ";" + nuevo_año + ";" + nueva_empresa + "\n"

                                                nuevo += [unidad]

                                            else:
                                                # si no se encuentra la placa se mantiene 
                                                nuevo += [linea]

                                            linea = archivo.readline()
                                    # agrega todos los datos a unidades.txt
                                    with open("unidades.txt", "w") as archivo:
                                        i = 0

                                        while i < len(nuevo):
                                            archivo.write(nuevo[i])
                                            i += 1

                                    print("Unidad modificada")




                                    
                            
                            #E: Ninguna
                            #S: muestra los modelos
                            #R: ninguna
                            #Mostrar 
                            if admin == "4":
                                # recorre el archivo linea por linea mientras cada linea la hace una linea para poner las posiciones de la lista en cada print
                                with open("unidades.txt", "r") as archivo:
                                    linea = archivo.readline()

                                    while linea != "":
                                        datos = linea.strip().split(";")

                                        
                                        print("------------------------------------------")
                                        print("                  UNIDAD                  ")
                                        print("------------------------------------------")
                                        print("Placa: " + datos[0])
                                        print("Modelo: " + datos[1])
                                        print("año: " + datos[2])
                                        print("Empresa operadora: " + datos[3])
                                        print("")

                                        linea = archivo.readline()
                                        
                            if admin == "5":
                                option = "5"
                                
                        while option == "13":
                            print("")
                            print("==========================================")
                            print("            GESTION DE CONDUCTORES        ")
                            print("==========================================")
                            print("(1) Incluir")
                            print("(2) Eliminar")
                            print("(3) Modificar")
                            print("(4) Mostrar")
                            print("(5) Atras")
                            print("")
                            admin = input("Digite una opcion: ")
                            print("")



                            #E: datos del conductor
                            #S: Conductor incluido en el archivo
                            #R: La cedula no se puede repetir y ningun campo puede estar vacio
                            if admin == "1":

                                cedula = input("Cedula: ")
                                nombre = input("Nombre completo: ")
                                licencia = input("Tipo de licencia: ")
                                fecha = input("Fecha de vencimiento: ")
                                jornada = input("Jornada maxima diaria: ")

                                if cedula == "" or nombre == "" or licencia == "" or fecha == "" or jornada == "":
                                    print("No se puede agregar el conductor, ningun campo puede quedar vacio")

                                elif validar_fecha(fecha) == False:
                                    print("La fecha no es valida; FORMATO: DD/MM/YYYY")
                                    
                                else:

                                    existe = False
                                    #Verifica que la cedula no se encuentre en el atchivo conductores.txt
                                    with open("conductores.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            if cedula == datos[0]:
                                                existe = True

                                            linea = archivo.readline()
                                    # no se agrega 
                                    if existe == True:
                                        print("La cedula ya esta registrada")

                                    else:
                                        # se añade al archivo
                                        conductor = cedula + ";" + nombre + ";" + licencia + ";" + fecha + ";" + jornada

                                        with open("conductores.txt", "a") as archivo:
                                            archivo.write(conductor + "\n")

                                        print("Conductor agregado")

                                        
                            #E: cedula
                            #S: Archivo de conductores con el conductor eliminado
                            #R: El conductor no puede estar asociado a una salida

                            if admin == "2":

                                cedula = input("Cedula del conductor a eliminar: ")

                                existe = False
                                # valida que la cedula a eliminar no se encuentre en el archivo salidas.txt
                                with open("salidas.txt", "r") as archivo:
                                    linea = archivo.readline()

                                    while linea != "":
                                        datos = linea.strip().split(";")

                                        if cedula == datos[3]:
                                            existe = True

                                        linea = archivo.readline()
                                # no elimina 
                                if existe == True:
                                    print("El conductor esta asociado a una salida")

                                else:

                                    nuevo = []
                                    # mientras cada linea sea distinta a la asignada se agregara a nuevo
                                    with open("conductores.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            if datos[0] != cedula:
                                                nuevo += [linea]

                                            linea = archivo.readline()
                                    # rescribe el archivo 
                                    with open("conductores.txt", "w") as archivo:
                                        i = 0

                                        while i < len(nuevo):
                                            archivo.write(nuevo[i])
                                            i += 1

                                    print("Conductor eliminado")




                            #E: cedula
                            #S: Archivo de conductores con los datos modificados
                            #R: El conductor no puede estar asociado a una salida y la cedula no se puede repetir

                            if admin == "3":

                                cedula = input("Cedula del conductor a modificar: ")

                                existe = False

                                # Buscamos si el conductor esta asociado a una salida
                                with open("salidas.txt", "r") as archivo:
                                    linea = archivo.readline()

                                    while linea != "":
                                        datos = linea.strip().split(";")

                                        if cedula == datos[3]:
                                            existe = True

                                        linea = archivo.readline()
                                # no se modifica
                                if existe == True:
                                    print("El conductor esta asociado a una salida")

                                else:

                                    nuevo = []
                                    # se sustituira linea seleccionada por la nueva 
                                    with open("conductores.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            if datos[0] == cedula:

                                                nueva_cedula = input("Nueva cedula: ")
                                                nuevo_nombre = input("Nuevo nombre completo: ")
                                                nueva_licencia = input("Nuevo tipo de licencia: ")
                                                nueva_fecha = input("Nueva fecha de vencimiento: ")
                                                nueva_jornada = input("Nueva jornada maxima diaria: ")

                                                # Valida que no se encuentre vacia
                                                if nueva_cedula == "":
                                                    nueva_cedula = datos[0]

                                                else:
                                                    cedula_existe = False
                                                    # valida que la cedula ingresada no deba coisidir con la nueva que se digito
                                                    with open("conductores.txt", "r") as archivo_conductores:
                                                        linea_conductor = archivo_conductores.readline()

                                                        while linea_conductor != "":
                                                            datos_conductor = linea_conductor.strip().split(";")

                                                            if nueva_cedula == datos_conductor[0] and nueva_cedula != cedula:
                                                                cedula_existe = True

                                                            linea_conductor = archivo_conductores.readline()

                                                    if cedula_existe == True:
                                                        print("La cedula ya esta registrada")
                                                        nueva_cedula = datos[0]
                                              
                                                # valida que los ningun dato quede vacio
                                                if nuevo_nombre == "":
                                                    nuevo_nombre = datos[1]

                                                if nueva_licencia == "":
                                                    nueva_licencia = datos[2]

                                                if nueva_fecha == "":
                                                    nueva_fecha = datos[3]

                                                elif validar_fecha(nueva_fecha) == False:
                                                    print("La fecha no es valida")
                                                    nueva_fecha = datos[3]

                                                if nueva_jornada == "":
                                                    nueva_jornada = datos[4]
                                                #añade
                                                conductor = nueva_cedula + ";" + nuevo_nombre + ";" + nueva_licencia + ";" + nueva_fecha + ";" + nueva_jornada + "\n"

                                                nuevo += [conductor]

                                            else:
                                                # no se modifica esa linea, sigue con la siguiente 
                                                nuevo += [linea]

                                            linea = archivo.readline()
                                    # rescribe el archivo con los datos modificados
                                    with open("conductores.txt", "w") as archivo:
                                        i = 0

                                        while i < len(nuevo):
                                            archivo.write(nuevo[i])
                                            i += 1

                                    print("Conductor modificado")


                            #E: Ninguna
                            #S: muestra los conductores
                            #R: ninguna
                            #Mostrar 
                            if admin == "4":
                                 with open("conductores.txt", "r") as archivo:
                                    linea = archivo.readline()

                                    while linea != "":
                                        datos = linea.strip().split(";")
                                        
                                        print("------------------------------------------")
                                        print("                CONDUCTORES               ")
                                        print("------------------------------------------")
                                        print("Cedula: " + datos[0])
                                        print("Nombre completo: " + datos[1])
                                        print("Tipo de licencia: " + datos[2])
                                        print("Fecha de vencimiento: " + datos[3])
                                        print("Jornada maxima diaria: " + datos[4])
                                        print("")

                                        linea = archivo.readline()


                                        
                            if admin == "5":
                                option = "5"


                
                        while option == "14":
                            print("")
                            print("==========================================")
                            print("              GESTION DE RUTAS            ")
                            print("==========================================")
                            print("(1) Incluir")
                            print("(2) Eliminar")
                            print("(3) Modificar")
                            print("(4) Mostrar")
                            print("(5) Atras")
                            print("")
                            admin = input("Digite una opcion: ")
                            print("")



                            #E: codigo de ruta, lugar de origen, lugar de destino, distancia total en kilómetros y tarifa por kilómetro
                            #S: los datos agregados al archivo de rutas 
                            #R: La cedula no se puede repetir y ningun campo puede estar vacio
                            if admin:
                                if admin == "1":
                                    codigo_ruta = input("Codigo de ruta: ")
                                    lugar_origen = input("Lugar de origen: ")
                                    lugar_destino = input("Lugar de destino: ")
                                    distancia_total = input("Distancia total en kilómetros: ")
                                    tarifa_por_kilometro = input("Tarifa por kilómetro: ")

                                    if codigo_ruta == "" or lugar_origen == "" or lugar_destino == "" or distancia_total == "" or tarifa_por_kilometro == "":
                                        print("No se puede agregar la ruta, ningun campo puede quedar vacio")

                                    else:

                                        existe = False
                                        #Verifica que la ruta no se encuentre en el archivo rutas.txt
                                        with open("rutas.txt", "r") as archivo:
                                            linea = archivo.readline()

                                            while linea != "":
                                                datos = linea.strip().split(";")

                                                if codigo_ruta == datos[0]:
                                                    existe = True

                                                linea = archivo.readline()
                                        # no se agrega 
                                        if existe == True:
                                            print("El codigo de ruta ya esta registrada")

                                        else:
                                            # se añade al archivo
                                            ruta = codigo_ruta + ";" + lugar_origen + ";" + lugar_destino + ";" + distancia_total + ";" + tarifa_por_kilometro

                                            with open("rutas.txt", "a") as archivo:
                                                archivo.write(ruta + "\n")

                                            print("Ruta agregado")


                               
                                #E: codigo de ruta 
                                #S: El archivo sin la linea asignada
                                #R: La ruta no puede estar asociado a una salida

                                if admin == "2":

                                    codigo_ruta = input("Codigo de ruta a eliminar: ")

                                    existe = False
                                    # valida que el codigo de ruta a eliminar no se encuentre en el archivo salidas.txt ni paradas.txt
                                    # archivo de salidas
                                    with open("salidas.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            if codigo_ruta == datos[1]:
                                                existe = True

                                            linea = archivo.readline()

                                    #archivo de paradas 
                                    with open("paradas.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            if codigo_ruta == datos[0]:
                                                existe = True

                                            linea = archivo.readline()
                                            
                                    # no elimina 
                                    if existe == True:
                                        print("El codigo de ruta tinen paradas registradas o salidad programadas")

                                    else:

                                        nuevo = []
                                        # mientras cada linea sea distinta a la asignada se agregara a nuevo
                                        with open("rutas.txt", "r") as archivo:
                                            linea = archivo.readline()

                                            while linea != "":
                                                datos = linea.strip().split(";")

                                                if datos[0] != codigo_ruta:
                                                    nuevo += [linea]

                                                linea = archivo.readline()
                                        # rescribe el archivo 
                                        with open("rutas.txt", "w") as archivo:
                                            i = 0

                                            while i < len(nuevo):
                                                archivo.write(nuevo[i])
                                                i += 1

                                        print("Ruta eliminada")




                                
                                #E: Codigo de ruta
                                #S: Archivo de rutas con los datos modificados
                                #R: El codigo de ruta no puede estar asociado a una salida o con paradas registradas

                                if admin == "3":

                                    codigo_ruta = input("El codigo de ruta a modificar: ")

                                    existe = False

                                    # Buscamos si el codigo esta asociado a una salida
                                    with open("salidas.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            if codigo_ruta == datos[1]:
                                                existe = True

                                            linea = archivo.readline()

                                    # Buscamos si el codigo esta asociado a una parada
                                    with open("paradas.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            if codigo_ruta == datos[0]:
                                                existe = True

                                            linea = archivo.readline()

                                    # No se modifica
                                    if existe == True:
                                        print("El codigo de ruta esta asociado a una salida o con paradas registradas")

                                    else:

                                        nuevo = []

                                        # Se sustituira la linea seleccionada por la nueva
                                        with open("rutas.txt", "r") as archivo:
                                            linea = archivo.readline()

                                            while linea != "":
                                                datos = linea.strip().split(";")

                                                if datos[0] == codigo_ruta:

                                                    nuevo_codigo = input("Nuevo codigo de ruta: ")
                                                    nuevo_origen = input("Nuevo lugar de origen: ")
                                                    nuevo_destino = input("Nuevo lugar de destino: ")
                                                    nueva_dis_total_k = input("Nueva distancia total de kilometros: ")
                                                    nueva_tarifa = input("Nueva tarifa por kilometro: ")

                                                    # Si queda vacio conserva el dato anterior
                                                    if nuevo_codigo == "":
                                                        nuevo_codigo = datos[0]

                                                    if nuevo_origen == "":
                                                        nuevo_origen = datos[1]

                                                    if nuevo_destino == "":
                                                        nuevo_destino = datos[2]

                                                    if nueva_dis_total_k == "":
                                                        nueva_dis_total_k = datos[3]
                                                    elif nueva_dis_total_k.isdigit() == False:
                                                        print("La distancia debe contener solamente numeros")
                                                        nueva_dis_total_k = datos[3]

                                                    if nueva_tarifa == "":
                                                        nueva_tarifa = datos[4]
                                                    elif nueva_tarifa.isdigit() == False:
                                                        print("La tarifa debe contener solamente numeros")
                                                        nueva_tarifa = datos[4]

                                                    # Verificamos que el nuevo codigo no exista
                                                    codigo_repetido = False

                                                    if nuevo_codigo != datos[0]:

                                                        with open("rutas.txt", "r") as archivo2:
                                                            linea2 = archivo2.readline()

                                                            while linea2 != "":
                                                                datos2 = linea2.strip().split(";")

                                                                if nuevo_codigo == datos2[0]:
                                                                    codigo_repetido = True

                                                                linea2 = archivo2.readline()

                                                        if codigo_repetido == True:
                                                            print("El codigo de ruta ya existe")
                                                            nuevo_codigo = datos[0]

                                                    ruta = nuevo_codigo + ";" + nuevo_origen + ";" + nuevo_destino + ";" + nueva_dis_total_k + ";" + nueva_tarifa + "\n"

                                                    nuevo += [ruta]

                                                else:
                                                    # añade la linea a nuevo 
                                                    nuevo += [linea]
                                                # sigue con la siguiente linea 
                                                linea = archivo.readline()
                                                
                                        # agrega linea por linea al archivo 
                                        with open("rutas.txt", "w") as archivo:
                                            i = 0

                                            while i < len(nuevo):
                                                archivo.write(nuevo[i])
                                                i += 1

                                        print("Ruta modificada correctamente")




                                #E: Ninguna
                                #S: muestra las rutas
                                #R: ninguna
                                #Mostrar 
                                if admin == "4":
                                     with open("rutas.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")
                                            
                                            print("------------------------------------------")
                                            print("                   RUTAS                  ")
                                            print("------------------------------------------")
                                            print("Codigo de ruta: " + datos[0])
                                            print("Lugar de origen: " + datos[1])
                                            print("Lugar de destino: " + datos[2])
                                            print("Distancia total en kilometros: " + datos[3])
                                            print("Tarifa por kilometro: " + datos[4])
                                            print("")

                                            linea = archivo.readline()

                                if admin == "5":
                                    option = "5"


                                
                        while option == "15":
                            print("")
                            print("==========================================")
                            print("        GESTION DE PARADAS POR RUTA       ")
                            print("==========================================")
                            print("(1) Incluir")
                            print("(2) Eliminar")
                            print("(3) Modificar")
                            print("(4) Mostrar")
                            print("(5) Atras")
                            print("")
                            admin = input("Digite una opcion: ")
                            print("")

                            

                           
                            #E: datos de la parada
                            #S: Parada incluida en el archivo
                            #R: La ruta debe existir, el orden no se puede repetir y los kilometros deben ser crecientes

                            if admin == "1":

                                codigo_ruta = input("Codigo de ruta: ")
                                numero_orden = input("Numero de orden: ")
                                nombre_parada = input("Nombre de la parada: ")
                                kilometro = input("Kilometro acumulado: ")

                                # valida que ningun espacio quede vacio
                                if codigo_ruta == "" or numero_orden == "" or nombre_parada == "" or kilometro == "":
                                    print("No se puede agregar la parada, ningun campo puede quedar vacio")

                                elif numero_orden.isdigit() == False or kilometro.isdigit() == False:
                                    print("El numero de orden y el kilometro deben ser numeros")

                                else:

                                    ruta_existe = False

                                    # verifica que la ruta exista
                                    with open("rutas.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            if codigo_ruta == datos[0]:
                                                ruta_existe = True

                                            linea = archivo.readline()
                                    # no lo incluye
                                    if ruta_existe == False:
                                        print("La ruta no esta registrada")

                                    else:

                                        orden_existe = False
                                        orden_anterior = 0
                                        kilometro_anterior = 0
                                        orden_siguiente = 0
                                        kilometro_siguiente = 0
                                        hay_anterior = False
                                        hay_siguiente = False
                                        hay_parada_1 = False

                                        # busca las paradas de la ruta
                                        with open("paradas.txt", "r") as archivo:
                                            linea = archivo.readline()

                                            while linea != "":
                                                datos = linea.strip().split(";")

                                                if codigo_ruta == datos[0]:

                                                    orden_actual = int(datos[1])
                                                    kilometro_actual = int(datos[3])

                                                    if numero_orden == datos[1]:
                                                        orden_existe = True

                                                    if orden_actual == 1:
                                                        hay_parada_1 = True

                                                    # busca la parada anterior
                                                    if orden_actual < int(numero_orden):
                                                        if hay_anterior == False or orden_actual > orden_anterior:
                                                            orden_anterior = orden_actual
                                                            kilometro_anterior = kilometro_actual
                                                            hay_anterior = True

                                                    # busca la parada siguiente
                                                    if orden_actual > int(numero_orden):
                                                        if hay_siguiente == False or orden_actual < orden_siguiente:
                                                            orden_siguiente = orden_actual
                                                            kilometro_siguiente = kilometro_actual
                                                            hay_siguiente = True

                                                linea = archivo.readline()

                                        if orden_existe == True:
                                            print("El numero de orden ya esta registrado")

                                        elif int(numero_orden) == 1 and int(kilometro) != 0:
                                            print("La primera parada debe tener kilometro acumulado 0")

                                        elif int(numero_orden) != 1 and hay_parada_1 == False:
                                            print("Debe existir primero la parada numero 1")

                                        elif hay_anterior == True and int(kilometro) <= kilometro_anterior:
                                            print("El kilometro debe ser mayor al de la parada anterior")

                                        elif hay_siguiente == True and int(kilometro) >= kilometro_siguiente:
                                            print("El kilometro debe ser menor al de la parada siguiente")

                                        else:

                                            parada = codigo_ruta + ";" + numero_orden + ";" + nombre_parada + ";" + kilometro

                                            # añade la parada al archivo        
                                            with open("paradas.txt", "a") as archivo:
                                                archivo.write(parada + "\n")

                                            print("Parada agregada")



                           
                           
                            #E: Codigo de ruta y numero de orden
                            #S: Archivo de paradas sin la parada seleccionada
                            #R: Las paradas siguientes deben reacomodar su numero de orden

                            if admin == "2":

                                codigo_ruta = input("Codigo de ruta: ")
                                numero_orden = input("Numero de orden de la parada a eliminar: ")

                                if codigo_ruta == "" or numero_orden == "":
                                    print("No se puede eliminar, ningun campo puede quedar vacio")

                                elif numero_orden.isdigit() == False:
                                    print("El numero de orden debe ser un numero")

                                else:

                                    existe = False
                                    nuevo = []

                                    # busca la parada que se quiere eliminar
                                    with open("paradas.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            if codigo_ruta == datos[0] and numero_orden == datos[1]:
                                                existe = True

                                            linea = archivo.readline()

                                    if existe == False:
                                        print("La parada no existe")

                                    else:

                                        # elimina la parada y acomoda las siguientes
                                        with open("paradas.txt", "r") as archivo:
                                            linea = archivo.readline()

                                            while linea != "":
                                                datos = linea.strip().split(";")

                                                if codigo_ruta == datos[0]:

                                                    if numero_orden == datos[1]:
                                                        pass

                                                    elif int(datos[1]) > int(numero_orden):
                                                        nuevo_orden = int(datos[1]) - 1

                                                        parada = datos[0] + ";" + str(nuevo_orden) + ";" + datos[2] + ";" + datos[3] + "\n"

                                                        nuevo += [parada]

                                                    else:
                                                        nuevo += [linea]

                                                else:
                                                    nuevo += [linea]

                                                linea = archivo.readline()

                                        # reescribe el archivo
                                        with open("paradas.txt", "w") as archivo:
                                            i = 0

                                            while i < len(nuevo):
                                                archivo.write(nuevo[i])
                                                i += 1

                                        print("Parada eliminada")



                           
                            #E: Codigo de ruta y numero de orden
                            #S: Archivo de paradas con los datos modificados
                            #R: El orden no se puede repetir y los kilometros deben ser crecientes
                            if admin == "3":
                                
                                codigo_ruta = input("Codigo de ruta de la parada a modificar: ")
                                numero_orden = input("Numero de orden de la parada a modificar: ")
                                
                                # validaciones 
                                if codigo_ruta == "" or numero_orden == "":
                                    print("No se puede modificar, ningun campo puede quedar vacio")

                                elif numero_orden.isdigit() == False:
                                    print("El numero de orden debe ser un numero")

                                else:

                                    existe = False

                                    # busca la parada
                                    with open("paradas.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            if codigo_ruta == datos[0] and numero_orden == datos[1]:
                                                existe = True

                                            linea = archivo.readline()
                                    # no lo modifica 
                                    if existe == False:
                                        print("La parada no existe")

                                    else:

                                        nuevo = []

                                        # valida que los datos coisidan
                                        with open("paradas.txt", "r") as archivo:
                                            linea = archivo.readline()

                                            while linea != "":
                                                datos = linea.strip().split(";")

                                                if datos[0] == codigo_ruta and datos[1] == numero_orden:

                                                    nuevo_codigo = input("Nuevo codigo de ruta: ")
                                                    nuevo_orden = input("Nuevo numero de orden: ")
                                                    nuevo_nombre = input("Nuevo nombre de la parada: ")
                                                    nuevo_kilometro = input("Nuevo kilometro acumulado: ")

                                                    # conserva los datos anteriores si quedan vacios

                                                    if nuevo_codigo == "":
                                                        nuevo_codigo = datos[0]

                                                    if nuevo_orden == "":
                                                        nuevo_orden = datos[1]

                                                    if nuevo_nombre == "":
                                                        nuevo_nombre = datos[2]

                                                    if nuevo_kilometro == "":
                                                        nuevo_kilometro = datos[3]

                                                    # verifica que la nueva ruta exista
                                                    ruta_existe = False

                                                    with open("rutas.txt", "r") as archivo_rutas:
                                                        linea_ruta = archivo_rutas.readline()

                                                        while linea_ruta != "":
                                                            datos_ruta = linea_ruta.strip().split(";")

                                                            if nuevo_codigo == datos_ruta[0]:
                                                                ruta_existe = True

                                                            linea_ruta = archivo_rutas.readline()

                                                    # no modifica y mantiene los valores anteriores 
                                                    if ruta_existe == False:
                                                        print("La ruta no esta registrada")

                                                        nuevo_codigo = datos[0]
                                                        nuevo_orden = datos[1]
                                                        nuevo_nombre = datos[2]
                                                        nuevo_kilometro = datos[3]

                                                    else:
                                                        # valida que sean numeros 
                                                        if nuevo_orden.isdigit() == False or nuevo_kilometro.isdigit() == False:
                                                            print("El numero de orden y el kilometro deben ser numeros")

                                                            nuevo_orden = datos[1]
                                                            nuevo_kilometro = datos[3]

                                                        else:

                                                            orden_repetido = False
                                                            orden_anterior = 0
                                                            kilometro_anterior = 0
                                                            orden_siguiente = 0
                                                            kilometro_siguiente = 0
                                                            hay_anterior = False
                                                            hay_siguiente = False

                                                            # busca las paradas de la nueva ruta
                                                            with open("paradas.txt", "r") as archivo_paradas:
                                                                linea_parada = archivo_paradas.readline()





                                                                while linea_parada != "":
                                                                    datos_parada = linea_parada.strip().split(";")

                                                                    if nuevo_codigo == datos_parada[0]:

                                                                        # no compara la parada que estamos modificando
                                                                        if not (codigo_ruta == datos_parada[0] and numero_orden == datos_parada[1]):

                                                                            # busca si el orden ya existe y encuentra la parada anterior y siguiente para validar los kilometros
                                                                            orden_actual = int(datos_parada[1])
                                                                            kilometro_actual = int(datos_parada[3])

                                                                            if nuevo_orden == datos_parada[1]:
                                                                                orden_repetido = True

                                                                            if orden_actual < int(nuevo_orden):
                                                                                if hay_anterior == False or orden_actual > orden_anterior:
                                                                                    orden_anterior = orden_actual
                                                                                    kilometro_anterior = kilometro_actual
                                                                                    hay_anterior = True

                                                                            if orden_actual > int(nuevo_orden):
                                                                                if hay_siguiente == False or orden_actual < orden_siguiente:
                                                                                    orden_siguiente = orden_actual
                                                                                    kilometro_siguiente = kilometro_actual
                                                                                    hay_siguiente = True

                                                                    linea_parada = archivo_paradas.readline()




                                                            # valida que el numero de orden no se repita y que los kilometros sean correctos segun las paradas anteriores y siguientes
                                                            if orden_repetido == True:
                                                                print("El numero de orden ya esta registrado")
                                                                nuevo_orden = datos[1]
                                                                nuevo_kilometro = datos[3]

                                                            elif int(nuevo_orden) == 1 and int(nuevo_kilometro) != 0:
                                                                print("La primera parada debe tener kilometro acumulado 0")
                                                                nuevo_orden = datos[1]
                                                                nuevo_kilometro = datos[3]

                                                            elif int(nuevo_orden) != 1 and hay_anterior == False:
                                                                print("Debe existir la parada numero 1")
                                                                nuevo_orden = datos[1]
                                                                nuevo_kilometro = datos[3]

                                                            elif hay_anterior == True and int(nuevo_kilometro) <= kilometro_anterior:
                                                                print("El kilometro debe ser mayor al de la parada anterior")
                                                                nuevo_orden = datos[1]
                                                                nuevo_kilometro = datos[3]

                                                            elif hay_siguiente == True and int(nuevo_kilometro) >= kilometro_siguiente:
                                                                print("El kilometro debe ser menor al de la parada siguiente")
                                                                nuevo_orden = datos[1]
                                                                nuevo_kilometro = datos[3]





                                                    parada = nuevo_codigo + ";" + nuevo_orden + ";" + nuevo_nombre + ";" + nuevo_kilometro + "\n"

                                                    nuevo += [parada]

                                                else:
                                                    nuevo += [linea]

                                                linea = archivo.readline()
                                                
                                        # lo agrega al archivo paradas.txt
                                        with open("paradas.txt", "w") as archivo:
                                            i = 0

                                            while i < len(nuevo):
                                                archivo.write(nuevo[i])
                                                i += 1

                                        print("Parada modificada")




                            #E: Ninguna
                            #S: Muestra las paradas registradas
                            #R: Ninguna
                            if admin == "4":

                                with open("paradas.txt", "r") as archivo:
                                    linea = archivo.readline()

                                    while linea != "":
                                        datos = linea.strip().split(";")

                                        print("------------------------------------------")
                                        print("                  PARADA                  ")
                                        print("------------------------------------------")
                                        print("Codigo de ruta: " + datos[0])
                                        print("Numero de orden: " + datos[1])
                                        print("Nombre de la parada: " + datos[2])
                                        print("Kilometro acumulado: " + datos[3])
                                        print("")

                                        linea = archivo.readline()

                                        
                            if admin == "5":
                                option = "5"


                                
                        while option == "16":
                            print("")
                            print("==========================================")
                            print("          PROGRAMACION DE SALIDAS         ")
                            print("==========================================")
                            print("(1) Incluir")
                            print("(2) Eliminar")
                            print("(3) Modificar")
                            print("(4) Mostrar")
                            print("(5) Atras")
                            print("")
                            admin = input("Digite una opcion: ")
                            print("")

                            if admin:



                                
                                #E: datos de la salida
                                #S: Salida incluida en el archivo
                                #R: La salida debe cumplir todas las validaciones establecidas
                                if admin == "1":

                                    codigo_ruta = input("Codigo de ruta: ")
                                    placa = input("Placa de la unidad: ")
                                    cedula = input("Cedula del conductor: ")
                                    fecha = input("Fecha: ")
                                    hora_salida = input("Hora de salida: ")
                                    hora_llegada = input("Hora estimada de llegada: ")


                                    ruta_existe = False
                                    unidad_existe = False

                                    with open("rutas.txt", "r") as archivo_rutas:
                                        linea_ruta = archivo_rutas.readline()

                                        while linea_ruta != "":
                                            datos_ruta = linea_ruta.strip().split(";")

                                            if codigo_ruta == datos_ruta[0]:
                                                ruta_existe = True

                                            linea_ruta = archivo_rutas.readline()


                                    with open("unidades.txt", "r") as archivo_unidades:
                                        linea_unidad = archivo_unidades.readline()

                                        while linea_unidad != "":
                                            datos_unidad = linea_unidad.strip().split(";")

                                            if placa == datos_unidad[0]:
                                                unidad_existe = True

                                            linea_unidad = archivo_unidades.readline()

                                    if ruta_existe == False:
                                        print("La ruta no esta registrada")

                                    elif unidad_existe == False:
                                        print("La unidad no esta registrada")

                                    else:
                                        # valida que las casillas no esten vacias 
                                        if codigo_ruta == "" or placa == "" or cedula == "" or fecha == "" or hora_salida == "" or hora_llegada == "":
                                            print("No se puede agregar la salida, ningun campo puede quedar vacio")

                                        # verifica que el formato de la fecha sea correcto
                                        elif validar_fecha(fecha) == False:
                                            print("La fecha no es valida")

                                        # valida que el formato de la hora sea correcto
                                        elif validar_hora(hora_salida) == False or validar_hora(hora_llegada) == False:
                                            print("La hora no es valida")
                                    
                                        else:
                                            # convierte las horas a minutos y verifica que la hora de llegada sea posterior a la salida
                                            minutos_salida = int(hora_salida[0] + hora_salida[1]) * 60 + int(hora_salida[3] + hora_salida[4])

                                            minutos_llegada = int(hora_llegada[0] + hora_llegada[1]) * 60 + int(hora_llegada[3] + hora_llegada[4])

                                            if minutos_llegada <= minutos_salida:
                                                print("La hora de llegada debe ser posterior a la hora de salida")

                                            else:

                                                traslape_unidad = False
                                                traslape_conductor = False

                                                # verifica que la unidad y el conductor no tengan otra salida en el mismo horario
                                                with open("salidas.txt", "r") as archivo:
                                                    linea = archivo.readline()

                                                    while linea != "":
                                                        datos = linea.strip().split(";")

                                                        if datos[4] == fecha:

                                                            otra_salida = int(datos[5][0] + datos[5][1]) * 60 + int(datos[5][3] + datos[5][4])

                                                            otra_llegada = int(datos[6][0] + datos[6][1]) * 60 + int(datos[6][3] + datos[6][4])

                                                            if placa == datos[2]:
                                                                if minutos_salida < otra_llegada and minutos_llegada > otra_salida:
                                                                    traslape_unidad = True

                                                            if cedula == datos[3]:
                                                                if minutos_salida < otra_llegada and minutos_llegada > otra_salida:
                                                                    traslape_conductor = True

                                                        linea = archivo.readline()

                                                # verifica si la unidad o el conductor tienen otra salida en ese horario
                                                if traslape_unidad == True:
                                                    print("La unidad ya tiene otra salida en ese horario")

                                                elif traslape_conductor == True:
                                                    print("El conductor ya tiene otra salida en ese horario")

                                                else:
                                                    conductor_existe = False
                                                    jornada_maxima = 0
                                                    fecha_vencimiento = ""

                                                    with open("conductores.txt", "r") as archivo_conductores:
                                                        linea_conductor = archivo_conductores.readline()

                                                        while linea_conductor != "":
                                                            datos_conductor = linea_conductor.strip().split(";")

                                                            if cedula == datos_conductor[0]:
                                                                conductor_existe = True
                                                                jornada_maxima = int(datos_conductor[4])
                                                                fecha_vencimiento = datos_conductor[3]

                                                            linea_conductor = archivo_conductores.readline()

                                                    if conductor_existe == False:
                                                        print("El conductor no esta registrado")
                                                    else:
                                                        horas_conductor = 0
                                                        
                                                        # suma las horas de las salidas del conductor en la misma fecha para verificar su jornada maxima
                                                        with open("salidas.txt", "r") as archivo:
                                                            linea = archivo.readline()

                                                            while linea != "":
                                                                datos = linea.strip().split(";")

                                                                if datos[3] == cedula and datos[4] == fecha:

                                                                    salida = int(datos[5][0] + datos[5][1]) * 60 + int(datos[5][3] + datos[5][4])

                                                                    llegada = int(datos[6][0] + datos[6][1]) * 60 + int(datos[6][3] + datos[6][4])

                                                                    horas_conductor += llegada - salida

                                                                linea = archivo.readline()

                                                        horas_conductor += minutos_llegada - minutos_salida

                                                        # verifica que el conductor no supere su jornada maxima y que su licencia no este vencida
                                                        if horas_conductor > jornada_maxima * 60:
                                                            print("El conductor supera su jornada maxima")

                                                        else:
                                                            
                                                            fecha_salida_numero = int(fecha[6] + fecha[7] + fecha[8] + fecha[9]) * 10000 + int(fecha[3] + fecha[4]) * 100 + int(fecha[0] + fecha[1])
                                                            fecha_vencimiento_numero = int(fecha_vencimiento[6] + fecha_vencimiento[7] + fecha_vencimiento[8] + fecha_vencimiento[9]) * 10000 + int(fecha_vencimiento[3] + fecha_vencimiento[4]) * 100 + int(fecha_vencimiento[0] + fecha_vencimiento[1])

                                                            if fecha_salida_numero > fecha_vencimiento_numero:
                                                                print("La licencia del conductor esta vencida")

                                                            else:
                                                                codigo_salida = "S001"
                                                                mayor = 0

                                                                # busca el numero de salida mas alto para generar el siguiente codigo automaticamente
                                                                with open("salidas.txt", "r") as archivo:
                                                                    linea = archivo.readline()

                                                                    while linea != "":
                                                                        datos = linea.strip().split(";")

                                                                        numero = int(datos[0][1:])

                                                                        if numero > mayor:
                                                                            mayor = numero

                                                                        linea = archivo.readline()

                                                                numero = mayor + 1

                                                                # genera el codigo de salida, crea el registro 
                                                                if numero < 10:
                                                                    codigo_salida = "S00" + str(numero)

                                                                elif numero < 100:
                                                                    codigo_salida = "S0" + str(numero)

                                                                else:
                                                                    codigo_salida = "S" + str(numero)

                                                                salida = codigo_salida + ";" + codigo_ruta + ";" + placa + ";" + cedula + ";" + fecha + ";" + hora_salida + ";" + hora_llegada

                                                                # lo guarda en el archivo
                                                                with open("salidas.txt", "a") as archivo:
                                                                    archivo.write(salida + "\n")

                                                                print("Salida registrada correctamente")       


                                    
                                #E: Codigo de salida
                                #S: Archivo de salidas sin la salida seleccionada
                                #R: La salida no se puede eliminar si tiene abordajes registrados
                                if admin == "2":

                                    codigo_salida = input("Codigo de salida a eliminar: ")

                                    # valida que no este vacio 
                                    if codigo_salida == "":
                                        print("No se puede eliminar, el codigo no puede quedar vacio")

                                    else:

                                        existe = False
                                        tiene_abordajes = False

                                        # verifica que lo que se busca esta en el archivo salidas.txt
                                        with open("salidas.txt", "r") as archivo:
                                            linea = archivo.readline()

                                            while linea != "":
                                                datos = linea.strip().split(";")

                                                if codigo_salida == datos[0]:
                                                    existe = True

                                                linea = archivo.readline()

                                        if existe == False:
                                            print("La salida no existe")

                                        else:

                                            # valida que el codigo no este asociado
                                            with open("abordajes.txt", "r") as archivo:
                                                linea = archivo.readline()

                                                while linea != "":
                                                    datos = linea.strip().split(";")

                                                    if codigo_salida == datos[2]:
                                                        tiene_abordajes = True

                                                    linea = archivo.readline()

                                            if tiene_abordajes == True:
                                                print("La salida tiene abordajes registrados")

                                            else:

                                                nuevo = []

                                                # agrega todas las lineas da una variable excepto la seleccionada 
                                                with open("salidas.txt", "r") as archivo:
                                                    linea = archivo.readline()

                                                    while linea != "":
                                                        datos = linea.strip().split(";")

                                                        if datos[0] != codigo_salida:
                                                            nuevo += [linea]

                                                        linea = archivo.readline()

                                                # sobre escribe el archivo con la nueva variable
                                                with open("salidas.txt", "w") as archivo:
                                                    i = 0

                                                    while i < len(nuevo):
                                                        archivo.write(nuevo[i])
                                                        i += 1

                                                print("Salida eliminada")
                                                



                                #E: Codigo de salida
                                #S: Archivo de salidas con los datos modificados
                                #R: La salida debe cumplir las mismas validaciones al modificar
                                if admin == "3":

                                    codigo_salida = input("Codigo de salida a modificar: ")

                                    # verifica que el codigo no quede vacio
                                    if codigo_salida == "":
                                        print("No se puede modificar, el codigo no puede quedar vacio")

                                    else:

                                        existe = False

                                        # busca que el codigo de salida en el archivo salida.txt
                                        with open("salidas.txt", "r") as archivo:
                                            linea = archivo.readline()

                                            while linea != "":
                                                datos = linea.strip().split(";")

                                                if codigo_salida == datos[0]:
                                                    existe = True

                                                linea = archivo.readline()

                                        # no se modifica 
                                        if existe == False:
                                            print("La salida no existe")

                                        else:

                                            nuevo = []
                                            salida_modificada = False
                                            
                                            with open("salidas.txt", "r") as archivo:
                                                linea = archivo.readline()

                                                # si el codigo de la linea es igual al seleccionado modificamos la linea 
                                                while linea != "":
                                                    datos = linea.strip().split(";")

                                                    if codigo_salida == datos[0]:

                                                        nuevo_codigo_ruta = input("Nuevo codigo de ruta: ")
                                                        nueva_placa = input("Nueva placa de la unidad: ")
                                                        nueva_cedula = input("Nueva cedula del conductor: ")
                                                        nueva_fecha = input("Nueva fecha: ")
                                                        nueva_hora_salida = input("Nueva hora de salida: ")
                                                        nueva_hora_llegada = input("Nueva hora estimada de llegada: ")

                                                        # verificamos que los datos no esten vacios, si no se conserva el anterior 
                                                        if nuevo_codigo_ruta == "":
                                                            nuevo_codigo_ruta = datos[1]

                                                        if nueva_placa == "":
                                                            nueva_placa = datos[2]

                                                        if nueva_cedula == "":
                                                            nueva_cedula = datos[3]

                                                        if nueva_fecha == "":
                                                            nueva_fecha = datos[4]

                                                        if nueva_hora_salida == "":
                                                            nueva_hora_salida = datos[5]

                                                        if nueva_hora_llegada == "":
                                                            nueva_hora_llegada = datos[6]



                                                        ruta_existe = False
                                                        unidad_existe = False
                                                        conductor_existe = False

                                                        # verifica que la nueva modificacion de la ruta exista
                                                        with open("rutas.txt", "r") as archivo_rutas:
                                                            linea_ruta = archivo_rutas.readline()

                                                            while linea_ruta != "":
                                                                datos_ruta = linea_ruta.strip().split(";")

                                                                if nuevo_codigo_ruta == datos_ruta[0]:
                                                                    ruta_existe = True

                                                                linea_ruta = archivo_rutas.readline()



                                                        # verifica que la nueva unudad se encuentre en el archivo
                                                        with open("unidades.txt", "r") as archivo_unidades:
                                                            linea_unidad = archivo_unidades.readline()

                                                            while linea_unidad != "":
                                                                datos_unidad = linea_unidad.strip().split(";")

                                                                if nueva_placa == datos_unidad[0]:
                                                                    unidad_existe = True

                                                                linea_unidad = archivo_unidades.readline()


                                                        jornada_maxima = 0
                                                        fecha_vencimiento = ""

                                                        # se verifica que la cedula del nuevo conductor exista 
                                                        with open("conductores.txt", "r") as archivo_conductores:
                                                            linea_conductor = archivo_conductores.readline()

                                                            while linea_conductor != "":
                                                                datos_conductor = linea_conductor.strip().split(";")

                                                                if nueva_cedula == datos_conductor[0]:
                                                                    conductor_existe = True
                                                                    jornada_maxima = int(datos_conductor[4])
                                                                    fecha_vencimiento = datos_conductor[3]

                                                                linea_conductor = archivo_conductores.readline()

                                                        # no va permitir modificar si alguno es verdad 
                                                        if ruta_existe == False:
                                                            print("La ruta no esta registrada")

                                                        elif unidad_existe == False:
                                                            print("La unidad no esta registrada")

                                                        elif conductor_existe == False:
                                                            print("El conductor no esta registrado")

                                                        elif validar_fecha(nueva_fecha) == False:
                                                            print("La fecha no es valida")

                                                        elif validar_hora(nueva_hora_salida) == False or validar_hora(nueva_hora_llegada) == False:
                                                            print("La hora no es valida")

                                                        else:

                                                            ## convierte las horas a minutos y verifica que la llegada sea posterior a la salida
                                                            minutos_salida = int(nueva_hora_salida[0] + nueva_hora_salida[1]) * 60 + int(nueva_hora_salida[3] + nueva_hora_salida[4])

                                                            minutos_llegada = int(nueva_hora_llegada[0] + nueva_hora_llegada[1]) * 60 + int(nueva_hora_llegada[3] + nueva_hora_llegada[4])

                                                            if minutos_llegada <= minutos_salida:
                                                                print("La hora de llegada debe ser posterior a la hora de salida")

                                                            else:

                                                                traslape_unidad = False
                                                                traslape_conductor = False
                                                                # verifica que la nueva unidad y el nuevo conductor no tengan otra salida en el mismo horario
                                                                with open("salidas.txt", "r") as archivo_salidas:
                                                                    linea_salida = archivo_salidas.readline()

                                                                    while linea_salida != "":
                                                                        datos_salida = linea_salida.strip().split(";")

                                                                        if datos_salida[0] != codigo_salida and datos_salida[4] == nueva_fecha:

                                                                            otra_salida = int(datos_salida[5][0] + datos_salida[5][1]) * 60 + int(datos_salida[5][3] + datos_salida[5][4])

                                                                            otra_llegada = int(datos_salida[6][0] + datos_salida[6][1]) * 60 + int(datos_salida[6][3] + datos_salida[6][4])

                                                                            if nueva_placa == datos_salida[2]:
                                                                                if minutos_salida < otra_llegada and minutos_llegada > otra_salida:
                                                                                    traslape_unidad = True

                                                                            if nueva_cedula == datos_salida[3]:
                                                                                if minutos_salida < otra_llegada and minutos_llegada > otra_salida:
                                                                                    traslape_conductor = True

                                                                        linea_salida = archivo_salidas.readline()




                                                                # no permite modificarlo
                                                                if traslape_unidad == True:
                                                                    print("La unidad ya tiene otra salida en ese horario")

                                                                elif traslape_conductor == True:
                                                                    print("El conductor ya tiene otra salida en ese horario")

                                                                else:

                                                                    horas_conductor = 0

                                                                    # suma las horas de las salidas del nuevo conductor en la misma fecha
                                                                    with open("salidas.txt", "r") as archivo_salidas:
                                                                        linea_salida = archivo_salidas.readline()

                                                                        while linea_salida != "":
                                                                            datos_salida = linea_salida.strip().split(";")

                                                                            if datos_salida[0] != codigo_salida and datos_salida[3] == nueva_cedula and datos_salida[4] == nueva_fecha:

                                                                                salida = int(datos_salida[5][0] + datos_salida[5][1]) * 60 + int(datos_salida[5][3] + datos_salida[5][4])

                                                                                llegada = int(datos_salida[6][0] + datos_salida[6][1]) * 60 + int(datos_salida[6][3] + datos_salida[6][4])

                                                                                horas_conductor += llegada - salida

                                                                            linea_salida = archivo_salidas.readline()




                                                                    horas_conductor += minutos_llegada - minutos_salida
                                                                    
                                                                    # verifica que el conductor no supere su jornada maxima diaria
                                                                    if horas_conductor > jornada_maxima * 60:
                                                                        print("El conductor supera su jornada maxima")

                                                                    else:

                                                                        # convierte las fechas a numeros y verifica que la licencia del conductor no este vencida
                                                                        fecha_salida_numero = int(nueva_fecha[6] + nueva_fecha[7] + nueva_fecha[8] + nueva_fecha[9]) * 10000 + int(nueva_fecha[3] + nueva_fecha[4]) * 100 + int(nueva_fecha[0] + nueva_fecha[1])

                                                                        fecha_vencimiento_numero = int(fecha_vencimiento[6] + fecha_vencimiento[7] + fecha_vencimiento[8] + fecha_vencimiento[9]) * 10000 + int(fecha_vencimiento[3] + fecha_vencimiento[4]) * 100 + int(fecha_vencimiento[0] + fecha_vencimiento[1])

                                                                        if fecha_salida_numero > fecha_vencimiento_numero:
                                                                            print("La licencia del conductor esta vencida")

                                                                        else:

                                                                            salida = codigo_salida + ";" + nuevo_codigo_ruta + ";" + nueva_placa + ";" + nueva_cedula + ";" + nueva_fecha + ";" + nueva_hora_salida + ";" + nueva_hora_llegada + "\n"

                                                                            nuevo += [salida]
                                                                            salida_modificada = True

                                                    else:
                                                        nuevo += [linea]

                                                    linea = archivo.readline()

                                            # agrega la variable al archivo; lo hace linea por linea 
                                            with open("salidas.txt", "w") as archivo:
                                                i = 0

                                                while i < len(nuevo):
                                                    archivo.write(nuevo[i])
                                                    i += 1

                                            if salida_modificada == True:
                                                print("Salida modificada correctamente")




                                #E: Ninguna
                                #S: Muestra las salidas
                                #R: Ninguna
                                if admin == "4":
                                    

                                    with open("salidas.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            print("------------------------------------------")
                                            print("                  SALIDAS                 ")
                                            print("------------------------------------------")
                                            print("Codigo:", datos[0])
                                            print("Ruta:", datos[1])
                                            print("Unidad:", datos[2])
                                            print("Conductor:", datos[3])
                                            print("Fecha:", datos[4])
                                            print("Hora de salida:", datos[5])
                                            print("Hora de llegada:", datos[6])
                                            print("------------------------------------------")
                                            print("")

                                            linea = archivo.readline()


                                if admin == "5":
                                    option = "5"



                                    
                        while option == "17":     
                            print("")
                            print("==========================================")
                            print("     CONSULTAR HISTORIAL DE ABORDAJES     ")
                            print("==========================================")
                            print("(1) Filtrar")
                            print("(5) Atras")
                            print("")
                            admin = input("Digite una opcion: ")
                            print("")

                            if admin:
                                
                                #E: Filtros de ruta, fecha de salida, rango de fechas de registro y parada de abordaje
                                #S: Lista de abordajes que cumplen con los filtros y totales de pasajeros y monto
                                #R: Los filtros pueden quedar vacios y los abordajes deben coincidir con todos los filtros ingresados
                                if admin == "1":

                                    ruta_filtro = input("Ruta: ")
                                    fecha_salida_filtro = input("Fecha de salida: ")
                                    fecha_inicio = input("Fecha inicial de registro: ")
                                    fecha_final = input("Fecha final de registro: ")
                                    parada_filtro = input("Parada de abordaje: ")

                                    total_pasajeros = 0
                                    total_monto = 0
                                    encontrados = False

                                    with open("abordajes.txt", "r") as archivo:
                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            mostrar = True

                                            # busca la informacion de la salida relacionada con el abordaje
                                            salida_encontrada = False
                                            ruta = ""
                                            fecha_salida = ""
                                            hora_salida = ""
                                            placa = ""
                                            cedula = ""

                                            with open("salidas.txt", "r") as archivo_salidas:
                                                linea_salida = archivo_salidas.readline()

                                                while linea_salida != "":
                                                    datos_salida = linea_salida.strip().split(";")

                                                    if datos[2] == datos_salida[0]:
                                                        salida_encontrada = True
                                                        ruta = datos_salida[1]
                                                        fecha_salida = datos_salida[4]
                                                        hora_salida = datos_salida[5]
                                                        placa = datos_salida[2]
                                                        cedula = datos_salida[3]

                                                    linea_salida = archivo_salidas.readline()

                                            # verifica el filtro de ruta
                                            if ruta_filtro != "":
                                                if ruta_filtro != ruta:
                                                    mostrar = False

                                            # verifica el filtro de fecha de salida
                                            if fecha_salida_filtro != "":
                                                if fecha_salida_filtro != fecha_salida:
                                                    mostrar = False

                                            # convierte las fechas de registro a numeros para compararlas
                                            if fecha_inicio != "":
                                                fecha_inicio_numero = int(fecha_inicio[6] + fecha_inicio[7] + fecha_inicio[8] + fecha_inicio[9]) * 10000 + int(fecha_inicio[3] + fecha_inicio[4]) * 100 + int(fecha_inicio[0] + fecha_inicio[1])
                                                fecha_registro_numero = int(datos[3][6] + datos[3][7] + datos[3][8] + datos[3][9]) * 10000 + int(datos[3][3] + datos[3][4]) * 100 + int(datos[3][0] + datos[3][1])

                                                if fecha_registro_numero < fecha_inicio_numero:
                                                    mostrar = False

                                            if fecha_final != "":
                                                fecha_final_numero = int(fecha_final[6] + fecha_final[7] + fecha_final[8] + fecha_final[9]) * 10000 + int(fecha_final[3] + fecha_final[4]) * 100 + int(fecha_final[0] + fecha_final[1])
                                                fecha_registro_numero = int(datos[3][6] + datos[3][7] + datos[3][8] + datos[3][9]) * 10000 + int(datos[3][3] + datos[3][4]) * 100 + int(datos[3][0] + datos[3][1])

                                                if fecha_registro_numero > fecha_final_numero:
                                                    mostrar = False

                                            # verifica el filtro de parada de abordaje
                                            if parada_filtro != "":
                                                if parada_filtro != datos[5]:
                                                    mostrar = False

                                            if mostrar == True:

                                                print("------------------------------------------")
                                                print("            HISTORIAL DE ABORDAJES       ")
                                                print("------------------------------------------")
                                                print("Identificador:", datos[0])
                                                print("Nombre:", datos[1])
                                                print("Salida:", datos[2])
                                                print("Ruta:", ruta)
                                                print("Fecha de salida:", fecha_salida)
                                                print("Hora de salida:", hora_salida)
                                                print("Unidad:", placa)
                                                print("Conductor:", cedula)
                                                print("Fecha de registro:", datos[3])
                                                print("Hora de registro:", datos[4])
                                                print("Parada de abordaje:", datos[5])
                                                print("Parada de destino:", datos[6])
                                                print("Cantidad de pasajeros:", datos[7])
                                                print("Monto cancelado:", datos[8])
                                                print("------------------------------------------")
                                                print("")

                                                total_pasajeros += int(datos[7])
                                                total_monto += int(datos[8])
                                                encontrados = True

                                            linea = archivo.readline()

                                    if encontrados == True:
                                        print("Total de pasajeros:", total_pasajeros)
                                        print("Monto total acumulado:", total_monto)
                                    else:
                                        print("No se encontraron abordajes con los filtros indicados")


                                if admin == "5":
                                    option = "5"


                                
                else:
                    linea = archivo.readline()
            else:
                if acceso == False:
                    print ("Acceso denegado")








                    
    while option == "2":
       
        print("")
        print("==========================================")
        print("              MENU DE USUARIO             ")
        print("==========================================")
        print("(21) Consulta de salidas")
        print("(22) Registro de abordaje")
        print("(23) Anulación de abordaje")
        print("(24) Regresar al menú principal")
        print("")
        admin = input("Digite una opcion: ")
        print("")


        
        #E: Filtros de ruta, origen, destino y fecha de salida
        #S: Lista de salidas que cumplen con los filtros y cantidad de espacios ocupados y disponibles
        #R: Los filtros pueden quedar vacios y las salidas deben coincidir con todos los filtros ingresados
        if admin == "21":

            print("==========================================")
            print("            CONSULTA DE SALIDAS           ")
            print("==========================================")
            ruta_filtro = input("Ruta: ")
            origen_filtro = input("Lugar de origen: ")
            destino_filtro = input("Lugar de destino: ")
            fecha_filtro = input("Fecha de salida: ")

            encontrados = False

            with open("salidas.txt", "r") as archivo:
                linea = archivo.readline()

                while linea != "":
                    datos = linea.strip().split(";")

                    codigo_salida = datos[0]
                    codigo_ruta = datos[1]
                    placa = datos[2]
                    fecha = datos[4]
                    hora_salida = datos[5]
                    hora_llegada = datos[6]

                    mostrar = True

                    origen = ""
                    destino = ""
                    tarifa = 0

                    # busca la informacion de la ruta
                    with open("rutas.txt", "r") as archivo_rutas:
                        linea_ruta = archivo_rutas.readline()

                        while linea_ruta != "":
                            datos_ruta = linea_ruta.strip().split(";")

                            if codigo_ruta == datos_ruta[0]:
                                origen = datos_ruta[1]
                                destino = datos_ruta[2]

                            linea_ruta = archivo_rutas.readline()

                    # verifica el filtro de ruta
                    if ruta_filtro != "":
                        if ruta_filtro != codigo_ruta:
                            mostrar = False

                    # verifica el filtro de origen
                    if origen_filtro != "":
                        if origen_filtro != origen:
                            mostrar = False

                    # verifica el filtro de destino
                    if destino_filtro != "":
                        if destino_filtro != destino:
                            mostrar = False

                    # verifica el filtro de fecha
                    if fecha_filtro != "":
                        if fecha_filtro != fecha:
                            mostrar = False

                    # busca la capacidad de la unidad
                    capacidad = 0

                    with open("unidades.txt", "r") as archivo_unidades:
                        linea_unidad = archivo_unidades.readline()

                        while linea_unidad != "":
                            datos_unidad = linea_unidad.strip().split(";")

                            if placa == datos_unidad[0]:
                                modelo = datos_unidad[1]

                                with open("modelos.txt", "r") as archivo_modelos:
                                    linea_modelo = archivo_modelos.readline()

                                    while linea_modelo != "":
                                        datos_modelo = linea_modelo.strip().split(";")

                                        if modelo == datos_modelo[0]:
                                            asientos = int(datos_modelo[2])
                                            espacios_pie = int(datos_modelo[3])
                                            capacidad = asientos + espacios_pie

                                        linea_modelo = archivo_modelos.readline()

                            linea_unidad = archivo_unidades.readline()

                    # cuenta los pasajeros registrados en la salida
                    ocupados = 0

                    with open("abordajes.txt", "r") as archivo_abordajes:
                        linea_abordaje = archivo_abordajes.readline()

                        while linea_abordaje != "":
                            datos_abordaje = linea_abordaje.strip().split(";")

                            if codigo_salida == datos_abordaje[2]:
                                ocupados += int(datos_abordaje[7])

                            linea_abordaje = archivo_abordajes.readline()

                    disponibles = capacidad - ocupados

                    if mostrar == True:

                        print("------------------------------------------")
                        print("            CONSULTA DE SALIDAS           ")
                        print("------------------------------------------")
                        print("Numero de salida:", codigo_salida)
                        print("Ruta:", codigo_ruta)
                        print("Lugar de origen:", origen)
                        print("Lugar de destino:", destino)
                        print("Fecha:", fecha)
                        print("Hora de salida:", hora_salida)
                        print("Hora estimada de llegada:", hora_llegada)
                        print("Placa de la unidad:", placa)
                        print("Capacidad total:", capacidad)
                        print("Espacios ocupados:", ocupados)
                        print("Espacios disponibles:", disponibles)
                        print("------------------------------------------")
                        print("")

                        encontrados = True

                    linea = archivo.readline()

            if encontrados == False:
                print("No se encontraron salidas con los filtros indicados")



                
        #E: Numero de salida, nombre, fecha y hora de registro, paradas y cantidad de pasajeros
        #S: Registro del abordaje guardado en abordajes.txt y comprobante mostrado al usuario
        #R: La salida y las paradas deben existir, el destino debe ser posterior al abordaje y no se puede superar la capacidad
        if admin == "22":

            print("==========================================")
            print("            REGISTRO DE ABORDAJE          ")
            print("==========================================")
            codigo_salida = input("Numero de salida: ")
            nombre = input("Nombre del pasajero: ")
            fecha_registro = input("Fecha de registro: ")
            hora_registro = input("Hora de registro: ")
            parada_abordaje = input("Numero de parada de abordaje: ")
            parada_destino = input("Numero de parada de destino: ")
            cantidad = input("Cantidad de pasajeros: ")

            if codigo_salida == "" or nombre == "" or fecha_registro == "" or hora_registro == "" or parada_abordaje == "" or parada_destino == "" or cantidad == "":
                print("No se puede registrar el abordaje, ningun campo puede quedar vacio")

            elif validar_fecha(fecha_registro) == False:
                print("La fecha no es valida")

            elif validar_hora(hora_registro) == False:
                print("La hora no es valida")

            elif cantidad.isdigit() == False:
                print("La cantidad de pasajeros no es valida")

            elif int(cantidad) < 1:
                print("La cantidad de pasajeros debe ser mayor que cero")

            else:

                salida_existe = False
                ruta = ""
                fecha_salida = ""
                hora_salida = ""
                placa = ""

                # busca la salida seleccionada
                with open("salidas.txt", "r") as archivo:
                    linea = archivo.readline()

                    while linea != "":
                        datos = linea.strip().split(";")

                        if codigo_salida == datos[0]:
                            salida_existe = True
                            ruta = datos[1]
                            placa = datos[2]
                            fecha_salida = datos[4]
                            hora_salida = datos[5]

                        linea = archivo.readline()

                if salida_existe == False:
                    print("La salida no existe")

                else:

                    parada_abordaje_existe = False
                    parada_destino_existe = False
                    km_abordaje = 0
                    km_destino = 0
                    orden_abordaje = 0
                    orden_destino = 0

                    # busca las paradas de la ruta seleccionada
                    with open("paradas.txt", "r") as archivo:
                        linea = archivo.readline()

                        while linea != "":
                            datos = linea.strip().split(";")

                            if datos[0] == ruta:

                                if datos[1] == parada_abordaje:
                                    parada_abordaje_existe = True
                                    orden_abordaje = int(datos[1])
                                    km_abordaje = int(datos[3])

                                if datos[1] == parada_destino:
                                    parada_destino_existe = True
                                    orden_destino = int(datos[1])
                                    km_destino = int(datos[3])

                            linea = archivo.readline()

                    if parada_abordaje_existe == False:
                        print("La parada de abordaje no existe")

                    elif parada_destino_existe == False:
                        print("La parada de destino no existe")

                    elif orden_destino <= orden_abordaje:
                        print("La parada de destino debe ser posterior a la parada de abordaje")

                    else:

                        capacidad = 0

                        # busca la capacidad de la unidad
                        with open("unidades.txt", "r") as archivo:
                            linea = archivo.readline()

                            while linea != "":
                                datos = linea.strip().split(";")

                                if datos[0] == placa:
                                    modelo = datos[1]

                                    with open("modelos.txt", "r") as archivo_modelos:
                                        linea_modelo = archivo_modelos.readline()

                                        while linea_modelo != "":
                                            datos_modelo = linea_modelo.strip().split(";")

                                            if datos_modelo[0] == modelo:
                                                asientos = int(datos_modelo[2])
                                                espacios_pie = int(datos_modelo[3])
                                                capacidad = asientos + espacios_pie

                                            linea_modelo = archivo_modelos.readline()

                                linea = archivo.readline()

                        ocupados = 0

                        # suma los pasajeros que ya estan registrados en la salida
                        with open("abordajes.txt", "r") as archivo:
                            linea = archivo.readline()

                            while linea != "":
                                datos = linea.strip().split(";")

                                if datos[2] == codigo_salida:
                                    ocupados += int(datos[7])

                                linea = archivo.readline()

                        if ocupados + int(cantidad) > capacidad:
                            print("La cantidad de pasajeros supera la capacidad disponible")

                        else:

                            distancia = km_destino - km_abordaje
                            tarifa = 0

                            # busca la tarifa de la ruta
                            with open("rutas.txt", "r") as archivo:
                                linea = archivo.readline()

                                while linea != "":
                                    datos = linea.strip().split(";")

                                    if datos[0] == ruta:
                                        tarifa = int(datos[4])

                                    linea = archivo.readline()

                            monto = tarifa * distancia * int(cantidad)

                            # busca el numero de abordaje mas alto para generar el siguiente codigo
                            mayor = 0

                            with open("abordajes.txt", "r") as archivo:
                                linea = archivo.readline()

                                while linea != "":
                                    datos = linea.strip().split(";")

                                    numero = int(datos[0][1:])

                                    if numero > mayor:
                                        mayor = numero

                                    linea = archivo.readline()

                            numero = mayor + 1

                            if numero < 10:
                                identificador = "A00" + str(numero)

                            elif numero < 100:
                                identificador = "A0" + str(numero)

                            else:
                                identificador = "A" + str(numero)

                            registro = identificador + ";" + nombre + ";" + codigo_salida + ";" + fecha_registro + ";" + hora_registro + ";" + parada_abordaje + ";" + parada_destino + ";" + cantidad + ";" + str(monto)

                            with open("abordajes.txt", "a") as archivo:
                                archivo.write(registro + "\n")

                            print("------------------------------------------")
                            print("          COMPROBANTE DE ABORDAJE        ")
                            print("------------------------------------------")
                            print("Identificador:", identificador)
                            print("Nombre:", nombre)
                            print("Fecha de registro:", fecha_registro)
                            print("Hora de registro:", hora_registro)
                            print("Numero de salida:", codigo_salida)
                            print("Ruta:", ruta)
                            print("Unidad:", placa)
                            print("Parada de abordaje:", parada_abordaje)
                            print("Parada de destino:", parada_destino)
                            print("Cantidad de pasajeros:", cantidad)
                            print("Monto cancelado:", monto)
                            print("------------------------------------------")


                    

        #E: Identificador del abordaje
        #S: Archivo abordajes.txt sin el abordaje seleccionado
        #R: El identificador debe existir para poder eliminar el abordaje
        if admin == "23":

            print("==========================================")
            print("           ANULACION DE ABORDAJE          ")
            print("==========================================")
            identificador = input("Identificador del abordaje: ")

            if identificador == "":
                print("No se puede anular, el identificador no puede quedar vacio")

            else:

                existe = False

                # verifica que el abordaje exista
                with open("abordajes.txt", "r") as archivo:
                    linea = archivo.readline()

                    while linea != "":
                        datos = linea.strip().split(";")

                        if identificador == datos[0]:
                            existe = True

                        linea = archivo.readline()

                if existe == False:
                    print("El abordaje no existe")

                else:

                    nuevo = []

                    # guarda todos los abordajes excepto el seleccionado
                    with open("abordajes.txt", "r") as archivo:
                        linea = archivo.readline()

                        while linea != "":
                            datos = linea.strip().split(";")

                            if datos[0] != identificador:
                                nuevo += [linea]

                            linea = archivo.readline()

                    # reemplaza el archivo con los registros restantes
                    with open("abordajes.txt", "w") as archivo:
                        i = 0

                        while i < len(nuevo):
                            archivo.write(nuevo[i])
                            i += 1

                    print("Abordaje anulado correctamente")

                
        if admin == "24":
            option = "24"







