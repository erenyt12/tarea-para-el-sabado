mi_lista = []

print(type(mi_lista))

ciudad_1= input("ingrese la primer ciudad: ")
ciudad_2 = input("ingrese la segunda ciudad: ")
ciudad_3 = input("ingrese la tercer ciudad: ")
ciudad_4 = input("ingrese la cuarta ciudad: ")

tuple = (ciudad_1, ciudad_2, ciudad_3, ciudad_4)

#print(tuple)

ciudad_1, ciudad_2, ciudad_3, ciudad_4 = tuple

print ("se mostratan su primera ciudad ingresada y la ultima: ")
print(ciudad_1,  ciudad_4)

datos_de_su_circulo = float(input("ingrese el radio de su circulo para calcular el area: "))

area = datos_de_su_circulo * 3.14

resultado_de_area = round(area,2)

print("su area es: ",resultado_de_area)

mi_lista.insert(0, input("ingrese  el primer numero: "))

mi_lista.insert(1, input("ingrese  el segundo numero: "))

mi_lista.insert(2, input("ingrese  el tercer numero: "))

mi_lista.insert(3, input("ingrese  el cuarto numero: "))

mi_lista.insert(4, input("ingrese  el quinto numero: "))

mi_lista.insert(5, input("ingrese  el sexto numero: "))

mi_lista.insert(6, input("ingrese  el septimo numero: "))

for i in mi_lista:
    print(i)

dict_1 = {input("nombre de usuario: "): input("dni: "), input("nombre de usuario: "): input("dni: "), input("nombre de usuario: "): input("dni: "), input("nombre de usuario: "): input("dni: "), input("nombre de usuario: "): input("dni: ")} 

#print(dict_1)

print('''Menú
     1- Mostrar los números de la lista
     2- Mostrar ciudades    
     3- Calcular el área de un círculo
     4- Agregar número a la lista y        mostrar los números distintos
     5- Agregar usuario y DNI 
     6- Buscar usuario por nombre e imprimir su DNI
     7- Salir del sistema''')

   

continuar = True
while continuar:
    opcion = input("elija una opcion: ")
    
    if opcion == '1':
        for i in mi_lista:
             print(i)
    elif opcion == '2':
        print(ciudad_1, ciudad_2, ciudad_3, ciudad_4)
    elif opcion == '3':
        datos_de_su_circulo = float(input("ingrese el radio de su circulo para calcular el area: "))
        area = datos_de_su_circulo * 3.14
        resultado_de_area = round(area,2)
        print("su area es: ",resultado_de_area)
    elif opcion == '4':
        mi_lista.append(input("ingrese nuevo numero a la lista: "))
        nuevo_numero = mi_lista[-1]
        print("el nuevo numero agregado es: ", nuevo_numero)
    elif opcion == '5':
            dict_1[input("ingresar usuario: ")] = input("ingresar dni: ")
            #print(dict_1)
    elif opcion == '6':
            buscar_usuario = input("ingrese el usuario que quiere buscar: ")
            if buscar_usuario in dict_1:
                dni = dict_1[buscar_usuario]
                print("su DNI es: ",dni)
            else:
                print("este usuario no se encuentra en el sistema, intente nuevamente ")
                buscar_usuario = input("ingrese el usuario que quiere buscar: ")
    elif opcion == '7':
            print("saliendo del sistema...\n ")
            
    else:
        print("opcion incorrecta")

        continuar = False