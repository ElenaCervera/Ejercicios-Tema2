# Ejercicio 3
#Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:
#Borrar los elementos duplicados.
#Ordenar la lista de mayor a menor.
#Eliminar todos los números impares.
#Realizar una suma de todos los números que quedan.
#Añadir como primer elemento de la lista la suma realizada.
#Devolver la lista modificada.
#Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:
#nueva_lista = modificar(lista)
#print( nueva_lista[0] == sum(nueva_lista[1:]) )
#True
#Recordatorio
#La función sum(lista) devuelve una suma de los elementos de una lista.

class ej_lista:

  def __init__(self,lista):
    self.lista=lista
  
  def ordenar(self):
    lista=self.lista
    lista.sort(reverse=True) 
    return lista
  def eliminar_impar(self):
    lista_par=[]
    self.lista.sort()
    for n in self.lista:
        if n%2==0:
         lista_par.append(n)
    suma=sum(lista_par)
    lista_par.insert(0,suma)

    return lista_par
  

lista=[15,28,14,69,75,32,1,5,9,78,4,6]
lista_n=ej_lista(lista)
print(lista_n.ordenar())
print(lista_n.eliminar_impar())
print(lista)

nueva_lista=modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )


 
 
 


