##elaboro samuel 22/010/18

from Cuenta import *
#importamos la clase madrte
class Cuentahija(Cuenta):
    def __init__(self, valor, tipo):
        Cuenta.__init__(self, valor)
        self.__tipo = tipo
#inicializamos el constructor
    def __str__( self ):
        msg = Cuenta.__str__(self)
        msg += "\ntipo:" + str( self.__tipo ) 
        return msg 
# metodo str se sobre escribe           
        
""" En la clase hija tratamos de ir adoptando la idea de herencia donde nuestra
    clase Cuenta va a heredar sus atributos y metodos a la clase hija. Notemos que 
    siempre tenemos que inicializar el metodo constructor de nuestra clase "madre" que
    en nuestro caso es la clase Cuenta"""