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
    print("\033[1m3._\033[0mmodificar gets",end="\n\n")
    print("\033[1m4._\033[0mmostrar sets",end="\n\n")
    print("\033[1m5._\033[0msalir ",end="\n\n")

    #creamos una variable la cual tendra el valor de los menus
    f=input("\033[1m¿Cual de todos desea hacer?\033[0m\n")
    a=f.lower()
    #empecemos los condicionales y si es necesario pondremos un rango
    if a=="instanciar un objeto":
        print("vamos a instanciar el objeto\n")

    elif a=="desplegar":
        print("despleguemos el objeto\n")


    elif a=="modificar gets":
        print("modifiquemos los gets")
        x=True
        while(x):
            #ponemos la pregunta inicial
            print("¿Qué get en especifico desea modificar?",end="\n\n")
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
                print(d)
                x=False
            elif d=="tipo":
                #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                print(d)
                x=False
            elif d=="placas":
                #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                print(d)
                x=False
            elif d=="capacidad máxima bruta":
                #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                print(d)
                x=False
            elif d=="peso del producto":
                #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                print(d)
                x=False
            elif d=="peso tara":
                #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                print(d)
                x=False
            else:
                #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                print(d,"no esta tal cual en el menu favor de rectificar y escribirlo de una manera que lo entienda")
                x=True

    elif a=="mostrar sets":
        x=True
        print("mostrar sets")
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
                print(d)
                x=False
            elif d=="tipo":
                #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                print(d)
                x=False
            elif d=="placas":
                #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                print(d)
                x=False
            elif d=="capacidad maxima bruta":
                #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                print(d)
                x=False
            elif d=="peso del producto":
                #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                print(d)
                x=False
            elif d=="peso tara":
                #aqui ponen el metodo para modificary borran el print(es para que no de error el if)
                print(d)
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

