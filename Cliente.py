#elaboro samuel 22/010/18

from Cuenta import *

#metodo constructor
class Cliente:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.cuentas = []
    
    # el metodo mostrar detalles lo sustituimos por el metodo __str__
    """def mostrarDetalles (self):
        print ("\n Informacion del cliente")
        print ("\n", self.__nombre)
        print ("\n", self.__edad)
        print ("\n", self.__direccion) """
        
        
  # modificamos el metodo __str__ pues ahora son varias cuentas   
    """def __str__( self ):
        tmp = ""
        tmp += "Nombre::" + str( self.__nombre)
        tmp += "\nDireccion::" + str( self.__direccion)
        tmp += "\nEdad::" + str( self.__edad)
        tmp += "\n" + str(self.__cuenta)
        return tmp"""    
    # __str__ sobreescribe el metodo str devolviendo un string
    def getnombre(self):
      return self.nombre
    def setedad(self, edad):
       self.__edad = edad

    def getedad (self):
       return self.edad

    def setdireccion(self, direccion):
       self.__direccion = direccion

    def getdireccion (self):
       return self.direccion

    #puse los set y get para poder modificar los atributos pues pienso que pueden ir cambiando y no son constantes   
       
#metodo que agrega una cuenta
    def agregarCuentas(self,cuenta):
        self.cuentas.append(cuenta)
        return

#metodo que elimina una cuenta
    def eliminarCuentas(self,cuenta):
        del self.cuentas[cuenta]
        return

#metodo que accede a una cuenta a traves de su lugar en la lista
    def getCuentas(self):
        return self.cuentas
    def getCuenta(self,index):
        return self.cuentas[index]

#metodo que imprime los datos del cliente
    def __str__( self ):
        tmp = "Nombre::" + str( self.nombre )
        tmp += "\nDireccion::" + str( self.direccion )
        tmp += "\nEdad::" + str( self.edad )
        tmp += "\n" +self.cteCuentas()
        return tmp
#metodo que imprime las cuentas del cliente
    def cteCuentas( self ):
        straux = ""
        for i in range( len(self.cuentas)):
            straux = straux + "\n\ncuenta: "+ str(i) +"\n"+ str(self.cuentas[i] )
            
        return straux

    
     

           


