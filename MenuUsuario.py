#elaboro samuel 19/11/18
from Cuenta import *
from Cliente import *
from CuentaHija import *
from CuentaCredito import *
from CuentaDeAhorro import *

#metodo constructor
class MenuUsuario :
    def __init__(self):
        pass
#metodo que interactua con una persona donde se pueden elegir 3 opciones
    def MenuCuenta(self,cliente):
        flag = True
        while (flag):
          opciones = "Menu cuenta"
          opciones += "\n Teclee la opcion correcta"
          opciones += "\n 1.Agregar cuenta"
          opciones += "\n 2.Eliminar cuenta"
          opciones += "\n 3.Depositar en cuenta"
          opciones += "\n 4.Retirar dinero de la cuenta"
          print(opciones)
          opcion = input()
          print("Elegiste la opcion:" + opcion)
          print("\n")
          if opcion == "1":
              self.MenuagregarCuentas(cliente)
          elif opcion =="2":
              self.MenuEliminarCuentas(cliente)
          elif opcion =="3":
              self.MenuDepositarCuenta(cliente)
          elif opcion == "4":
              self.MenuRetirarCuenta(cliente)
          opciones = "\n Desea Realizar otra transaccion?"
          opciones += "\n 1.Si"
          opciones += "\n 2.No"
          print(opciones)
          opcion = input()
          if opcion == "2":
              flag = False
        return
        
        
#metodo que elimina una cuenta
    def MenuEliminarCuentas(self, cliente):
        print("\nEligió eliminar una cuenta")
        print(cliente.cteCuentas())
        opc = input("Eliga el indice de la cuenta que desee eliminar \n")
        print (int(opc))
        cliente.eliminarCuentas(int(opc) )
        print(cliente.cteCuentas())
        return 

#metodo que agrega una cuenta     
    def MenuagregarCuentas(self, cliente):
        print( "Eligió agregar una cuenta")
        print("   1.Tipo de cuenta Ahorro")
        print("   2.Tipo de cuenta Credito")
        opc = input("Eliga el tipo de cuenta deseado \n")
        if opc == "1":
            print("Creacion de cuenta de Ahorro")
            print("inserte los siguientes datos:")
            print("saldo inicial")
            saldo  = input("")
            print( "tasa de interes")
            tasa = input(" ")
            print("Saldo inicial establecido:" + saldo)
            print("Tasa de interes acordada:" + tasa)
            ca = CuentaDeAhorro(float(saldo),float(tasa))
            cliente.agregarCuentas(ca)
        elif opc == "2":
            print("Creacion de cuenta de Credito")
            print("inserte los siguientes datos:")
            print("saldo inicial")  
            saldo  = input("")
            print( "sobregiro")
            sobregiro = input(" ")
            print("Saldo inicial establecido:" + saldo)
            print("Sobregiro establecido:" + sobregiro)
            cta = CuentaCredito(int(saldo),int(sobregiro))
            cliente.agregarCuentas(cta)
        return
#metodo que permite depositar dinero en alguna cuenta
    def MenuDepositarCuenta(self, cliente):
        print( " \n Eligió agregar dinero a la cuenta")
        if(len(cliente.cteCuentas())==0):
            print("  El cliente no tiene asignado ninguna cuenta")
            return
        else :
             print(cliente.cteCuentas())
        opc = input(" \n Eliga el indice de la cuenta donde desee agregar dinero \n")
        cliente.getCuenta(int(opc))
        aux = cliente.getCuenta(int(opc))
        print("Cantidad que desea depositar")
        opc = input()
        aux.depositar(int(opc))
        print(cliente.cteCuentas())
        return
#metodo que permite retirar dinero de una uenta
    def MenuRetirarCuenta(self, cliente):
        print( " \n Eligió retirar dinero a la cuenta")
        if(len(cliente.cteCuentas())==0):
            prin("  El cliente no tiene asignado ninguna cuenta")
            return
        else:
            print(cliente.cteCuentas())
        opc = input(" \n Eliga el indice de la cuenta donde desee retirar dinero \n")
        cliente.getCuenta(int(opc))
        aux = cliente.getCuenta(int(opc))
        print("Cantidad que desea retirar")
        opc = float(input())
        aux.retirar(int(opc))
        print(cliente.cteCuentas())
        return