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
#metodo que comienza a interactuar con un cliente  
    def MenuBanco(self,cliente):
      
        opciones = "Menu Banco"
        opciones += "\n Teclee la opcion correcta"
        opciones += "\n 1.Agregar cliente"
        opciones += "\n 2.Eliminar cliente"
        opciones += "\n 3.Acceder a Menu Cuenta"
        print(opciones)
        
        print(" \n si desea realizar alguna transaccion teclee la opcion 3")
        opcion = input()
        print("Elegiste la opcion:" + opcion)
        if opcion == "1":
            self.MenuagregarClientes(cliente)
        elif opcion =="2":
            self.MenueliminarClientes(cliente)
        elif opcion =="3":
            self.MenuClientes(cliente)

        return
    #metodo que accede a realizar una transaccion
    def MenuClientes(self,cliente):
        print(cliente.banctes()) 
        opc = input(" \n Eliga al cliente que desee realizar la transaccion \n")
        print (int(opc))
        aux = cliente.getCliente(int(opc))
        self.mu.MenuCuenta(aux)
        return

#metodo que agrega clientes
    def MenuagregarClientes(self, cliente):
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
        cliente.agregarClientes(newcte)
        return
 # metodo que elimina clientes  
    def MenueliminarClientes(self, cliente):
        print(" \n Eligió eliminar un cliente")
        print(cliente.banctes())
        opc = input("Eliga el indice del cliente que desee eliminar \n")
        print (int(opc))
        cliente.eliminarClientes(int(opc) )
        print(cliente.banctes())
        return
    