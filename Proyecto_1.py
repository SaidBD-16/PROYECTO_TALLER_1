option = ""
admin = ""

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
                                    marca                  = input("Marca: ")
                                    cantidad_de_asientos   = input("Cantidad de asientos: ")
                                    cantidad_espacios_pie  = input("Cantidad de espacios de pie: ")

                                    modelo = descripcion_del_modelo + ";" + marca + ";" + cantidad_de_asientos + ";" + cantidad_espacios_pie 

                                    existe = False

                                    # agrega una nueva linea al archivo mientras no haya una descripcion de modelo igual
                                    with open("modelos.txt", "r") as archivo:

                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                            if datos[0] == descripcion_del_modelo:
                                                existe = True

                                            linea = archivo.readline()
                                            
                                    if existe == True:
                                        print("Ya esta incluido")
                                    else:
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
                                
                        if option == "14":
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

                            if admin != "5":
                                if admin == "1":
                                    pass

                                if admin == "2":
                                    pass

                                if admin == "3":
                                    pass

                                if admin == "4":
                                    pass
                        if option == "15":
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

                            if admin != "5":
                                if admin == "1":
                                    pass

                                if admin == "2":
                                    pass

                                if admin == "3":
                                    pass

                                if admin == "4":
                                    pass
                                
                        if option == "16":
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

                            if admin != "5":
                                if admin == "1":
                                    pass

                                if admin == "2":
                                    pass

                                if admin == "3":
                                    pass

                                if admin == "4":
                                    pass
                            
                        if option == "17":     
                            print("")
                            print("==========================================")
                            print("     CONSULTAR HISTORIAL DE ABORDAJES     ")
                            print("==========================================")
                            print("(1) Incluir")
                            print("(2) Eliminar")
                            print("(3) Modificar")
                            print("(4) Mostrar")
                            print("(5) Atras")
                            print("")
                            admin = input("Digite una opcion: ")
                            print("")

                            if admin != "5":
                                if admin == "1":
                                    pass

                                if admin == "2":
                                    pass

                                if admin == "3":
                                    pass

                                if admin == "4":
                                    pass
                                
                else:
                    linea = archivo.readline()
            else:
                if acceso == False:
                    print ("Acceso denegado")
                    
    elif option == "2":
        while option != "24":
            print("")
            print("(21) Consulta de salidas")
            print("(22) Registro de abordaje")
            print("(23) Anulación de abordaje")
            print("(24) Regresar al menú principal")
            print("")
            option = input("Digite una opcion: ")
            print("")

            if option == "21":
                pass
            elif option == "22":
                pass
            elif option == "23":
                pass







