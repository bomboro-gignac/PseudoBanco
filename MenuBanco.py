#elaboro samuel 19/11/18
from Cuenta import *
from Cliente import *
from CuentaHija import *
from CuentaCredito import *
from CuentaDeAhorro import *
from MenuUsuario import *
#metodo constructor
class MenuBanco():
    def __init__(self):
        self.mu = MenuUsuario ()
      # self.openFile("Archivo.txt")
       # print(len(self.clientes))
#metodo que comienza a interactuar con un cliente  
    def MenuBanco(self,banco):
        flag = True
        while (flag):
            opciones = "Menu Banco"
            opciones += "\n Teclee la opcion correcta"
            opciones += "\n 1.Agregar cliente"
            opciones += "\n 2.Eliminar cliente"
            opciones += "\n 3.Acceder a Menu Cuenta"
            opciones += "\n 4.Mostrar Datos estadisticos"
            print(opciones)
        
            print(" \n si desea realizar alguna transaccion teclee la opcion 3")
            opcion = input()
            print("Elegiste la opcion:" + opcion)
            if opcion == "1":
                self.MenuagregarClientes(banco)
            elif opcion =="2":
                self.MenueliminarClientes(banco)
            elif opcion =="3":
                self.MenuClientes(banco)
            elif opcion =="4":
                self.MenuDatos(banco)
            opciones = "\n Desea Realizar otra transaccion?"
            opciones += "\n 1.Si"
            opciones += "\n 2.No"
            print(opciones)
            opcion = input()
            if opcion == "2":
                flag = False
        return
    #metodo que accede a realizar una transaccion
    def MenuClientes(self,banco):
        print(banco.banctes()) 
        opc = input(" \n Eliga al cliente que desee realizar la transaccion \n")
        print (int(opc))
        aux = banco.getCliente(int(opc))
        self.mu.MenuCuenta(aux)
        banco.writeFile()
        return

#metodo que agrega clientes
    def MenuagregarClientes(self, banco):
        print( " \n Eligió agregar un cliente")
        print("inserte los siguientes datos:")
        print("Nombre")
        nombre = input("")
        print( "Edad")
        edad = input(" ")
        print( "Direccion")
        direccion = input("")
        print("Nombre del cliente:" + nombre)
        print("Edad:" + edad)
        print("Direccion:" + direccion)
        newcte = Cliente(nombre,edad,direccion)
        banco.agregarClientes(newcte)
        banco.writeFile()
        return
 # metodo que elimina clientes  
    def MenueliminarClientes(self, banco):
        print(" \n Eligió eliminar un cliente")
        print(banco.banctes())
        opc = input("Eliga el indice del cliente que desee eliminar \n")
        print (int(opc))
        banco.eliminarClientes(int(opc) )
        print(banco.banctes())
        banco.writeFile()
        return
    
    def MenuDatos(self,banco):
        print(" \n Eligió mostrar datos estadisticos del banco")
        opciones = "Datos Estadisticos"
        opciones += "\n Teclee la opcion que desee visulizar"
        opciones += "\n 1.Promedio de saldos disponibles entre los usuarios del banco"
        opciones += "\n 2.Desviacion estandar de las Edades de los usuarios"
        print(opciones)
        opcion = input()
        print("Elegiste la opcion:" + opcion)
        
        if opcion == "1":
            banco.promedio_cuenta()
        elif opcion =="2":
            des = banco.desviacion_edad()
            print(des)