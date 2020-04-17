
print()

print("primer punto: 1. cantidad de maquinas rayos x en buen estado") 
print("digitar 1 en el Input para la respuesta")

print()

print("segundo punto: 2. cantidad de maquinas tag en mal estado")
print("digitar 4 en el Input para la respuesta")

print()

print("tercer punto: 3.cantidad total de maquinas en stock")
print("digitar 10 en el Input para la respuesta")

print()

a=int(input("digite el tipo de maquina segun las instrucciones: "))

print()

from array import *


cars = [["buen estado", "averiadas"] , ["xray", "tag"] , ["11 maquinas" , "3 maquinas" , "7 maquinas" , "4 maquinas"] , ["25 maquinas en total, 14 en buen estado y 11 averiadas"]]



if a==1 :

    print (cars [0][0])
    print (cars [1][0])
    print (cars [2][0])

elif a==2:

    print (cars [0][1])
    print (cars [1][0])
    print (cars [2][1])
    pass

elif a==3 :

    print (cars [0][0])
    print (cars [1][1])
    print (cars [2][2])
    pass

elif a==4 :

    print (cars [0][1])
    print (cars [1][1])
    print (cars [2][3])
    pass

elif a==10 :

    print (cars [3])
    pass

print()