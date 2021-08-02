class Calculadora:
    def __init__(self, numero1, numero2):
        self.num1 = numero1
        self.num2 = numero2
    
    def suma(self):
        return self.num1 + self.num2
    
    
    def resta(self):
        return self.num1 - self.num2
    
    
    def mutiplicacion(self):
        return self.num1 * self.num2
    
    
    def division(self):
        return self.num1 / self.num2

class CalEstandar(Calculadora):
    def __init__(self, numero1, numero2):
            super().__init__(numero1,numero2)


    def mutiplicacion(self): # aplicar polimorfismo
        return self.num1 * self.num2   
    
    
    def exponente(self):
        return self.num1**self.num2
    
    def valorAbsoluto(self,numero1):
        if numero1 <0:
            numero1 = numero1*-1
        return numero1


class CalCientifica(Calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1,numero2)
    
    def  circunferencia(self):
        PI = 3.1416 
        perimetro = 2* PI*self.num1
        return perimetro
    
    def areaCirculo(self):
        PI = 3.1416 
        area = PI*self.num1**2
        return area 
    
    def areaCuadrado(self):
        return self.num2**2  
    
class Basico:
    def __init__(self):
        pass

    def numerosN(self,num1):
        for i in range(1,num1+1):
            print(i,end=" ")
        print("")
        
    def suma(self,num1):
        suma=0
        for i in range(1,num1+1):
            suma+=i
        print("La Suma Es: ",suma)

    def multiplo(self, num1, num2):
        if num1%num2 ==0:
            print("El numero {} si es multiplo de {}".format(num1,num2))
        else:
            print("El numero {} no es multiplo de {}".format(num1,num2))

    def Divisores(self, num1):
        list=[]
        for i in range(1,num1+1):
            if  num1%i==0:
                list.append(i)
        return list
    
    def primo(self, num1):
        c=0
        for i in range(1,num1+1):
            if num1%i==0:
                c+=1
        if c==2:
            return True
        return False

    def perfecto(self,num1):
        suma=0
        for i in range(1,num1):
            if num1%i==0:
                suma+=i
        if suma==num1:
            print("El Número Es Perfecto")
        else:
            print("El Número NO Es Perfecto")

class Intermedio(Basico):
    
    def __init__(self):
        pass
        
    def numerosN(self,n):
        i = 1
        while i <= n:
            print(i)
            i = i + 1
            
    def factorial(self,numero):
        resultado = 1
        for i in range(1, numero + 1):
            resultado = resultado * i
        return resultado
    
    def fibonacci(self,n):
        a = 0
        b = 1
        c=0
        for i in range(n):
            print(a, end=" ")
            c = a+b
            a = b
            b = c
        print()
    def primosGemelos (self,numero1,numero2):
        a = 0
        if numero1 > 0 and numero2 > 0 and numero1 != numero2:
            if numero1 > numero2:
                numero1 ^= numero2
                numero2 ^= numero1
                numero1 ^= numero2
            for i in range (numero1, numero2+1):
                creciente = 2
                esPrimo = True
                
                while esPrimo and creciente < i:
                    if i % creciente == 0:
                        esPrimo = False
                    else:
                        creciente += 1
                if esPrimo and not a:
                    a = i
                elif esPrimo and a:
                    b = i
                    if b-a == 2:
                        print("{} y {} son numeros primos gemelos".format(a, b))
                        a=i
        else:
            if numero1 == numero2:
                print("Incorrecto los numeros son Iguales.")    
            else:
                print("Los numeros son incorrectos.")
                
    def numerosAmigos(self, numero1, numero2):
        acu1 = 0
        lista1 = []
        for i in range(1, numero1):
            if numero1 % i == 0:
                lista1.append(i)
                acu1 = acu1 + i
        acu2 = 0
        lista2 = []
        for x in range(1, numero2):
            if numero2 % x == 0:
                lista2.append(x)
                acu2 = acu2 + x
                
        if acu1 == numero2 and acu2 == numero1:
            print("Los numeros {} y {} son numeros amigos.".format(numero1, numero2))
        else:
            print("Los numeros {} y {} no son numeros amigos.".format(numero1, numero2)) 
            
class TratamientodeLista(Intermedio):
    def __init__(self, lista):
        super().__init__()
        self.lista = lista
    
    def presentarLista(self):
        for elemento in self.lista:
            print(elemento, end=" ")
        print()    
    
    def buscarLista(self, valor):
        if valor in self.lista:
            print("El valor: ", valor, " se encuentra en la lista.")
        else:
            print("El valor: ", valor, " no se encuentra en la lista.")

    def listaFactorial(self):
        factoriales = []
        for elemento in self.lista():
            factoriales.append(super().factorial(elemento))
        return factoriales

    def listaPrimo(self):
        primos = []
        for elemento in self.lista:
            if super().primo(elemento):
                primos.append(elemento)
        return primos

    def listaNotas(self, listaNotasDiccionario):
        for elemento in listaNotasDiccionario:
            print("Alumno: ", elemento, " Calificación: ", listaNotasDiccionario[elemento])

    def insertarLista(self, valor, posicion):
        self.lista.insert(posicion, valor)
    
    def eliminarLista(self, valor):
        try:
            while True:
                self.lista.remove(valor)
        except ValueError:
            pass
    
    def retornaValorLista(self, posicion):
        return self.lista.pop(posicion)

    def copiarTuplaLista(self, tupla):
        return list(tupla)

def vueltoLista(self,listaClientesDiccionario):
        print(" Dar el vuelto a varios clientes ")
        pago=float(input("Ingrese pago del cliente: "))
        nom=(input("Ingrese nombre del cliente: ")).capitalize()
        print(nom)
        for x in listaClientesDiccionario:
            for clave, valor in x.items():     
                if clave == nom:
                    if valor > 0:
                        cambio=pago-valor
                        print(cambio)
                    else:
                        cambio=pago
        if cambio <= -1:                
            print(" Mantiene una deuda de:",cambio,"$ con nosotros")
        else:
            print("su cambio es: ",cambio, "$ no tiene deuda con nosotros")

  
class Cadena():
    def __init__(self,cadena):
        self.cadena=cadena

    def  recorrerCadena(self, buscando):
        for x in self.cadena:
            print(x,'',end='')

        print("Buscar un carácter en una cadena")
        acum=0
        for x,i in enumerate(self.cadena):
            if i== buscando:
                acum=acum+1
        print("Su caracter se encuentra {} vez(veces), dentro de la cadena".format(acum))
        print()

    def  listaPosiciones(self,caracter):
        print("Retornar una lista con la posiciones dado un carácter de la cadena")

        acum=0
        aux=[]
        for x,i in enumerate(self.cadena):
            acum=acum+1
            if i == caracter:
                aux.append(acum)
                lista=aux
        print(lista)        
 
    def listaPalabras(self):

        print("Retornar una lista con todas las palabras de una cadena")
 
        print(self.cadena.split())


        print(" retornar una cadena a partir de una lista")
 
        print(" ".join(self.cadena))

    def insertarDato(self,insertar,posicion):
        if posicion <= len(self.cadena):
            izquierda = self.cadena[:posicion]
            derecha =self.cadena[posicion+1:]
            
            print("{} {} {}".format(izquierda, insertar, derecha))
        else:
            print("La posicion no existe")
        

    def eliminarOcurrencias(self,buscado):

        print("Eliminar todas las ocurrencias en una cadena")


        print("El elemento buscado se encontro {} veces en la cadena".format(self.cadena.count(buscado)))

    def retornaValor(self,posicion):
        lista = []
        lista2 = []
        for pos, ele in enumerate (self.cadena):
            if pos == posicion:
                lista.append(self.cadena[pos])      
            else:
                lista2.append(self.cadena[pos])
        print("Se retorna la cadena de esta forma:")
        print(" ".join(lista2))     
        print("Letra de la posicion removido:")           
        print(" ".join(lista))

    def concatenarCadena(self,nombre):

        dato = "Hola, señor(a)"
        final= "Usted a usado nuestro programa cadena."
        frase= dato+" "+nombre+" "+final
        print(frase)
