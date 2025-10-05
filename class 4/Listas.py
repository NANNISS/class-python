'''
Introducción a las listas en python
'''

#Definición de una lista
array=["futbol","pc",18.6,18,[6,7,8,10],True,False,"pc"]
print(array)

#ACCEDER A UN ELEMENTO DE LA LISTA
print(array[0]) #siempre se inicia desde 0

'''
for(int i=0; i<=0; i++)´{
    system.out.println(i);
}
'''

#buscar valores
print(array[0])
print("pc" in array) #imprime si existe el valor
print("pc" in array)
print(array.index("pc")) #devuelve el indice del elemento
print(len(array)) #devuelve la cantidad de elementos en la lista
print(array.count("pc")) #devuelve la cantidad de veces que se repite
array.clear()#limpiar lista
print("array",array)
array=["futbol","pc",18.6,18,[6,7,8,10],True,False,"pc"]
array.reverse()#invierte lista
print("array invertido",array)
