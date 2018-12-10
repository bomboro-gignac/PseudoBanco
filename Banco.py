from Cuenta import *
from Cliente import *
from CuentaHija import *
from CuentaCredito import *
from CuentaDeAhorro import *
from MenuUsuario import *
from MenuBanco import *
import math 
import numpy as np
import matplotlib.pyplot as plt

#elaboro samuel 22/010/18
#En esta clase es donde convergen todos nuestros metodos 
class Banco:
   #metodo constructor
    def __init__(self,nombre,ubicacion):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.clientes = []
        self.openFile("Archivo.txt")
        '''
        print(len(self.clientes))
        print(self.banctes())
        self.writeFile()
        print("\n"+self.promedio_edad())
        print(self.promedio_cuenta())
        '''
    
    
#metodo que imprime los datos del banco
    def __str__( self ):
        tmp = ""
        tmp += "Nombre del Banco::" + str( self.__nombre)
        tmp += "\nUbicacion::" + str( self.__ubicacion)
        tmp += "\n" +self.banctes()
        
        return tmp
#metodo que agrega un cliente
    def agregarClientes(self,cliente):
        self.clientes.append(cliente)
        self.writeFile()
#metodo que elimina un cliente
    def eliminarClientes(self,cliente):
        del self.clientes[cliente]
        self.writeFile()
#metodo que accede a un cliente del banco
    def getCliente(self,index):
        return self.clientes[index]
#metodo que imprime un cliente
    def opFile():
      self.openFile("Archivo.txt")

    def banctes( self ):
        straux = ""
        for i in range( len(self.clientes)):
            straux = straux + "\n***********\ncliente:"+ str(i) +"\n"+ str(self.clientes[i]  )  
        return straux
#metodo que calcula el promedio de las edades
    def promedio_edad(self):
        n = range (len(self.clientes))
        suma = 0.0
        edades = []
        for i in n:
            suma = suma + self.clientes[i].getedad()
            edades.append(self.clientes[i].getedad())
        plt.hist(edades, bins=60, alpha=1, edgecolor = 'black',  linewidth=1)
        X_1 = []
        Y_1 = []
        plt.plot(X_1,Y_1,"b-")
        plt.xlabel('Edades de los clientes ')
        plt.ylabel('Numero de clientes con la misma edad')
        plt.title('Desviacion Estandar de las edades de los clientes')
        plt.legend()
        plt.savefig("promedio_edad.png")
        plt.show() 
        return suma/len(n)
#metodo que calcula el promedio del saldo inicial de las cuentas de un cliente    
    def promedio_cuenta(self):
        promedio = []
        n = range (len(self.clientes))
        suma = 0.0
        for i in n:
            ctas =  self.clientes[i].getCuentas()
            suma = 0
            for j in range (len(ctas)):
              suma = suma + ctas[j].consulta()
            if (len(ctas) == 0):
                promedio.append(0)
            else :
                promedio.append(suma/len(ctas))
        #print(promedio)
        n, bins, patches = plt.hist(promedio, 10, density=True, facecolor='g', alpha=0.75)
        plt.grid(True)
        plt.savefig("promedio_ctas.png")
        plt.show()  
        
#metodo que calcula la desviacion estandar
    def desviacion_edad(self):
        n = range (len(self.clientes))
        promedio = Banco.promedio_edad(self)
        suma = 0.0
        for i in n:
            suma = suma + (int(self.clientes[i].getedad())-promedio)**2.0
        return str(math.sqrt(suma/len(n)))
      
   
#metodo que abre el archivo txt    
    def openFile(self, name):
        with open("Archivo.txt","r") as archivo_1:
            for linea in archivo_1:
                datos = linea.split(",")
                if (len(datos)==1):
                    continue
                if datos[0]=='N':
                    cte = Cliente (datos[1], int(datos[2]), datos[3])
                    self.clientes.append(cte)
                elif datos[0]=='A':
                    ctaa = CuentaDeAhorro(float(datos[1]),float(datos[2]) )
                    cte.agregarCuentas(ctaa)
                else :
                    ctac = CuentaCredito(float(datos[1]),float(datos[2]))
                    cte.agregarCuentas(ctac)
        archivo_1.close()
#metodo que modifica el archivo
    def writeFile(self):
        with open("Archivo.txt","w") as archivo_1:
            for i in range (len(self.clientes)):
                cte = self.clientes[i]
                archivo_1.write("N,"+cte.getnombre()+","+str(cte.getedad()) +","+cte.getdireccion()+"\n")
                ctas = cte.getCuentas()
                if (len(ctas)==0):
                    archivo_1.write("\n")
                for j in range (len(ctas)):
                    cta = ctas[j]
                    archivo_1.write(cta.datos()+"\n")
        archivo_1.close()