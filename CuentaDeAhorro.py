##elaboro samuel 22/010/18

from Cuenta import *
#importamos la clase de la que vamos a heredar sus metodos y atributos
class CuentaDeAhorro(Cuenta):
    #inicializamos el metodo constructor
    
    def __init__(self,valor, ti):
        #inicializamos el constructor de la clase cuenta
        Cuenta.__init__(self,valor) 
        self.__ti = ti 

    def __str__( self ):
        tmp = "\n\n===================\n Cuenta ahorro\n"
        tmp += "Cantidad disponible en la cuenta:" + str( self.getCantidad())
        tmp += "\nTasa de Interes:" + str( self.__ti)
        return tmp
    def datos(self):
        return "A,"+str(self.getCantidad())+","+str(self.__ti)     
