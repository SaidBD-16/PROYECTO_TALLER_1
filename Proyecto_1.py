option = ""
while option != "3":
    print("")
    print("(1) Opciones Administrativas")
    print("(2) Opciones de Usuario")
    print("(3) Salir")
    print("")
    option = input("Digite una opcion: ")
    print("")

    if option == "1":

        usuario = input("Usuario:")
        contraseña = input("contraseña:")
        datos = usuario + ";" + contraseña

        with open("acceso.txt", "r") as archivo:
            linea = archivo.readline()

            acceso = False
            while linea != "":  
                linea = linea.strip()
                
                if datos == linea:
                    print("Acceso concedido")
                    acceso = True 
                    linea = ""
                      
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

                        if option == "11":
                            pass
                        elif option == "12":
                            pass         
                        elif option == "13":
                            pass
                        elif option == "14":
                            pass
                        elif option == "15":
                            pass
                        elif option == "16":
                            pass
                        elif option == "17":     
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







