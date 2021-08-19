mi_lista = []

#print(type(mi_lista))

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