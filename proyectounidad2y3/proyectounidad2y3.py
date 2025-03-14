import MisClases.ClaseVehiculoDeCarga as clase


#declaramos una variable para que este fija para el while
z=True
x=True
#creamos el while
while(z):

    #ponemos la pregunta inicial
    print("\n********************************************")
    print("********************************************")
    print("******************\033[1mMENU\033[0m**********************")
    print("********************************************")
    print("********************************************\n")

    print("\033[1m         ¿Qué desea hacer?\033[0m",end="\n\n")

    #damos las opciones del menu
    print("\033[1m1._\033[0minstanciar un objeto ",end="\n\n")
    print("\033[1m2._\033[0mdesplegar",end="\n\n")
    print("\033[1m3._\033[0mmodificar sets",end="\n\n")
    print("\033[1m4._\033[0mmostrar gets",end="\n\n")
    print("\033[1m5._\033[0msalir ",end="\n\n")

    #creamos una variable la cual tendra el valor de los menus
    f=input("\033[1m¿Cual de todos desea hacer?\033[0m\n")
    a=f.lower()
    #empecemos los condicionales y si es necesario pondremos un rango
    try:
        if a=="instanciar un objeto":
            print("vamos a instanciar el objeto\n")
            vehiculo=clase.VehiculoDeCarga(0,"Torton","joivtr",300,40,30.6)
            numerov=int(input("Ingrese el número del vehículo: "))
            tipo = input("Ingrese el tipo del vehículo: ")
            placas=input("Ingrese las placas del vehículo: ")
            capmax=float(input("Ingrese la capacidad máxima del vehículo: "))
            pesoproducto = float(input("Ingrese el peso del producto: "))
            pesota=float(input("Ingrese el peso del vehículo:"))
            vehiculouser=clase.VehiculoDeCarga(numerov,tipo, placas, capmax,pesoproducto,pesota)
            print("Los objetos se instanciaron con exito!")
        elif a=="desplegar":

            print("despleguemos el objeto\n")
            print(vehiculo)
            print(vehiculouser)

        elif a=="modificar sets":
            print("modifiquemos los sets")
            x=True
            while(x):
                #ponemos la pregunta inicial
                print("¿Qué set en especifico desea modificar?",end="\n\n")
                #damos las opciones del menu
                print("número de vehículo",end="\n\n")
                print("tipo",end="\n\n")
                print("placas",end="\n\n")
                print("capacidad máxima bruta",end="\n\n")
                print("peso del producto",end="\n\n")
                print("peso tara ",end="\n\n")

             #creamos una variable la cual tendra el valor de los menus
                e=input("¿Cual de todos desea hacer?\n")
                d=e.lower()
                if d=="número de vehículo":
                    #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                    numerove=int(input("Ingrese el nuevo número del vehículo:"))
                    vehiculouser.set_numero_de_vehiculo(numerove)
                    x=False
                    print("Se modifico el número de vehículo!")
                elif d=="tipo":
                    #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                    tipon = input("Ingrese el nuevo tipo de vehículo:")
                    vehiculouser.set_tipo(tipon)
                    x = False
                    print("Se modifico el tipo de vehículo!")
                elif d=="placas":
                    #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                    placasn = input("Ingrese la nueva placa del vehículo:")
                    vehiculouser.set_placas(placasn)
                    x = False
                    print("Se modifico la placa del vehículo!")
                elif d=="capacidad máxima bruta":
                    #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                    capmaxn = float(input("Ingrese la nueva capacidad máxima bruta del vehículo:"))
                    vehiculouser.set_capmax(capmaxn)
                    x = False
                    print("Se modifico la capacidad máxima bruta del vehículo!")
                elif d=="peso del producto":
                    #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                    pesoproducton = float(input("Ingrese el nuevo peso del producto del vehículo:"))
                    vehiculouser.set_peso_del_producto(pesoproducton)
                    x = False
                    print("Se modifico el peso del producto del vehículo!")
                elif d=="peso tara":
                    #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                    pesotaran = float(input("Ingrese el nuevo peso del vehículo:"))
                    vehiculouser.set_peso_tara(pesotaran)
                    x = False
                    print("Se modifico el peso del vehículo!")
                else:
                    #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                    print(d,"no esta tal cual en el menú favor de rectificar y escribirlo de una manera que lo entienda")
                    x=True
        elif a=="mostrar gets":
            x=True
            print("mostrar gets")
            while(x):
                #ponemos la pregunta inicial
                print("¿Qué get en especifico desea mostrar?",end="\n\n")

                #damos las opciones del menu
                print("número de vehículo",end="\n\n")
                print("tipo",end="\n\n")
                print("placas",end="\n\n")
                print("capacidad máxima bruta",end="\n\n")
                print("peso del producto",end="\n\n")
                print("peso tara ",end="\n\n")

                #creamos una variable la cual tendra el valor de los menus
                e=input("¿Cual de todos desea hacer?\n")
                d=e.lower()
                if d=="número de vehículo":
                    #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                    print("El número de vehículo es:",vehiculouser.get_numero_de_vehiculo())
                    x=False
                elif d=="tipo":
                    #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                    print("El tipo de vehículo es:", vehiculouser.get_tipo())
                    x=False
                elif d=="placas":
                    #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                    print("La placa del vehículo es:", vehiculouser.get_placas())
                    x=False
                elif d=="capacidad máxima bruta":
                    #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                    print("La capacidad maxima bruta del vehículo es:", vehiculouser.get_capmax())
                    x=False
                elif d=="peso del producto":
                    #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                    print("El peso del producto del vehículo es:", vehiculouser.get_peso_del_producto())
                    x=False
                elif d=="peso tara":
                    #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                    print("El peso del vehículo es:", vehiculouser.get_peso_tara())
                    x=False
                else:
                    #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                    print(d,"no esta tal cual en el menú favor de rectificar y escribirlo de una manera que lo entienda")
                    x=True

        elif a=="salir":
            print("muchas gracias por el tiempo\n")
            z=False

        else:
            print("escriba de forma correcta las letras de la palabra\n")
    except NameError:
        print("No se puede realizar esta acción por que los objetos aún no han sido instanciados. ")
    except ValueError:
        print("No se puede realizar esta acción por que el valor es incorrecto. ")
