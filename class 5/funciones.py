'''
Funciones en python
'''

def sumar(a,b):
    r=a+b
    print(f"sumando dentro de la funcion {a} + {b}=" ) #otra forma de mostrar los datos
    return r
resultado=sumar(5,3)
print("el resultado de la suma es: {resultado}")

#ó

a=5
b=3
resultado=sumar(a,b)
print("-------fuera de la función-----------")
print(f"El resultado de la suma es: {resultado}")
