option = ""
admin = ""

#E: Ninguna
#S: Uno de los dos menús adjuntos
#R: Debe ingresar "1, 2 o 3" como opciones unicas

while option != "3":
    print("")
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
        
                        if option == "11":
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

                            if admin != "5":

                                #E: modelo
                                #S: Modelo incluido en el archivo
                                #R: La descripcion del modelo no se puede repetir 
                                #Incluir 
                                if admin == "1":
                                    
                                    descripcion_del_modelo = input("Descripción del modelo: ")
                                    marca                  = input("Marca: ")
                                    cantidad_de_asientos   = input("Cantidad de asientos: ")
                                    cantidad_espacios_pie  = input("Cantidad de espacios de pie: ")

                                    modelo                 = descripcion_del_modelo + ";" + marca + ";" + cantidad_de_asientos + ";" + cantidad_espacios_pie

                                    existe = False

                                    # agrega una nueva linea al archivo mientras no haya una descripcion de modelo igual
                                    with open("modelos.txt", "r") as archivo:

                                        linea = archivo.readline()

                                        while linea != "":
                                            datos = linea.strip().split(";")

                                        if datos[0] == descripcion_del_modelo:
                                            print("Ya esta agregado")
                                            existe = True

                                        linea = archivo.readline()
                                        
                                    with open("modelos.txt", "a") as archivo:
                                        archivo.write(modelo + "\n")


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

                                                if datos[1] != descripcion_del_modelo:
                                                    nuevo += [linea]

                                                linea = archivo.readline()
                                        # añade linea por linea en modelo.txt 
                                        with open("modelos.txt", "w") as archivo:
                                            i= 0

                                            while i < len(nuevo):
                                                archivo.write(nuevo[i])
                                                posicion += 1

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

                                            print("")
                                            print("==========================================")
                                            print("             MODELO DE AUTOBUS            ")
                                            print("==========================================")
                                            print("Descripcion: " + datos[0])
                                            print("Marca: " + datos[1])
                                            print("Cantidad de asientos: " + datos[2])
                                            print("Cantidad de espacios de pie: " + datos[3])
                                            print("")

                                            linea = archivo.readline()
                                                                

                        #E: option 12
                        #S: Una de las opciones validas "1, 2, 3, 4 o 5"
                        #R: Solo se deben ingresar opciones permitidas del menú   
                        if option == "12":
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

                            if admin != "5":
                                if admin == "1":
                                    pass

                                if admin == "2":
                                    pass

                                if admin == "3":
                                    pass

                                if admin == "4":
                                    pass
                                
                        if option == "13":
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

                            if admin != "5":
                                if admin == "1":
                                    pass

                                if admin == "2":
                                    pass

                                if admin == "3":
                                    pass

                                if admin == "4":
                                    pass
                                
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







