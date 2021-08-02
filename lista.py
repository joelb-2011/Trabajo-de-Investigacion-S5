from random import randint
import math

def es_primo(num):
    if num == 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

class Lista:
    def __init__(self, lista):
        self.lista = lista
    
    def presentarLista(self):
        for elem in self.lista:
            print(elem, end=" ")
    
    def buscarLista(self, valor):
        try:
            index = self.lista.index(valor)
            print("El valor se encuentra en la posición {}".format(index))
        except: 
            print("El valor no se encuentra en la lista")
    
    def listaFactorial(self):
        for elem in self.lista:
            print(math.factorial(elem), end=" ")
    
    def listaPrimo(self):
        n=int(input("ingrese cantidad de números primos a mostrar: "))
        primos = 0
        num = 1
        lista = []
        while primos < n:
            if(es_primo(num)):
                lista.append(num)
                primos = primos + 1
            num = num + 1
        for elem in lista:
            print(elem, end=" ")

    def listaNotas(self, listaNotasDicccionario):
        for elem in listaNotasDicccionario:
            print(elem, end="\n")

    def insertarLista(self, valor, posicion):
        self.lista.insert(posicion, valor)
        print("Valor insertado!")

    def eliminarLista(self, valor):
        try:
            self.lista.remove(valor)
            print("El valor {} se ha sido eliminado".format(valor))
        except: 
            print("El valor no se encuentra en la lista")
        
    def retornaValorLista(self, posicion):
        try:
            valor = self.lista[posicion]
            del self.lista[posicion]
            print("Se retornó y eliminó el valor {}".format(valor))
        except:
            print("Posición inaccesible")

    def copiarTuplaLista(self, tupla):
        self.lista = self.lista + tupla
        print("Mostrar lista copiada: ")
        for elem in self.lista:
            print(elem, end=" ")

    def vueltoLista(self, listaClientesDiccionario):
        for elem in listaClientesDiccionario:
            elem["vuelto"] = randint(0, 50)
            print(elem, end="\n")