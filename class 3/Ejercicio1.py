'''
Crear un programa que pida dos numeros 
y obtenga como resultado cual 
de ellos es par o si ambos los son
'''

n1=int(input("ingrese el primer numero: "))
n2=int(input("ingrese el segundo numero: "))

espar_n1 = (n1 % 2 == 0)
espar_n2 = (n2 % 2 == 0)

if espar_n1 and espar_n2:
    print("ambos son pares")
elif espar_n1:
    print(f"el primer numero es par : {n1}")
elif espar_n2:
    print(f"el segundo numero es par : {n2}")
else:
    print("ninguno es par ")