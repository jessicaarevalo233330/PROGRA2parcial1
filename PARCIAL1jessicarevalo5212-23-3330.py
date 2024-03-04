''' 
Elabore un programa para elaborar un menú, con el cual se manejará las notas de un curso. 
Los datos son, carné (numérico), Nombre y nota. 
Las opciones del menú son: 
a. Agregar una persona con su nota, 
b. Modificar la nota de una persona, 
c. Consultar la nota de una persona. 

Utilice listas de diccionarios.
'''
#importamos para estilizar el programa
from os import system
Todos_los_alumnos=[]
def menu():
    #al llamar a la funcion se imprime el panel
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("Bienvenido al control de notas de alumnos")
    print("seleccione una opcion segun sea el numero:")
    print("\n1.- Agregar una persona con su nota")
    print("2.- Modificar la nota de un alumno")
    print("3.- Consultar la nota de un alumno ")
    print("4.- Salir ")
    #se pide la funcion, si no se da un numero, devuelve 0, y si da un numero se convierte a entero
    try:
        opcion=int(input())
        return opcion
    except ValueError:
        return 0

def agregar():
    #se inicia con un ciclo para que no se reinicie al panel principal
    while True:
        #iniciamos con un diccionario
        datos_estudiante={'CARNE':0,'NOMBRE':'','NOTA': 0.0}
        carnet=input("Escribe el numero de carnet: ")
        #despues de pedir el carnet se verifica si es un numero, se convierte a entero
        try:
            carnet=int(carnet)
            #antes de continuar se busca que no este repetido en donde estan todos los alumnos
            if any(alumno['CARNE'] ==carnet for alumno in Todos_los_alumnos):
                print("Ya existe este carnet en los registros")
            else:
                #se le da continuidad al no haber repeticiones
                datos_estudiante["CARNE"]=carnet
                nombre=input("Ingresa el nombre completo del estudiante: ")
                nombre=nombre.upper()
                datos_estudiante["NOMBRE"]=nombre
                #se hace otro ciclo para pedir la nota, que sea un numero y no una cadena, asi registrarlo en el dato del estudiante
                while True:
                    try:
                        nota=float(input("Ingrese la nota del estudiante: "))
                        datos_estudiante["NOTA" ]=nota
                        break
                    except ValueError:
                        print ("se solicitan numeros")
                return datos_estudiante
            #se rompe el ciclo al cumplirse los requisitos
            break
        except ValueError:
            print("\nintentelo de nuevo se solicitan numeros")

def modificar():
    if not Todos_los_alumnos:
        print("No hay alumnos registrados")
    else:
        #se hace un ciclo para no repetir el panel principal al no registrar numeros
        while True:
            carnet=input("ingrese el carnet a buscar: ")
            try:
                carnet=int(carnet)
                busqueda= False
                #como vamos a buscar, creamos un ciclo for para revisar cada alumno en la lista de todos los alumnos
                for alumnito_a_buscar in Todos_los_alumnos:
                    #si encuentra el carnet lo marca como buscado
                    if alumnito_a_buscar[ "CARNE" ]==carnet:
                        busqueda=True
                        #registramos los datos originales del alumno
                        su_nombre=alumnito_a_buscar[ 'NOMBRE' ]
                        nota_actual=alumnito_a_buscar[ "NOTA" ]
                        #realizamos otro ciclo para que se ingresen floats y no cadenas para modificar los datos originales
                        while True:
                            try:
                                dato_a_modificar=float(input("Digite la nueva nota: "))
                                alumnito_a_buscar["NOTA"]=dato_a_modificar
                                #se rompe este segundo ciclo al cumplir los requisitos
                                break
                            except ValueError:
                                print("Solo se permiten numeros" )
                        #imprimimos los datos actualizados y originales
                        print("la nota de ",su_nombre ,"cambio de",nota_actual," a ",dato_a_modificar)
                        return
                #si el carnet no esta, la busqueda es falsa e imprime un mensaje
                if not busqueda:
                    print("el carnet ",carnet, " no existe en los registros")
                #se rompe el primer ciclo al cumplirse el ingreso de un carnet registrado
                else: break    
                
            except ValueError:
                print ("Intenta otra vez, se solicitan numeros")

def mostrar_nota():
    if not Todos_los_alumnos:
        print("Aun no hay nadie en el registro")
        return
    else:
        #se hace un ciclo para no copiar el menu cuando no se ingresan numeros
        while True:
            estudiante = input("Ingrese el carne del alumno: ")
            #se intenta  convertir a entero, si no hay error
            try:
                estudiante = int (estudiante)
                encontrado = False
                #en la variable name se va pasando a todos los alumnos
                for name in Todos_los_alumnos:
                    #especificamos que buscamos y si se cumple  muestra la informacion
                    if name['CARNE']==estudiante:
                        #aqui se dice que si se encontro y copia los nados del alumno que coincidio con el carnet dado
                        encontrado=True
                        nombre=name['NOMBRE']
                        nota=name['NOTA']
                        nume=name['CARNE'] 
                        print(nombre,"con el carnet no: ",nume," tiene una nota de", nota)
                        #rompe el ciclo for para no seguir buscando alumnos
                        break
                #si no se encuentra nadie entonces--   
                if not encontrado:   
                    print("ese CARNET     no esta registrado")
                #sale del bucle while al haber ingresado un carnet de alumno que este registrado
                else: break  
            except ValueError:
                print("Se solicitan numeros")
   
    
#-----------------------------------------------
#como las anteriores funciones no se ejecutan al no ser llamadas se hace un ciclo para llamarlas
while True:
    #para ir limpiando pantalla
    system('cls')
    opcion_menu=menu()
    #se registra la opcion y se busca una coincidencia
    print("■■■■■■■■■■ ■■■■■■■■■■")
    if  opcion_menu==0:
        print("\nSe solicitan numeros, intenta de nuevo ☺ ")
    elif opcion_menu==1:
        #llama a la funcion agregar() y recibe el diccionario de datos que inserta en la lista de Todos_los_alumnos
        registrar=agregar()
        #condicional si y solo si "registrar" tiene datos
        if registrar!=None:
            Todos_los_alumnos.append(registrar)
            print("\nRegistro exitoso")
    elif opcion_menu ==2:
        #no recibe datos de la funcion, solo hace que se ejecute
        modificar()
    elif  opcion_menu==3:
        #solo ejecuta la funcion mostrar_nota()
        mostrar_nota()
    elif opcion_menu==4:
        #opcion extra para terminar el ciclo  while y finalizar el programaa
        print("Gracias por  usar este sistema\n ☺")
        break
#por si el usuario  pone algo que no es una opcion valida
    else:
        print("la opcion que pide no existe")
    #para que el programa se vea mas limpio
    system('pause')