biografia = """
Mi nombre es Rodrigo Rosario Cruz, naci en sucre y actualmene resido en el, 
pertenezco ala carrera de ingenieria en ciencias de la computacion , 
curso el 5to semestre de mi carrera, tengo 21 años, y este semestre me toca ver inteligencia artificial 1 
                  """ ;
while (True):

    print("""MENU OPCIONES:
1.- Imprimir biografia:
2.- Salir:
            """)
    opcion = int(input("Digite una opcion: "))

    if(opcion == 1):
        print(biografia)
    elif (opcion == 2):
        quit()
    else:
        print("no existe esa opcion vuelva a elegir una opcion del menu que se muestra");



