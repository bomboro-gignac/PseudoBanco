#elaboro samuel 22/010/18

from Cuenta import *

class Cliente:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.cuentas = []
    #metodo constructor
    
    """def mostrarDetalles (self):
        print ("\n Informacion del cliente")
        print ("\n", self.__nombre)
        print ("\n", self.__edad)
        print ("\n", self.__direccion) """
    
    # el metodo mostrar detalles lo sustituimos por el metodo __str__
    
    """def __str__( self ):
        tmp = ""
        tmp += "Nombre::" + str( self.__nombre)
        tmp += "\nDireccion::" + str( self.__direccion)
        tmp += "\nEdad::" + str( self.__edad)
        tmp += "\n" + str(self.__cuenta)
        return tmp"""
    # __str__ sobreescribe el metodo str devolviendo un string
    
    def setedad(self, edad):
        self.__edad = edad
    
    def getedad (self):
        return self.__edad
    
    def setdireccion(self, direccion):
        self.__direccion = direccion
    
    def getdireccion (self):
        return self.__direccion
    
    #puse los set y get para poder modificar los atributos pues pienso que pueden ir cambiando y no son constantes
    
    
    def agregarCuentas(self,cuenta):
        self.cuentas.append(cuenta)
    
    def eliinarCuentas(self,cuenta):
        self.cuentas.remove(cuenta)
    
    def getCuenta(self,index):
        return self.cuentas[index]
    
    def __str__( self ):
        tmp = "Nombre::" + str( self.nombre )
        tmp += "\nDireccion::" + str( self.direccion )
        tmp += "\nEdad::" + str( self.edad )
        tmp += "\n" +self.cteCuentas()
        return tmp
    
    def cteCuentas( self ):
        straux = ""
            for i in range( len(self.cuentas)):
                if type(self.cuentas[i]) is "'CuentaCredito.CuentaCredito'" :
                    print ( str(type(self.cuentas[i])) + " : ")
                        else:
                            print ( str(type(self.cuentas[i])) + " ++ ")
                                #straux= straux+str(i)+ "  " + str(self.cuentas[i] )
                                return straux




