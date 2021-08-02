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

